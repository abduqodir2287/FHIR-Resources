from fastapi import APIRouter, status

from src.domain.patient.patient_resource import Patient

patient_router = APIRouter(prefix="/Patient", tags=["Patients"])

@patient_router.post("", response_model=Patient, status_code=status.HTTP_201_CREATED)
async def add_patient(
		patient_info: Patient
) -> Patient:
	return patient_info

