from motor.motor_asyncio import AsyncIOMotorClient
from fastapi.encoders import jsonable_encoder

from src.configs.config import settings
from src.domain.patient.patient_resource import Patient
from src.domain.patient.schemas.time_resources.birthDate import Date

class PatientDB:

	def __init__(self) -> None:
		self.client = AsyncIOMotorClient(settings.MONGO_CLIENT)
		self.db = self.client[settings.MONGO_DB_NAME]
		self.collection = self.db["Patients"]


	async def get_all_patients(self) -> list[Patient]:
		patients_list = []

		async for patient in self.collection.find():
			patients_list.append(patient)

		return patients_list


	async def insert_patient(self, patient: Patient) -> str:
		patient_info = jsonable_encoder(patient)

		insert = await self.collection.insert_one(patient_info)

		return str(insert.inserted_id)


	async def delete_patient(self, firstname: str, lastname: str, birthDate: Date) -> bool:

		patient = await self.collection.find_one({"name.text": firstname, "name.family": lastname,
		                                          "birthDate": jsonable_encoder(birthDate)})

		if patient:
			await self.collection.delete_one({"_id": patient["_id"]})

			return True

		return False






