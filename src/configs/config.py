from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
	LOG_LEVEL: str
	LOG_FORMAT: str
	LOG_FILE: str
	LOG_BACKUP_COUNT: int
	LOG_WRITE_STATUS: bool


	model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

