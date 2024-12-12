from enum import Enum

class ContactSystemCode(str, Enum):
	phone = "phone"
	fax = "fax"
	email = "email"
	pager = "pager"
	url = "url"
	sms = "sms"
	other = "other"


class ContactUseCode(str, Enum):
	home = "home"
	work = "work"
	temp = "temp"
	old = "old"
	mobile = "mobile"

