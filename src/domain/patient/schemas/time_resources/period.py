from datetime import datetime
from typing import Optional

from fastapi import HTTPException
from pydantic import BaseModel, model_validator, Field


class Period(BaseModel):
	start: Optional[datetime] = Field(None, description="Starting time with inclusive boundary")
	end: Optional[datetime] = Field(None, description="End time with inclusive boundary, if not ongoing")

	@model_validator(mode="before")
	def check_period(cls, values):
		start = values.get("start")
		end = values.get("end")

		if start and end is not None:

			if start > end:
				raise HTTPException(status_code=400, detail='The end date must be greater than or equal to the start date.')

		return values


