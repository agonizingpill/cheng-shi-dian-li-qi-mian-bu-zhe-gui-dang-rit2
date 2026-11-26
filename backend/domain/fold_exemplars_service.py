from sqlalchemy import select

from core.queueing import submit, result
from core.records import get, insert, need, scan, update
from domain.flag_archive_model import flag_archive
from domain.crease_samples_model import crease_samples
from domain.fold_exemplars_model import fold_exemplars
from domain.model_trials_service import current_live
from domain.storage_slips_model import storage_slips


def find_exemplar(conn, user, data):
    query=get(conn,crease_samples,data.sample)
    live=current_live(conn)
    if live:
        pool=[get(conn,crease_samples,code) for code in live['fit'] if code!=data.sample]
        version=live['code']
    else:
        pool=[x for x in scan(conn,crease_samples) if x['signed'] and x['code']!=data.sample]
        version=None
    need(query['signed'] and len(pool)>=10,'签认样条和参考不足')
    return submit(user,{'kind':'lookup','version':version,'query':query,'references':pool})


def save_exemplar(conn, user, data):
    run=result(user,data.token)
    need(run['input'].get('kind','lookup')=='lookup','该计算号不是代表样查找')
    stats=run['result']
    return insert(conn,fold_exemplars,code=data.code,sample=run['input']['query']['code'],
      example=stats['exemplar'],group_size=stats['group_size'],token=data.token,
      version=run['input'].get('version'))
