from pydantic import BaseModel

class PatientResponseForPost(BaseModel):
	PatientId: str


class FirstPageResponse(BaseModel):
	Message: str

