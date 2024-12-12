from pydantic import BaseModel, Field, PositiveInt, AnyUrl, conint, condecimal
from typing import Optional

from src.domain.patient.schemas.photo_attachment.enums import MimeType, LanguageEnum
from src.domain.patient.schemas.time_resources.birthDate import Date
from src.domain.patient.schemas.photo_attachment.data_encoding_validate import DataModel


class Attachment(BaseModel):
	contentType: Optional[MimeType] = Field(None, description="Mime type of the content, with charset etc.")
	language: Optional[LanguageEnum] = Field(None, description="Human language")
	data: Optional[DataModel] = Field(None, description="Data inline, base64ed")
	url: Optional[AnyUrl] = Field(None, description="Uri where the data can be found")
	size: conint(ge=-9223372036854775808, le=9223372036854775807) = Field(
		None, description="Number of bytes of content (if url provided)")
	hash: Optional[DataModel] = Field(None, description="Hash of the data (sha-1, base64ed)")
	title: Optional[str] = Field(None, description="Label to display in place of the data")
	creation: Optional[Date] = Field(None, description="Date attachment was first created")
	height: Optional[PositiveInt] = Field(None, description="Height of the image in pixels (photo/video)")
	width: Optional[PositiveInt] = Field(None, description="Width of the image in pixels (photo/video)")
	frames: Optional[PositiveInt] = Field(None, description="Number of frames if > 1 (photo)")
	duration: condecimal(max_digits=18, decimal_places=17) = Field(None, description="Length in seconds (audio / video)")
	pages: Optional[PositiveInt] = Field(None, description="Number of printed pages")


