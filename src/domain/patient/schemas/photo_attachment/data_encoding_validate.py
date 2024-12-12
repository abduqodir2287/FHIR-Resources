import base64
from pydantic import constr, model_validator, BaseModel
from fastapi import HTTPException, status

from src.configs.logger_setup import logger


class DataModel(BaseModel):
	data: str = constr(min_length=1)


	@model_validator(mode="before")
	def validate(cls, value):
		try:
			base64.b64decode(value["data"], validate=True)

		except Exception:
			logger.info("Данные не закодированы в формате base64.")
			raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Data must be encoded in base64 format.")

		return value

