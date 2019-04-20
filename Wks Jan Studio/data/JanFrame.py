from JanPort import tk

class _frame(object):
	def __init__(self, master, width = None, height = None, bg = None, borde = None, resize_with = None):
		try:
			self.width = width; self.height = height

			self.resize_canvas_width  = tk.Canvas (master.get_master(), width = width, height = height, bg = borde)
			self.resize_canvas_height = tk.Canvas (master.get_master(), width = width, height = height, bg = borde)
			self.master_frame         = tk.Frame  (master.get_master(), width = width, height = height, bg = bg)

			self.resize_canvas_width .bind("<B1-Motion>", self.resize_frame_width)
			self.resize_canvas_height.bind("<B1-Motion>", self.resize_frame_height)

			self.resize_canvas_width .place(x = 1, y = 0)
			self.resize_canvas_height.place(x = 0, y = 1)
			
			self.master_frame.place(x = 0, y = 0)
			
			self.resize_with = resize_with
			self.master      = master
		except:
			raise
		return None

	def resize_frame_width(self, event):
		try:
			self.width = event.x
			
			self.resize_canvas_width .configure(width = self.width, height = self.height)
			self.resize_canvas_height.configure(width = self.width, height = self.height)			
			self.master_frame        .configure(width = self.width, height = self.height)

			if not self.resize_with is None:
				self.resize_with.display.set_mode((self.width, self.height), self.resize_with.DOUBLEBUF)
		except:
			raise
		return None

	def resize_frame_height(self, event):
		try:
			self.height = event.y			
			
			self.resize_canvas_width .configure(width = self.width, height = self.height)
			self.resize_canvas_height.configure(width = self.width, height = self.height)
			self.master_frame        .configure(width = self.width, height = self.height)
			
			if not self.resize_with is None:
				self.resize_with.display.set_mode((self.width, self.height), self.resize_with.DOUBLEBUF)
		except:
			raise
		return None

	def get_id(self):
		try:
			return self.master_frame
		except:
			raise
		return None