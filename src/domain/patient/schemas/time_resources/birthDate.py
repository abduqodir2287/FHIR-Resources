from datetime import datetime
from fastapi import HTTPException, status
from pydantic import BaseModel, Field, model_validator
from typing import Optional

from src.configs.logger_setup import logger


class Date(BaseModel):
	date: Optional[str] = Field(
		None, description="The person's date of birth in the format 'YYYY', 'YYYY-MM' or 'YYYY-MM-DD'.",
		examples=["2000-01-01", "2000-01", "2000"]
	)

	@model_validator(mode="before")
	def validate_birth_date(cls, values):
		date = values.get("date")

		try:
			if len(date) == 4:
				datetime.strptime(date, "%Y")

				return values

			elif len(date) == 7:
				datetime.strptime(date, "%Y-%m")

				return values

			elif len(date) == 10:
				datetime.strptime(date, "%Y-%m-%d")

				return values


		except ValueError as e:
			logger.warning(f"{e}")

		raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
		                    detail="The date must be in the format 'YYYY', 'YYYY-MM' or 'YYYY-MM-DD'.")

