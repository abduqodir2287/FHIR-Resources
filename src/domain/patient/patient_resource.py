from typing import Optional
from pydantic import BaseModel, Field

from src.domain.patient.schemas.address.Address import Address
from src.domain.patient.schemas.contact_resources.contact import Contact
from src.domain.patient.schemas.contact_resources.contact_point import ContactPoint
from src.domain.patient.schemas.HumanName import HumanName
from src.domain.patient.schemas.identifier.codable_concept import CodableConcept
from src.domain.patient.schemas.link import Link
from src.domain.patient.schemas.photo_attachment.attachment import Attachment
from src.domain.patient.schemas.identifier.identifier import Identifier
from src.domain.patient.schemas.reference import Reference
from src.domain.patient.schemas.time_resources.birthDate import Date
from src.domain.patient.enums import GenderCode
from src.domain.patient.schemas.deceased import Deceased
from src.domain.patient.schemas.multipleBirth import MultipleBirth
from src.domain.patient.schemas.communication import Communication


class Patient(BaseModel):
	identifier: list[Optional[Identifier]] = Field(None, description="An identifier for this patient")
	active: Optional[bool] = Field(None, description="Whether this patient's record is in active use")
	name: Optional[HumanName] = Field(None, description="A name associated with the patient")
	telecom: list[Optional[ContactPoint]] = Field(None, description="A contact detail for the individual")
	gender: Optional[GenderCode] = Field(None, description="male | female | other | unknown")
	birthDate: Optional[Date] = Field(None, description="The date of birth for the individual")
	deceased: Optional[Deceased] = Field(
		None, description="Indicates if/when the individual is deceased. (One of these 2:)")
	address: list[Optional[Address]] = Field(None, description="An address for the individual")
	maritalStatus: Optional[CodableConcept] = Field(None, description="Marital (civil) status of a patient")
	multipleBirth: Optional[MultipleBirth] = Field(
		None, description="Whether patient is part of a multiple birth. One of these 2:")
	photo: list[Optional[Attachment]] = Field(None, description="Image of the patient")
	contact: list[Optional[Contact]] = Field(
		None, description="A contact party (e.g. guardian, partner, friend) for the patient")
	communication: list[Communication] = Field(
		..., description="A language which may be used to communicate with the patient about his or her health")
	generalPractitioner: list[Optional[Reference]] = Field(None, description="Patient's nominated primary care provider")
	managingOrganization: Optional[str] = Field(
		None, description="Organization that is the custodian of the patient record")
	link: Link = Field(
		..., description="Link to a Patient or RelatedPerson resource that concerns the same actual individual")


