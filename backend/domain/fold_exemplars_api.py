from fastapi import APIRouter, Depends

from core.auth import actor, allow
from core.audit import record
from core.db import transaction
from core.records import scan
from domain import fold_exemplars_service as service
from domain.fold_exemplars_model import fold_exemplars
from domain.fold_exemplars_schemas import FindExemplar, SaveExemplar

router = APIRouter()

@router.get('/fold_exemplars')
def list_fold_exemplars(user=Depends(actor)):
    with transaction() as conn:
        return scan(conn, fold_exemplars)


@router.post('/fold_exemplars/find-exemplar')
def find_exemplar(data: FindExemplar, user=Depends(actor)):
    allow(user, ('operator', 'reviewer'))
    with transaction() as conn:
        output = service.find_exemplar(conn, user, data)
        record(conn, user, 'fold_exemplars.find_exemplar')
        return output


@router.post('/fold_exemplars/save-exemplar')
def save_exemplar(data: SaveExemplar, user=Depends(actor)):
    allow(user, ('reviewer',))
    with transaction() as conn:
        output = service.save_exemplar(conn, user, data)
        record(conn, user, 'fold_exemplars.save_exemplar')
        return output
