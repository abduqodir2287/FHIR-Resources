from typing import Optional
from pydantic import BaseModel, model_validator, Field
from fastapi import HTTPException, status


class MultipleBirth(BaseModel):
	multipleBirthBoolean: Optional[bool] = Field(None)
	multipleBirthInteger: Optional[int] = Field(None)

	@model_validator(mode="before")
	def validate_deceased_fields(cls, values):
		multipleBirthBoolean = values.get('multipleBirthBoolean')
		multipleBirthInteger = values.get('multipleBirthInteger')

		if multipleBirthBoolean is not None and multipleBirthBoolean is False:
			if multipleBirthInteger is not None or multipleBirthInteger == 0:

				raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
				                    detail="When 'multipleBirthBoolean' is False, 'multipleBirthInteger' must be None.")

		elif multipleBirthBoolean is None and multipleBirthInteger is not None:
			raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
			                    detail="When 'deceasedBoolean' is None, 'deceasedDateTime' must be None.")

		return values


