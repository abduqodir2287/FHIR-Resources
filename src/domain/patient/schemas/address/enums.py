from enum import Enum

class AddressUse(str, Enum):
	home = "home"
	work = "work"
	temp = "temp"
	old = "old"
	billing = "billing"


class AddressType(str, Enum):
	postal = "postal"
	physical = "physical"
	both = "both"

