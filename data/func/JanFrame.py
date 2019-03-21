from tkinter import *
import tkinter as tk

class _frame(object):
	def __init__(self, master, width=None, height=None, bg=None, borde=None, resize_with=None):
		try:
			self.width = width; self.height = height

			self._resize_canvas_width  = tk.Canvas(master.get_master(), width=width, height=height, bg=borde)
			self._resize_canvas_height = tk.Canvas(master.get_master(), width=width, height=height, bg=borde)
			self._master_frame         = tk.Frame(master.get_master(), width=width, height=height, bg=bg)

			self._resize_canvas_width.bind("<B1-Motion>", self._resize_frame_width)
			self._resize_canvas_height.bind("<B1-Motion>", self._resize_frame_height)

			self._resize_canvas_width.place(x=1, y=0)
			self._resize_canvas_height.place(x=0, y=1)
			self._master_frame.place(x=0, y=0)
			
			self.resize_with = resize_with
			self.master      = master
		except:
			raise
		return None

	def _resize_frame_width(self, event):
		try:
			self.width=event.x
			self._resize_canvas_width.configure(width=self.width, height=self.height)
			self._resize_canvas_height.configure(width=self.width, height=self.height)
			self._master_frame.configure(width=self.width, height=self.height)
			self.resize_with.display.set_mode((self.width, self.height), self.resize_with.DOUBLEBUF)
		except:
			raise
		return None

	def _resize_frame_height(self, event):
		try:
			self.height=event.y			
			self._resize_canvas_width.configure(width=self.width, height=self.height)
			self._resize_canvas_height.configure(width=self.width, height=self.height)
			self._master_frame.configure(width=self.width, height=self.height)
			self.resize_with.display.set_mode((self.width, self.height), self.resize_with.DOUBLEBUF)
		except:
			raise
		return None

	def get_id(self):
		try:
			return self._master_frame
		except:
			raise
		return None

class frame(object):
	def __init__(self, master, width=None, height=None, bg=None, borde=None):
		try:
			self.width = width; self.height = height

			self._resize_canvas_width  = tk.Canvas(master.get_master(), width=width, height=height, bg=borde)
			self._resize_canvas_height = tk.Canvas(master.get_master(), width=width, height=height, bg=borde)
			self._master_frame         = tk.Frame(master.get_master(), width=width, height=height, bg=bg)

			self._resize_canvas_width.bind("<B1-Motion>", self._resize_frame_width)
			self._resize_canvas_height.bind("<B1-Motion>", self._resize_frame_height)

			self._resize_canvas_width.place(x=1, y=0)
			self._resize_canvas_height.place(x=0, y=1)
			self._master_frame.place(x=0, y=0)
			
			self.master      = master
		except:
			raise
		return None

	def _resize_frame_width(self, event):
		try:
			self.width=event.x
			self._resize_canvas_width.configure(width=self.width, height=self.height)
			self._resize_canvas_height.configure(width=self.width, height=self.height)
			self._master_frame.configure(width=self.width, height=self.height)
		except:
			raise
		return None

	def _resize_frame_height(self, event):
		try:
			self.height=event.y			
			self._resize_canvas_width.configure(width=self.width, height=self.height)
			self._resize_canvas_height.configure(width=self.width, height=self.height)
			self._master_frame.configure(width=self.width, height=self.height)
		except:
			raise
		return None

	def get_id(self):
		try:
			return self._master_frame
		except:
			raise
		return None
