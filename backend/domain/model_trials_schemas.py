from typing import Annotated

from pydantic import BaseModel, ConfigDict, StringConstraints

class LaunchTrial(BaseModel):
    model_config = ConfigDict(extra="forbid")
    code: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=160)]
    holdout: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=1600)]


class TrialCode(BaseModel):
    model_config = ConfigDict(extra="forbid")
    code: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=160)]
