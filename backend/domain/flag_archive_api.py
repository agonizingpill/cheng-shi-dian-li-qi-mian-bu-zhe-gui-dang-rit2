from fastapi import APIRouter, Depends

from core.auth import actor, allow
from core.audit import record
from core.db import transaction
from core.records import scan
from domain import flag_archive_service as service
from domain.flag_archive_model import flag_archive
from domain.flag_archive_schemas import ReturnFlag

router = APIRouter()

@router.get('/flag_archive')
def list_flag_archive(user=Depends(actor)):
    with transaction() as conn:
        return scan(conn, flag_archive)


@router.post('/flag_archive/return-flag')
def return_flag(data: ReturnFlag, user=Depends(actor)):
    allow(user, ('reviewer',))
    with transaction() as conn:
        output = service.return_flag(conn, user, data)
        record(conn, user, 'flag_archive.return_flag')
        return output
