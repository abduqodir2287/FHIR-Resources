import rfc3986
from rfc3986.validators import Validator
from pydantic import BaseModel, Field, model_validator
from fastapi import HTTPException, status
from typing import Optional

from src.domain.patient.schemas.identifier.enums import IdentifierCode
from src.domain.patient.schemas.identifier.codable_concept import CodableConcept
from src.domain.patient.schemas.time_resources.period import Period


class Identifier(BaseModel):
	use: Optional[IdentifierCode] = Field(None, description="usual | official | temp | secondary | old (If known)")
	type: Optional[CodableConcept] = Field(None, description="Description of identifier")
	system: Optional[str] = Field(None, description="The namespace for the identifier value")
	value: Optional[str] = Field(None, description="The value that is unique")
	period: Optional[Period] = Field(None, description="Time period when id is/was valid for use")
	assigner: Optional[str] = Field(None, description="Organization that issued id (may be just text)")


	@model_validator(mode="before")
	def validator_system(cls, values) -> None:
		uri = rfc3986.uri_reference(values.get("system"))

		validator = Validator().require_presence_of("scheme", "host")
		try:
			validator.validate(uri)

		except Exception:
			raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
			                    detail=f"URI '{values.get('system')}' does not conform to RFC 3986")

		return values


