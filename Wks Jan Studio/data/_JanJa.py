from JanPort import *

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

import _thread

start_thread = lambda x: _thread.start_new_thread(x, None)

JAN_ENGINE_engine = load(replace_folder("data/_JanJa.py", "JanConfig.json"))

class load_type(object): 
	def __init__(self, project = None, type = None, tag = None, master = None, path = None, state = None):
		try:
			import base64
			import io

			self.project    = project
			self.master     = master
			self.move       = False
			self.resize     = False
			self.rotate     = False
			self.rendering  = True
			self.selected   = False
			self.state      = state
			self.base64     = base64

			if self.project[1] is "load":
				self.path      = path
				self.img_data  = self.base64.b64encode(open(self.path, "rb").read()).decode("utf-8")
				self.img_path  = io.BytesIO(base64.b64decode(self.img_data))
				self.type      = type
				self.tag       = tag
				self.extension = os.path .splitext(os.path.basename(self.path))[1]
				self.img       = pygame.image.load(self.img_path)
				self.rect      = self.img.get_rect()

				self.do("load")

			elif self.project[1] is "project_load":
				self.tag        = tag
				self.type       = type
				self.json_name  = "Class {} {}".format(self.type, self.tag)
				self.json_class = "Game {}".format(self.type)

				self.do("project_load")

				self.img_path = io.BytesIO(base64.b64decode(self.img_data))
				self.img      = self.img = pygame.transform.scale(pygame.image.load(self.path), 
				(self.project[0].json[self.json_class][self.json_name]["Width"], self.project[0].json[self.json_class][self.json_name]["Height"]))
				
				self.rect   = self.img.get_rect()
				self.rect.w = self.project[0].json[self.json_class][self.json_name]["Width"]
				self.rect.h = self.project[0].json[self.json_class][self.json_name]["Height"]
				self.rect.x = self.project[0].json[self.json_class][self.json_name]["X"]
				self.rect.y = self.project[0].json[self.json_class][self.json_name]["Y"]
		except:
			raise
		return None

	def do(self, type, project = None):
		try:
			if type is "delete":
				self.do("delete_sprites_project")

				self.json_name = None
				self.path      = None
				self.img       = None
				self.rect      = None
				self.effect_   = None
				self.master    = None
				self.img_data  = None
				self.extension = None
				self.img_path  = None
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
					self.project[0].json[self.json_class][self.json_name]["Ext"]    = self.extension
					self.project[0].json[self.json_class][self.json_name]["Width"]  = self.rect.w
					self.project[0].json[self.json_class][self.json_name]["Height"] = self.rect.h
					self.project[0].json[self.json_class][self.json_name]["X"]      = self.rect.x
					self.project[0].json[self.json_class][self.json_name]["Y"]      = self.rect.y
					self.project[0].json[self.json_class][self.json_name]["Path"]   = self.path
					self.project[0].json[self.json_class][self.json_name]["Data"]   = self.img_data

			elif type is "project_load":
				try:
					self.project[0].json[self.json_class][self.json_name]
				except:
					self.project[0].json[self.json_class][self.json_name] = {}

				self.tag       = self.project[0].json[self.json_class][self.json_name]["Tag"]
				self.type      = self.project[0].json[self.json_class][self.json_name]["Type"]
				self.extension = self.project[0].json[self.json_class][self.json_name]["Ext"]
				self.path      = self.project[0].json[self.json_class][self.json_name]["Path"]
				self.img_data  = self.project[0].json[self.json_class][self.json_name]["Data"]

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
					self.project[0].json[self.json_class][self.json_name]["Ext"]    = self.extension
					self.project[0].json[self.json_class][self.json_name]["Width"]  = self.rect.w
					self.project[0].json[self.json_class][self.json_name]["Height"] = self.rect.h
					self.project[0].json[self.json_class][self.json_name]["X"]      = self.rect.x
					self.project[0].json[self.json_class][self.json_name]["Y"]      = self.rect.y
					self.project[0].json[self.json_class][self.json_name]["Path"]   = self.path
					self.project[0].json[self.json_class][self.json_name]["Data"]   = self.img_data

			elif type is "delete_sprites_project":
				if self.project[0] is None:
					""" No project """

				else: 
					del self.project[0].json[self.json_class][self.json_name]["Tag"]
					del self.project[0].json[self.json_class][self.json_name]["Type"]
					del self.project[0].json[self.json_class][self.json_name]["Ext"]
					del self.project[0].json[self.json_class][self.json_name]["Width"]
					del self.project[0].json[self.json_class][self.json_name]["Height"]
					del self.project[0].json[self.json_class][self.json_name]["X"]
					del self.project[0].json[self.json_class][self.json_name]["Y"]
					del self.project[0].json[self.json_class][self.json_name]["Path"]
					del self.project[0].json[self.json_class][self.json_name]["Data"]

					del self.project[0].json[self.json_class][self.json_name]

			elif type is "save":
				self.project    = [project]
				self.json_name  = "Class {} {}".format(self.type, self.tag)
				self.json_class = "Game {}".format(self.type)
					 
				try:
					self.project[0].json[self.json_class][self.json_name]
				except:
					self.project[0].json[self.json_class][self.json_name] = {}

				self.project[0].json[self.json_class][self.json_name]["Tag"]    = self.tag
				self.project[0].json[self.json_class][self.json_name]["Type"]   = self.type
				self.project[0].json[self.json_class][self.json_name]["Ext"]    = self.extension
				self.project[0].json[self.json_class][self.json_name]["Width"]  = self.rect.w
				self.project[0].json[self.json_class][self.json_name]["Height"] = self.rect.h
				self.project[0].json[self.json_class][self.json_name]["X"]      = self.rect.x
				self.project[0].json[self.json_class][self.json_name]["Y"]      = self.rect.y
				self.project[0].json[self.json_class][self.json_name]["Path"]   = self.path
				self.project[0].json[self.json_class][self.json_name]["Data"]   = self.img_data
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