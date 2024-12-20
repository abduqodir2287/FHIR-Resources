from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
	MONGO_CLIENT: str = None
	MONGO_DB_NAME: str = None
	LOG_LEVEL: str = None
	LOG_FORMAT: str = None
	LOG_FILE: str = None
	LOG_BACKUP_COUNT: int = None
	LOG_WRITE_STATUS: bool = None


	model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

