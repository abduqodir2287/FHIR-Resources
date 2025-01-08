from fastapi import FastAPI, status

from src.domain.patient.schema import FirstPageResponse
from src.presentation.rest.routers import all_routers


app = FastAPI()

for router in all_routers:
	app.include_router(router)


@app.get("/", response_model=FirstPageResponse, status_code=status.HTTP_200_OK)
async def hello() -> FirstPageResponse:
	return FirstPageResponse(Message="Hello, World")

