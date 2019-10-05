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

JAN_ENGINE_engine = load(replace_folder("data/_JanJa.py", "JanConfig.json"))

class load_type(object): 
	def __init__(self, project = None, type = None, tag = None, master = None, path = None, state = None, cam_x = None, cam_y = 0, camera = None):
		try:
			import base64
			import io

			self.project   = project
			self.master    = master
			self.move      = False
			self.resize    = False
			self.rotate    = False
			self.rendering = True
			self.selected  = False
			self.state     = state
			self.base64    = base64
			self.cam_x     = cam_x
			self.cam_y     = cam_y
			self.x         = 0
			self.y         = 0
			self.w         = 0
			self.h         = 0
			self.camera    = camera

			if self.project[1] is "load":
				self.path      = path
				self.img_data  = self.base64.b64encode(open(self.path, "rb").read()).decode("utf-8")
				self.img_path  = io.BytesIO(base64.b64decode(self.img_data))
				self.type      = type
				self.tag       = tag
				self.extension = os.path.splitext(os.path.basename(self.path))[1]
				self.img       = pygame.image.load(self.img_path)
				self.x         = self.img.get_rect().x
				self.y         = self.img.get_rect().y
				self.w         = self.img.get_rect().w
				self.h         = self.img.get_rect().h
				self.camera    = camera

				self.do("load")

			elif self.project[1] is "project_load":
				self.tag        = tag
				self.type       = type
				self.json_name  = "Class {} {}".format(self.type, self.tag)
				self.json_class = "Game {}".format(self.type)

				self.do("project_load")

				self.img_path = io.BytesIO(base64.b64decode(self.img_data))
				self.img      = pygame.transform.scale(pygame.image.load(self.img_path), 
				(self.project[0].json[self.json_class][self.json_name]["Width"], self.project[0].json[self.json_class][self.json_name]["Height"]))
				
				self.x = self.project[0].json[self.json_class][self.json_name]["X"]
				self.y = self.project[0].json[self.json_class][self.json_name]["Y"]
				self.w = self.project[0].json[self.json_class][self.json_name]["Width"]
				self.h = self.project[0].json[self.json_class][self.json_name]["Height"]

				self.camera = self.project[0].json[self.json_class][self.json_name]["Camera"]
		except:
			raise
		return None

	def set_size(self, width = None, height = None):
		try:
			import base64
			import io

			self.w = self.w if width is None else width
			self.h = self.h if height is None else height

			self.img = pygame.transform.scale(pygame.image.load(io.BytesIO(base64.b64decode(self.img_data))), (self.w, self.h))

			if self.state.event_file is 0:
				self.state.event_file = 1

			elif self.state.event_file is 2:
				self.state.event_file = 3
		except:
			raise
		return None

	def do(self, type, project = None, change = None):
		try:
			if type is "delete":
				self.project = [project]
				self.do("delete_sprites_project", self.project)

				self.json_name = None

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
					self.project[0].json[self.json_class][self.json_name]["Camera"] = self.camera
					self.project[0].json[self.json_class][self.json_name]["Ext"]    = self.extension
					self.project[0].json[self.json_class][self.json_name]["Width"]  = self.w
					self.project[0].json[self.json_class][self.json_name]["Height"] = self.h
					self.project[0].json[self.json_class][self.json_name]["X"]      = self.x
					self.project[0].json[self.json_class][self.json_name]["Y"]      = self.y
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
				self.camera    = self.project[0].json[self.json_class][self.json_name]["Camera"]

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
					self.project[0].json[self.json_class][self.json_name]["Camera"] = self.camera
					self.project[0].json[self.json_class][self.json_name]["Ext"]    = self.extension
					self.project[0].json[self.json_class][self.json_name]["Width"]  = self.w
					self.project[0].json[self.json_class][self.json_name]["Height"] = self.h
					self.project[0].json[self.json_class][self.json_name]["X"]      = self.x
					self.project[0].json[self.json_class][self.json_name]["Y"]      = self.y
					self.project[0].json[self.json_class][self.json_name]["Path"]   = self.path
					self.project[0].json[self.json_class][self.json_name]["Data"]   = self.img_data

			elif type is "delete_sprites_project":
				if self.project[0] is None:
					""" No project """

				else: 
					del self.project[0].json[self.json_class][self.json_name]["Tag"]
					del self.project[0].json[self.json_class][self.json_name]["Type"]
					del self.project[0].json[self.json_class][self.json_name]["Camera"]
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
				self.project[0].json[self.json_class][self.json_name]["Camera"] = self.camera
				self.project[0].json[self.json_class][self.json_name]["Ext"]    = self.extension
				self.project[0].json[self.json_class][self.json_name]["Width"]  = self.w
				self.project[0].json[self.json_class][self.json_name]["Height"] = self.h
				self.project[0].json[self.json_class][self.json_name]["X"]      = self.x
				self.project[0].json[self.json_class][self.json_name]["Y"]      = self.y
				self.project[0].json[self.json_class][self.json_name]["Path"]   = self.path
				self.project[0].json[self.json_class][self.json_name]["Data"]   = self.img_data

			elif type is "replace":
				self.project    = [project]
				self.json_name  = "Class {} {}".format(self.type, self.tag)
				self.json_class = "Game {}".format(self.type)

				self.project[0].json[self.json_class][self.json_name] = self.project[0].json["Game {}".format(self.type)]["Class {} {}".format(self.type, change)]

				del self.project[0].json["Game {}".format(self.type)]["Class {} {}".format(self.type, change)]
		except:
			raise
		return None

	def render(self, cam_y, cam_x, camera):
		try:
			if self.camera:
				if self.rendering:
					self.cam_x = cam_y
					self.cam_y = cam_x
	
					try:
						self.rect = pygame.rect.Rect((self.x - self.cam_x, self.y - self.cam_y), (self.w, self.h))
					except:
						pass
	
					self.master.blit(self.img, self.rect)
	
					if self.selected:
						if self.move:
							self.rect.centerx = pygame.mouse.get_pos()[0] + self.cam_x
							self.rect.centery = pygame.mouse.get_pos()[1] + self.cam_y
	
							self.x = self.rect.x
							self.y = self.rect.y
	
							if self.state.event_file is 0:
								self.state.event_file = 1
	
							elif self.state.event_file is 2:
								self.state.event_file = 3
	
						if self.rotate:
							pass
	
						if self.resize:
							try:
								self.set_size(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
							except:
								raise
		
						self.do("auto_cache_save")
	
						self.effect_ = pygame.Surface((self.w, self.h), pygame.SRCALPHA)
						self.effect_.fill((255, 0, 0, 50))
	
						self.master.blit(self.effect_, (self.x - self.cam_x, self.y - self.cam_y))
		except:
			raise
		return None