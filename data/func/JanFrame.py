from tkinter import *
import tkinter as tk

class _frame(object):
	def __init__(self, master, width=None, height=None, bg=None, borde=None, resize_with=None):
		try:
			self._resize_frame = tk.Frame(master.get_master(), width=width, height=height, bg=borde)
			self._master_frame = tk.Frame(master.get_master(), width=width, height=height, bg=bg)

			self._resize_frame.bind("<Button-1>", self._resize_frame)

			self._resize_frame.pack()
			self._master_frame.pack()
			
			if resize_with is None:
				resize_with = None
		except:
			raise
		return None

	def _resize_frame(self, x, y):
		try:
			self._resize_frame.configure(width=event.x, height=event.y)
			self._master_frame.configure(width=event.x, height=event.y)
			self.resize_with.display.set_mode((event.x, event.y), self.resize_with.DOUBLEBUF)
		except:
			raise
		return None

	def get_id(self):
		try:
			return self._master_frame
		except:
			raise
		return None
