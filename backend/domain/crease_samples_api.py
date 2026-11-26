from fastapi import APIRouter, Depends

from core.auth import actor, allow
from core.audit import record
from core.db import transaction
from core.records import scan
from domain import crease_samples_service as service
from domain.crease_samples_model import crease_samples
from domain.crease_samples_schemas import CaptureCrease, VerifyCrease

router = APIRouter()

@router.get('/crease_samples')
def list_crease_samples(user=Depends(actor)):
    with transaction() as conn:
        return scan(conn, crease_samples)


@router.post('/crease_samples/capture-crease')
def capture_crease(data: CaptureCrease, user=Depends(actor)):
    allow(user, ('operator', 'reviewer'))
    with transaction() as conn:
        output = service.capture_crease(conn, user, data)
        record(conn, user, 'crease_samples.capture_crease')
        return output


@router.post('/crease_samples/verify-crease')
def verify_crease(data: VerifyCrease, user=Depends(actor)):
    allow(user, ('reviewer',))
    with transaction() as conn:
        output = service.verify_crease(conn, user, data)
        record(conn, user, 'crease_samples.verify_crease')
        return output
