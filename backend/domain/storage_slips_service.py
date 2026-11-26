from sqlalchemy import select

from core.queueing import submit, result
from core.records import get, insert, need, scan, update
from domain.flag_archive_model import flag_archive
from domain.crease_samples_model import crease_samples
from domain.fold_exemplars_model import fold_exemplars
from domain.storage_slips_model import storage_slips


def handoff_flag(conn, user, data):
    guide=get(conn,fold_exemplars,data.guide)
    sample=get(conn,crease_samples,guide['sample'])
    flag=get(conn,flag_archive,sample['flag'],lock=True)
    witnesses=[name.strip() for name in data.witness.split('/')]
    need(len(witnesses)==2 and len(set(witnesses))==2 and all(witnesses),'请提供两位不同的替班保管员')
    need(not flag['displayed'],'待归还的旗面不可移交')
    need(data.action in ('平放复核','照册重折','特殊保管'),'未列入归档动作')
    need(not flag['heritage'] or data.action=='特殊保管','礼藏原件禁止重折或展开，只登记特殊保管')
    return insert(conn,storage_slips,**data.model_dump(),flag=flag['code'])
