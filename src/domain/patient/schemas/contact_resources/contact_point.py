import phonenumbers
from fastapi import HTTPException
from pydantic import BaseModel, PositiveInt, model_validator, Field
from typing import Optional
from email_validator import validate_email, EmailNotValidError
import validators

from src.configs.logger_setup import logger
from src.domain.patient.schemas.time_resources.period import Period
from src.domain.patient.schemas.contact_resources.enums import ContactSystemCode, ContactUseCode


class ContactPoint(BaseModel):
	system: Optional[ContactSystemCode] = Field(None, description="phone | fax | email | pager | url | sms | other")
	value: Optional[str] = Field(None, description="The actual contact point details")
	use: Optional[ContactUseCode] = Field(
		None, description="home | work | temp | old | mobile - purpose of this contact point")
	rank: Optional[PositiveInt] = Field(None, description="Specify preferred order of use (1 = highest)")
	period: Optional[Period] = Field(None, description="Time period when the contact point was/is in use")


	@model_validator(mode="before")
	def check_value(cls, values):
		system = values.get("system")
		value = values.get("value")

		if system and value is not None:
			if system in [ContactSystemCode.phone, ContactSystemCode.fax, ContactSystemCode.sms,
			              ContactSystemCode.pager]:

				try:
					phone_number = phonenumbers.parse(value)

					if not phonenumbers.is_valid_number(phone_number):
						raise HTTPException(status_code=400, detail=f'Invalid PhoneNumber format')

				except Exception as e:
					logger.warning(f"{e}")
					raise HTTPException(status_code=400, detail=f'Invalid PhoneNumber format')

			elif system == ContactSystemCode.email:

				try:
					validate_email(value)

				except EmailNotValidError:
					raise HTTPException(status_code=400, detail='Invalid email format')

			elif system == ContactSystemCode.url:

				if not validators.url(value):
					raise HTTPException(status_code=400, detail='Invalid URL format')

		return values

