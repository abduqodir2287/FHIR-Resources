from pydantic import BaseModel, Field

from src.domain.patient.enums import LinkTypeCode
from src.domain.patient.schemas.reference import Reference


class Link(BaseModel):
	other: Reference = Field(..., description="The other patient or related person resource that the link refers to")
	type: LinkTypeCode = Field(..., description="replaced-by | replaces | refer | seealso")

