from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, model_validator
from fastapi import HTTPException, status


class Deceased(BaseModel):
	deceasedBoolean: Optional[bool] = Field(None, description="Indicates if the individual is deceased as a boolean.")
	deceasedDateTime: Optional[datetime] = Field(None,
	                                             description="Indicates when the individual is deceased as a dateTime.")

	@model_validator(mode="before")
	def validate_deceased_fields(cls, values):
		deceased_boolean = values.get('deceasedBoolean')
		deceased_datetime = values.get('deceasedDateTime')

		if deceased_boolean is not None and deceased_boolean is False:
			if deceased_datetime is not None:

				raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
				                    detail="When 'deceasedBoolean' is False, 'deceasedDateTime' must be None.")

		elif deceased_boolean is None and deceased_datetime is not None:
			raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
			                    detail="When 'deceasedBoolean' is None, 'deceasedDateTime' must be None.")

		return values


