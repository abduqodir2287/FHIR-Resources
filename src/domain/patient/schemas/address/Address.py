from pydantic import BaseModel, Field
from typing import Optional

from src.domain.patient.schemas.address.enums import AddressUse, AddressType
from src.domain.patient.schemas.time_resources.period import Period


class Address(BaseModel):
	use: Optional[AddressUse] = Field(None, description="Purpose of this address")
	type: Optional[AddressType] = Field(None, description="The type of this address")
	text: Optional[str] = Field(None, description="Text representation of the address")
	line: list[Optional[str]] = Field(None, description="Street name, number, direction & P.O. Box etc.")
	city: Optional[str] = Field(None, description="Name of city, town etc.")
	district: Optional[str] = Field(None, description="District name (aka county)")
	state: Optional[str] = Field(None, description="Sub-unit of country (abbreviations ok)")
	postalCode: Optional[str] = Field(None, description="Postal code for area")
	country: Optional[str] = Field(None, description="Country (e.g. may be ISO 3166 2 or 3 letter code)")
	period: Optional[Period] = Field(None, description="Time period when address was/is in use")


