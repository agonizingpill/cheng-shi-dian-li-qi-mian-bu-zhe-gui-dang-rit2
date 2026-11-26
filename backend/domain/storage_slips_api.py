from fastapi import APIRouter, Depends

from core.auth import actor, allow
from core.audit import record
from core.db import transaction
from core.records import scan
from domain import storage_slips_service as service
from domain.storage_slips_model import storage_slips
from domain.storage_slips_schemas import HandoffFlag

router = APIRouter()

@router.get('/storage_slips')
def list_storage_slips(user=Depends(actor)):
    with transaction() as conn:
        return scan(conn, storage_slips)


@router.post('/storage_slips/handoff-flag')
def handoff_flag(data: HandoffFlag, user=Depends(actor)):
    allow(user, ('reviewer',))
    with transaction() as conn:
        output = service.handoff_flag(conn, user, data)
        record(conn, user, 'storage_slips.handoff_flag')
        return output
