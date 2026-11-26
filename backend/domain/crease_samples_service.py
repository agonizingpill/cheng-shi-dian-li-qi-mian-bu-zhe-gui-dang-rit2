from sqlalchemy import select

from core.queueing import submit, result
from core.records import get, insert, need, scan, update
from domain.flag_archive_model import flag_archive
from domain.crease_samples_model import crease_samples
from domain.fold_exemplars_model import fold_exemplars
from domain.storage_slips_model import storage_slips


def capture_crease(conn, user, data):
    asset=get(conn,flag_archive,data.flag,lock=True)
    need(not asset['displayed'],'旗面仍在仪典现场')
    need(0<data.depth<=20 and 0<data.width<=100 and 1<=data.lines<=20,'折痕读数越界')
    return insert(conn,crease_samples,**data.model_dump(),signed=False)


def verify_crease(conn, user, data):
    row=get(conn,crease_samples,data.sample,lock=True)
    need(not get(conn,flag_archive,row['flag'])['displayed'],'旗面仍在仪典现场')
    return update(conn,crease_samples,data.sample,signed=True)
