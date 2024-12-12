from pydantic import BaseModel, Field
from typing import Optional

from src.domain.patient.enums import GenderCode
from src.domain.patient.schemas.HumanName import HumanName
from src.domain.patient.schemas.address.Address import Address
from src.domain.patient.schemas.contact_resources.contact_point import ContactPoint
from src.domain.patient.schemas.identifier.codable_concept import CodableConcept
from src.domain.patient.schemas.time_resources.period import Period


class Contact(BaseModel):
	relationship: list[Optional[CodableConcept]] = Field(None, description="The kind of personal relationship")
	role: list[Optional[CodableConcept]] = Field(None, description="The kind of functional role")
	name: Optional[HumanName] = Field(None, description="A name associated with the contact person")
	additionalName: list[Optional[HumanName]] = Field(None, description="Additional names for the contact person")
	telecom: list[Optional[ContactPoint]] = Field(None, description="A contact detail for the person")
	address: Optional[Address] = Field(None, description="Address for the contact person")
	additionalAddress: list[Optional[Address]] = Field(None, description="Additional addresses for the contact person")
	gender: Optional[GenderCode] = Field(None, description="male | female | other | unknown")
	organization: Optional[str] = Field(None, description="Organization that is associated with the contact")
	period: Optional[Period] = Field(
		None, description="The period during which this contact person or "
		            "organization is valid to be contacted relating to this patient"
	)



