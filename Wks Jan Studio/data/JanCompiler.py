class load_projetc(object):
	def __init__(self, path):
		try:
			self.title_project = None
			self.sprites       = None
			self.objects       = None
			self.cameras       = None

			self.file = open(path, "r+")

			self.read_and_get()
		except:
			raise
		return None

	def add_(self, type, what):
		try:
			if type is "title":
				for file in self.file:
					_find = line.strip().split()

					if _find[0]:
						cache_what = _find[0].replace(_find, what)
						file.write(cache_what)

					file.close()
		except:
			raise
		return None

	def read_and_get(self):
		try:
			for file in self.file:
				_find = line.strip().split()

				self.title_project = _find[0]
				self.sprites       = _find[1]
				self.objects       = _find[2]

				file.close()
		except:
			raise
		return None