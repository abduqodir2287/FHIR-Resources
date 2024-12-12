from pydantic import BaseModel, Field, model_validator, AnyUrl
from fastapi import HTTPException, status
from typing import Optional
from urllib.parse import urlparse

from src.domain.patient.schemas.identifier.identifier import Identifier


class Reference(BaseModel):
	reference: Optional[str] = Field(None, description="Literal reference, Relative, internal or absolute URL")
	type: Optional[AnyUrl] = Field(
		None, description="Type the reference refers to (e.g. 'Patient') - must be a resource in resources")
	identifier: Optional[Identifier] = Field(None, description="Logical reference, when literal reference is not known")
	display: Optional[str] = Field(None, description="Text alternative for the resource")


	@model_validator(mode="before")
	def validate_reference(cls, values) -> None:
		reference = values.get("reference")

		parsed = urlparse(reference)

		if not parsed.scheme and not reference.startswith("/"):
			raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid relative path or absolute URL")

		if parsed.scheme and not parsed.netloc:
			raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid absolute URL")

		return values



