from fastapi import APIRouter, status, Query

from src.domain.patient.patient_resource import Patient
from src.domain.patient.service import PatientRouterService
from src.domain.patient.schema import PatientResponseForPost


patient_router = APIRouter(prefix="/Patient", tags=["Patients"])

patient_service = PatientRouterService()


@patient_router.get("", response_model=list[Patient], status_code=status.HTTP_200_OK)
async def get_all_patients() -> list[Patient]:
	return await patient_service.get_all_patients_service()


@patient_router.post("", response_model=PatientResponseForPost, status_code=status.HTTP_201_CREATED)
async def add_patient(patient_info: Patient) -> PatientResponseForPost:
	return await patient_service.add_patient_service(patient_info)


@patient_router.delete("", status_code=status.HTTP_204_NO_CONTENT)
async def delete_patient(
		firstname: str = Query(..., description="Text representation of the full name"),
		lastname: str = Query(..., description="Family name (often called 'Surname')"),
		birthDate: str = Query(..., description="The person's date of birth in the format 'YYYY', 'YYYY-MM' or 'YYYY-MM-DD'.")
) -> None:
	await patient_service.delete_patient_service(firstname, lastname, birthDate)

