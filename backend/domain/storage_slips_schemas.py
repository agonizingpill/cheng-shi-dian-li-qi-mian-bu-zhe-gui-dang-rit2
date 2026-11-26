from typing import Annotated

from pydantic import BaseModel, ConfigDict, FiniteFloat, StringConstraints

class HandoffFlag(BaseModel):
    model_config = ConfigDict(extra="forbid")
    code: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=160)]
    guide: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=160)]
    action: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=160)]
    locker: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=160)]
    witness: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=160)]
