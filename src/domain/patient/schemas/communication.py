from pydantic import BaseModel, Field
from typing import Optional

from src.domain.patient.schemas.identifier.codable_concept import CodableConcept


class Communication(BaseModel):
	language: CodableConcept = Field(
		..., description="The language which can be used to communicate with the patient about his or her health")
	preferred: Optional[bool] = Field(None, description="Language preference indicator")

