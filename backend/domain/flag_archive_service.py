from sqlalchemy import select

from core.queueing import submit, result
from core.records import get, insert, need, scan, update
from domain.flag_archive_model import flag_archive
from domain.crease_samples_model import crease_samples
from domain.fold_exemplars_model import fold_exemplars
from domain.storage_slips_model import storage_slips


def return_flag(conn, user, data):
    old=get(conn,flag_archive,data.flag,lock=True)
    need(old['displayed'] and data.receipt.startswith('RETURN-'),'旗面未借出或缺少归还凭据')
    return update(conn,flag_archive,data.flag,displayed=False)
