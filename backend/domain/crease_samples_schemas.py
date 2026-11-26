from typing import Annotated

from pydantic import BaseModel, ConfigDict, FiniteFloat, StringConstraints

class CaptureCrease(BaseModel):
    model_config = ConfigDict(extra="forbid")
    code: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=160)]
    flag: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=160)]
    depth: FiniteFloat
    width: FiniteFloat
    lines: int


class VerifyCrease(BaseModel):
    model_config = ConfigDict(extra="forbid")
    sample: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=160)]
