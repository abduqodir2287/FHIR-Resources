from fastapi import APIRouter, status

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


