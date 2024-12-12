from enum import Enum


class HumanNameCode(str, Enum):
	usual = "usual"
	official = "official"
	temp = "temp"
	nickname = "nickname"
	anonymous = "anonymous"
	old = "old"
	maiden = "maiden"


class GenderCode(str, Enum):
	male = "male"
	female = "female"
	other = "other"
	unknown = "unknown"


class LinkTypeCode(str, Enum):
	replaced_by = "replaced_by"
	replaces = "replaces"
	refer = "refer"
	seealso = "seealso"


