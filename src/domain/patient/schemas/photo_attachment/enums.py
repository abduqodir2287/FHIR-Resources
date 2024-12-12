from enum import Enum

class MimeType(str, Enum):
	json = "application/json"
	text = "text/plain"
	image = "image/png"


class LanguageEnum(str, Enum):
	ru = "ru"
	uz = "uz"
	en = "en"

