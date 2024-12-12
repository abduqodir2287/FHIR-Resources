from pydantic import BaseModel, Field
from typing import Optional

from src.domain.patient.schemas.identifier.coding import Coding


class CodableConcept(BaseModel):
	coding: list[Optional[Coding]] = Field(None, description="Code defined by a terminology system")
	text: Optional[str] = Field(None, description="Plain text representation of the concept")


