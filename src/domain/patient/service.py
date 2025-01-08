from fastapi import HTTPException, status

from src.configs.logger_setup import logger
from src.domain.patient.schemas.time_resources.birthDate import Date
from src.infrastructure.database.mongodb.patient.client import PatientDB
from src.domain.patient.patient_resource import Patient
from src.domain.patient.schema import PatientResponseForPost

class PatientRouterService:

	def __init__(self) -> None:
		self.mongodb = PatientDB()


	async def get_all_patients_service(self) -> list[Patient]:
		all_patients = await self.mongodb.get_all_patients()
		logger.info("Patients List sent Successfully")

		return all_patients


	async def add_patient_service(self, patient: Patient) -> PatientResponseForPost:
		patient_id = await self.mongodb.insert_patient(patient)
		logger.info("Patient added Successfully")

		return PatientResponseForPost(PatientId=patient_id)


	async def delete_patient_service(self, firstname: str, lastname: str, birthDate: str) -> None:
		result = await self.mongodb.delete_patient(firstname, lastname, Date(date=birthDate))

		if result:
			logger.info("Patient deleted Successfully")

			return None

		raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Patient not found")



