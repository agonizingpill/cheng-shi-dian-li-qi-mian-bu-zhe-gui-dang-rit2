from sqlalchemy import select

from core.queueing import submit, view
from core.records import get, insert, need, scan, update
from domain.crease_samples_model import crease_samples
from domain.model_trials_model import model_trials

TRIALING = '试算中'
READY = '待批准'
LIVE = '在用'
RETIRED = '已换下'
MIN_REFERENCES = 10


def current_live(conn, lock=False):
    query = select(model_trials).where(model_trials.c.status == LIVE)
    if lock:
        query = query.with_for_update()
    row = conn.execute(query).mappings().first()
    return dict(row) if row else None


def holdout_codes(raw):
    codes = [part.strip() for part in raw.replace('，', ',').split(',')]
    codes = [code for code in codes if code]
    need(codes and len(set(codes)) == len(codes), '请提供不同的留样编号')
    return codes


def trial_payload(conn, trial, baseline):
    holdout_rows = [get(conn, crease_samples, code) for code in trial['holdout']]
    flags = {row['flag'] for row in holdout_rows}
    fit_rows = [get(conn, crease_samples, code) for code in trial['fit']]
    fit_rows = [row for row in fit_rows if row['flag'] not in flags]
    baseline_fit = None
    if baseline is not None:
        baseline_fit = [get(conn, crease_samples, code) for code in baseline['fit']]
        baseline_fit = [row for row in baseline_fit if row['flag'] not in flags]
        need(len(baseline_fit) >= MIN_REFERENCES, '对照版扣除留样旗面后参考不足')
    return {'kind': 'trial', 'trial': trial['code'], 'fit': fit_rows,
            'holdout': holdout_rows, 'baseline_fit': baseline_fit}


def launch_trial(conn, user, data):
    present = conn.execute(select(model_trials.c.code).where(model_trials.c.code == data.code)).first()
    need(present is None, '版本号已存在')
    codes = holdout_codes(data.holdout)
    signed = [row for row in scan(conn, crease_samples) if row['signed']]
    by_code = {row['code']: row for row in signed}
    need(all(code in by_code for code in codes), '留样须为已签认样条')
    flags = {by_code[code]['flag'] for code in codes}
    fit = [row['code'] for row in signed if row['flag'] not in flags]
    need(len(fit) >= MIN_REFERENCES, '签认样条和参考不足')
    trial = {'code': data.code, 'fit': fit, 'holdout': codes}
    live = current_live(conn)
    payload = trial_payload(conn, trial, live)
    outcome = submit(user, payload)
    insert(conn, model_trials, code=data.code, fit=fit, holdout=codes,
           baseline=live['code'] if live else None, status=TRIALING,
           token=outcome['token'], report=None)
    return outcome


def resume_trial(conn, user, data):
    trial = get(conn, model_trials, data.code)
    need(trial['status'] == TRIALING, '仅试算中的版本可续跑')
    live = current_live(conn)
    payload = trial_payload(conn, trial, live)
    outcome = submit(user, payload)
    update(conn, model_trials, data.code, token=outcome['token'],
           baseline=live['code'] if live else None)
    return outcome


def collect_trial(conn, user, data):
    trial = get(conn, model_trials, data.code)
    need(trial['status'] == TRIALING, '仅试算中的版本可收取报告')
    run = view(user, trial['token'])
    need(run['status'] != 'rejected', '试算计算被拒绝：' + run.get('detail', ''))
    need(run['status'] == 'ready', '等待计算完成后再收取')
    update(conn, model_trials, data.code, status=READY, report=run['result'])
    return get(conn, model_trials, data.code)


def recompare_trial(conn, user, data):
    trial = get(conn, model_trials, data.code)
    need(trial['status'] == READY, '仅待批准的版本可重新比对')
    live = current_live(conn)
    need(live is not None, '尚无在用版可对照')
    need(live['code'] != trial['baseline'], '对照版未换下，无需重新比对')
    payload = trial_payload(conn, trial, live)
    outcome = submit(user, payload)
    update(conn, model_trials, data.code, status=TRIALING, token=outcome['token'],
           baseline=live['code'], report=None)
    return outcome


def approve_trial(conn, user, data):
    trial = get(conn, model_trials, data.code, lock=True)
    need(trial['status'] == READY, '仅待批准的版本可批准上线')
    live = current_live(conn, lock=True)
    current = live['code'] if live else None
    need(trial['baseline'] == current, '对照版已被换下，请重新比对后再批准')
    if live:
        update(conn, model_trials, live['code'], status=RETIRED)
    return update(conn, model_trials, data.code, status=LIVE)
