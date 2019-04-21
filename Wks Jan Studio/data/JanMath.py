from JanPort import math

def Sync_Resolution(resolution, _resolution):
	try:
		if not resolution.get("Default Resolution") is (False):
			if not resolution.get("Width") is (_resolution(0)):
				   resolution.set("Width",     _resolution(0))

			if not resolution.get("Height") is (_resolution(1)):
				   resolution.set("Height",     _resolution(1))

		elif not resolution.get("Default Resolution") is (True):
			""" """
	except:
		raise
	return None