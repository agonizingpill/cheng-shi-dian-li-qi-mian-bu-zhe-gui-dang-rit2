from fastapi import APIRouter, Depends

from core.auth import actor, allow
from core.audit import record
from core.db import transaction
from core.records import scan
from domain import model_trials_service as service
from domain.model_trials_model import model_trials
from domain.model_trials_schemas import LaunchTrial, TrialCode

router = APIRouter()

@router.get('/model_trials')
def list_model_trials(user=Depends(actor)):
    with transaction() as conn:
        return scan(conn, model_trials)


@router.post('/model_trials/launch-trial')
def launch_trial(data: LaunchTrial, user=Depends(actor)):
    allow(user, ('operator', 'reviewer'))
    with transaction() as conn:
        output = service.launch_trial(conn, user, data)
        record(conn, user, 'model_trials.launch_trial')
        return output


@router.post('/model_trials/resume-trial')
def resume_trial(data: TrialCode, user=Depends(actor)):
    allow(user, ('operator', 'reviewer'))
    with transaction() as conn:
        output = service.resume_trial(conn, user, data)
        record(conn, user, 'model_trials.resume_trial')
        return output


@router.post('/model_trials/collect-trial')
def collect_trial(data: TrialCode, user=Depends(actor)):
    allow(user, ('operator', 'reviewer'))
    with transaction() as conn:
        output = service.collect_trial(conn, user, data)
        record(conn, user, 'model_trials.collect_trial')
        return output


@router.post('/model_trials/recompare-trial')
def recompare_trial(data: TrialCode, user=Depends(actor)):
    allow(user, ('operator', 'reviewer'))
    with transaction() as conn:
        output = service.recompare_trial(conn, user, data)
        record(conn, user, 'model_trials.recompare_trial')
        return output


@router.post('/model_trials/approve-trial')
def approve_trial(data: TrialCode, user=Depends(actor)):
    allow(user, ('reviewer',))
    with transaction() as conn:
        output = service.approve_trial(conn, user, data)
        record(conn, user, 'model_trials.approve_trial')
        return output
