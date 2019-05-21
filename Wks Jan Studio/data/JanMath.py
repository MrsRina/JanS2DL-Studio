from JanPort import math

def Sync_Resolution(resolution, _resolution):
	try:
		if not resolution.get("Default Resolution") is (False):
			resolution.set("Width",     _resolution(0))
			resolution.set("Height",     _resolution(1))

		elif not resolution.get("Default Resolution") is (True):
			""" """
	except:
		raise
	return None

def Sync_Resolution_Pos(master):
	try:
		return (master.winfo_pointerx() - master.winfo_vrootx(),
				master.winfo_pointery() - master.winfo_vrooty())
	except:
		raise
	return None

def Sync_File(x):
	try:
		if x is 0:
			return "disabled"

		elif x is 1:
			return "disabled"

		elif x is 2:
			return "normal"

	except:
		raise
	return None

def Sync_File_As(x):
	try:
		if x is 0:
			return "disabled"

		elif x is 1:
			return "normal"

		elif x is 2:
			return "disabled"

	except:
		raise
	return None