from pydantic import BaseModel

class PatientResponseForPost(BaseModel):
	PatientId: str

