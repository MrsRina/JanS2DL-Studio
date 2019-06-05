import json

class create_project(object):
		def __init__(self, local = None, name = None, comments = None):
			try:
				self.local = local + "/{}.jan".format(name.replace(" ", "_"))
				file       = open(self.local, "w")
				file.write("{")
				file.write('\n    "Name" : "{}"'.format(name))
				file.write("\n}")
				file.close()

				self.path = open(self.local, "r+")
				self.json = json.load(self.path)

				self.json["Name"]          = name
				self.json["Game Sprites"]  = {}
				self.json["Game Objects"]  = {}
				self.json["Game Cameras"]  = {}
				self.json["Game Comments"] = comments

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

	def save(self):
		try:
			self.path.seek(0)
			json.dump(self.json, self.path, indent = 4)
			self.path.truncate()
		except:
			raise
		return None
