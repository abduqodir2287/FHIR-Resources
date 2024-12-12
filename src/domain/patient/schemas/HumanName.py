from pydantic import BaseModel, Field
from typing import Optional

from src.domain.patient.enums import HumanNameCode
from src.domain.patient.schemas.time_resources.period import Period


class HumanName(BaseModel):
	use: Optional[HumanNameCode] = Field(None, description="usual | official | temp | nickname | anonymous | old | maiden")
	text: Optional[str] = Field(None, description="Text representation of the full name")
	family: Optional[str] = Field(None, description="Family name (often called 'Surname')")
	given: list[Optional[str]] = Field(None, description="Given names (not always 'first'). Includes middle names")
	prefix: list[Optional[str]] = Field(None, description="Parts that come before the name")
	suffix: list[Optional[str]] = Field(None, description="Parts that come after the name")
	period: Optional[Period] = Field(None, description="Time period when name was/is in use")

