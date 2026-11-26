from sqlalchemy import select

from core.queueing import submit, result
from core.records import get, insert, need, scan, update
from domain.flag_archive_model import flag_archive
from domain.crease_samples_model import crease_samples
from domain.fold_exemplars_model import fold_exemplars
from domain.storage_slips_model import storage_slips


def find_exemplar(conn, user, data):
    query=get(conn,crease_samples,data.sample)
    pool=[x for x in scan(conn,crease_samples) if x['signed'] and x['code']!=data.sample]
    need(query['signed'] and len(pool)>=10,'签认样条和参考不足')
    return submit(user,{'query':query,'references':pool})


def save_exemplar(conn, user, data):
    run=result(user,data.token); stats=run['result']
    return insert(conn,fold_exemplars,code=data.code,sample=run['input']['query']['code'],
      example=stats['exemplar'],group_size=stats['group_size'],token=data.token)
