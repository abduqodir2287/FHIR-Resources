import rfc3986

from rfc3986.validators import Validator
from pydantic import BaseModel, Field, model_validator
from typing import Optional
from fastapi import HTTPException, status


class Coding(BaseModel):
	system: Optional[str] = Field(None, description="Identity of the terminology system")
	version: Optional[str] = Field(None, description="Version of the system - if relevant")
	code: Optional[str] = Field(None, description="Symbol in syntax defined by the system")
	display: Optional[str] = Field(None, description="Representation defined by the system")
	userSelected: Optional[bool] = Field(None, description="If this coding was chosen directly by the user")


	@model_validator(mode="before")
	def system_validator(cls, values) -> None:
		uri = rfc3986.uri_reference(values.get("system"))

		validator = Validator().require_presence_of("scheme", "host")
		try:
			validator.validate(uri)

		except Exception:
			raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
			                    detail=f"URI '{values.get('system')}' does not conform to RFC 3986")

		return values


	@model_validator(mode="before")
	def code_validator(cls, values) -> None:
		code = values.get("code")

		if not code or not code.strip() or "  " in code or code != code.strip():
			raise HTTPException(
				status_code=status.HTTP_400_BAD_REQUEST,
				detail="The 'code' field must be a string containing at least one character, "
				       "without leading or trailing spaces, and without double spaces."
			)

		return values

