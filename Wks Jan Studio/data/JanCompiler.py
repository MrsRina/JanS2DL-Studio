import json

class create_project(object):
		def __init__(self, local = None, name = None):
			try:
				self.local = local + "/{}.jan".format(name.replace(" ", "_"))
				file       = open(self.local, "w")
				file.write("{")
				file.write('\n    "Name" : "{}"'.format(name))
				file.write("\n}")
				file.close()

				self.path = open(self.local, "r+")
				self.json = json.load(self.path)

				self.json["Name"] = name

				self.save()
			except:
				raise
			return None

		def save(self):
			try:
				self.path.seek(0)
				json.dump(self.json, self.path, indent = 4)
				self.path.truncate()
			except:
				raise
			return None

class open_project(object):
	def __init__(self, path = None):
		try:
			self.local = path
			self.path  = open(self.local, "r+")
			self.json  = json.load(self.path)
		except:
			raise
		return None

	def add_sprite(self, sprite = None):
		try:
			self.json[sprite] = sprite
			self.save()
		except:
			raise
		return None

	def add_object(self, _object = None):
		try:
			self.json[_object] = _object
			self.save()
		except:
			raise
		return None

	def add_camera(self, camera = None):
		try:
			self.json[camera] = camera
			self.save()
		except:
			raise
		return None

	def remove(self, sprite):
		try:
			if sprite is "Class Sprite":
				del self.json[sprite]

			elif sprite is "Calss Object":
				del self.json[object]
		except:
			raise
		return None

	def save(self):
		try:
			self.path.seek(0)
			json.dump(self.json, self.path, indent = 4)
			self.path.truncate()
		except:
			raise
		return None