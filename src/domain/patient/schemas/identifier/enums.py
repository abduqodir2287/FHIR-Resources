from enum import Enum


class IdentifierCode(str, Enum):
	usual = "usual"
	official = "official"
	temp = "temp"
	secondary = "secondary"
	old = "old"

