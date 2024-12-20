from src.infrastructure.database.mongodb.patient.client import PatientDB
from src.domain.patient.patient_resource import Patient
from src.domain.patient.schema import PatientResponseForPost

class PatientRouterService:

	def __init__(self) -> None:
		self.mongodb = PatientDB()


	async def get_all_patients_service(self) -> list[Patient]:
		all_patients = await self.mongodb.get_all_patients()

		return all_patients


	async def add_patient_service(self, patient: Patient) -> PatientResponseForPost:
		patient_id = await self.mongodb.insert_patient(patient)

		return PatientResponseForPost(PatientId=patient_id)
