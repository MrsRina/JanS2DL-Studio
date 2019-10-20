from JanPort import math

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
			return "disabled"

		elif x is 3:
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

		elif x is 3:
			return "disabled"
	except:
		raise
	return None