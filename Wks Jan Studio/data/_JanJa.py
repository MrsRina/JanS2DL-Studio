from JanPort import (
os     ,
sys    ,
math   ,
ctypes ,

json)

hardware_dll = ctypes.windll.user32

# // define

hardware_res = hardware_dll.GetSystemMetrics

class load(object):
	def __init__(self, path):
		try:
			self.path = open(path, "r+")
			self.file = json.load(self.path)
		except:
			raise
		return None

	def set(self, item_json, write_json):
		try:
			self.file[item_json] = write_json
	
			self.path.seek(0)
			json.dump(self.file, self.path)
			self.path.truncate()
		except:
			raise
		return None

	def new(self, item_json, write_json):
		try:
			self.file[item_json] = write_json
	
			self.path.seek(0)
			json.dump(self.file, self.path, indent = 4)
			self.path.truncate()
		except:
			raise
		return None

	def rem(self, item_json):
		try:
			try:
				del self.file[item_json]
			except:
				pass
	
			self.path.seek(0)
			json.dump(self.file, self.path)
			self.path.truncate()
		except:
			raise
		return None

	def get(self, _value):
		try:
			return self.file[_value]
		except:
			raise
		return None

	def __repr__(self):
		try:
			return self.file
		except:
			raise
		return None

global JAN_ENGINE_path

def replace_folder(remove, place):
	try:
		cache      = os.path.realpath(__file__)
		cahce_path = cache.replace("\\", "/")
		
		path = cahce_path.replace(remove, place)
		
		return path
	except:
		raise
	return None

def replace(variable, to, new):
	try:
		cache_00 = variable.replace(to, new)

		return cache_00
	except:
		raise
	return None

JAN_ENGINE_engine = load(replace_folder("data/_JanJa.py", "JanConfig.json"))

from JanPort import JanMath
from JanPort import JanGui
from JanPort import pygame