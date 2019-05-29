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

class load_type(object):
	def __init__(self, project, type, tag, master, path, state):
		try:
			self.project    = project
			self.master     = master
			self.move       = False
			self.resize     = False
			self.rotate     = False
			self.rendering  = True
			self.selected   = False
			self.state      = state

			if self.project[1] is "load":
				self.type    = type
				self.path    = path
				self.tag     = tag
				self.img     = pygame.image.load(self.path)
				self.rect    = self.img.get_rect()

				self.do("load")

			elif self.project[1] is "project_load":
				self.do("project_load")
				
				self.type    = type
				self.path    = path
				self.tag     = tag
				self.img     = pygame.image.load(self.path)
				self.rect    = self.img.get_rect()
		except:
			raise
		return None

	def do(self, type):
		try:
			if type is "delete":
				self.do("delete_sprites_project")

				self.json_name = None
				self.path      = None
				self.img       = None
				self.rect      = None
				self.effect_   = None
				self.master    = None
				self.tag       = "deleted"

				self.move      = False
				self.resize    = False
				self.rotate    = False
				self.rendering = False
				self.selected  = False
				self.state     = None

			elif type is "auto_cache_save":
				if self.project[0] is None:
					""" No project """

				else:
					try:
						self.project[0].json[self.json_class][self.json_name]
					except:
						self.project[0].json[self.json_class][self.json_name] = {}
						
					self.project[0].json[self.json_class][self.json_name]["Tag"]    = self.tag
					self.project[0].json[self.json_class][self.json_name]["Type"]   = self.type
					self.project[0].json[self.json_class][self.json_name]["Width"]  = self.rect.w
					self.project[0].json[self.json_class][self.json_name]["Height"] = self.rect.h
					self.project[0].json[self.json_class][self.json_name]["X"]      = self.rect.x
					self.project[0].json[self.json_class][self.json_name]["Y"]      = self.rect.y
					self.project[0].json[self.json_class][self.json_name]["Path"]   = self.path

			elif type is "project_load":
				if self.project[0] is None:
					""" No project """

				else:
					try:
						self.project[0].json[self.json_class][self.json_name]
					except:
						self.project[0].json[self.json_class][self.json_name] = {}
	
					self.json_name = "Class {} {}".format(
						self.project[0].json[self.json_class][self.json_name]["Type"],
						self.project[0].json[self.json_class][self.json_name]["Tag"]
					)
	
					self.json_class = "Game {}".format(self.project[0].json["Game Sprites"][self.json_name]["Type"])
	
					self.tag    = self.project[0].json[self.json_class][self.json_name]["Tag"]
					self.type   = self.project[0].json[self.json_class][self.json_name]["Type"]
					self.rect.w = self.project[0].json[self.json_class][self.json_name]["Width"]
					self.rect.h = self.project[0].json[self.json_class][self.json_name]["Height"]
					self.rect.x = self.project[0].json[self.json_class][self.json_name]["X"]
					self.rect.y = self.project[0].json[self.json_class][self.json_name]["Y"]
					self.path   = self.project[0].json[self.json_class][self.json_name]["Path"]

			elif type is "load":
				self.json_name  = "Class {} {}".format(self.type, self.tag)
				self.json_class = "Game {}".format(self.type)

				if self.project[0] is None:
					""" No project """

				else:
					try:
						self.project[0].json[self.json_class][self.json_name]
					except:
						self.project[0].json[self.json_class][self.json_name] = {}

					self.project[0].json[self.json_class][self.json_name]["Tag"]    = self.tag
					self.project[0].json[self.json_class][self.json_name]["Type"]   = self.type
					self.project[0].json[self.json_class][self.json_name]["Width"]  = self.rect.w
					self.project[0].json[self.json_class][self.json_name]["Height"] = self.rect.h
					self.project[0].json[self.json_class][self.json_name]["X"]      = self.rect.x
					self.project[0].json[self.json_class][self.json_name]["Y"]      = self.rect.y
					self.project[0].json[self.json_class][self.json_name]["Path"]   = self.path

			elif type is "delete_sprites_project":
				if self.project[0] is None:
					""" No project """

				else:
					del self.project[0].json[self.json_class][self.json_name]["Tag"]
					del self.project[0].json[self.json_class][self.json_name]["Type"]
					del self.project[0].json[self.json_class][self.json_name]["Width"]
					del self.project[0].json[self.json_class][self.json_name]["Height"]
					del self.project[0].json[self.json_class][self.json_name]["X"]
					del self.project[0].json[self.json_class][self.json_name]["Y"]
					del self.project[0].json[self.json_class][self.json_name]["Path"]

					del self.project[0].json[self.json_class][self.json_name]
		except:
			raise
		return None

	def render(self):
		try:
			if self.rendering:
				self.master.blit(self.img, (self.rect.x, self.rect.y))

				if self.selected:
					if self.move:
						self.rect.x, self.rect.y = pygame.mouse.get_pos()

						if self.state.event_file is 0:
							self.state.event_file = 1

						elif self.state.event_file is 2:
							self.state.event_file = 3

					if self.rotate:
						pass

					if self.resize:
						self.rect.w, self.rect.h = pygame.mouse.get_pos()
						
						self.img = pygame.transform.scale(pygame.image.load(self.path), (self.rect.w, self.rect.h))

						if self.state.event_file is 0:
							self.state.event_file = 1

						elif self.state.event_file is 2:
							self.state.event_file = 3

						pygame.display.flip()

					self.do("auto_cache_save")

					self.effect_ = pygame.Surface((self.rect.w, self.rect.h), pygame.SRCALPHA)
					self.effect_.fill((255, 0, 0, 50))

					self.master.blit(self.effect_, self.rect)
		except:
			raise
		return None