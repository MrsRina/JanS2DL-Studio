from tkinter import *
import tkinter as tk

class _button(object):

	def __init__(self, master, width=None, height=None, fg=None, bg=None, font=None, text=None, res=None, command=None):
		try:
			self._master_button = tk.Button(master, width=width, height=height, fg=fg, bg=bg,
											font=font, text=text, command=command)
			self.x, self.y = res

			self._master_button.place(x=self.x, y=self.y)			
		except:
			raise
		return None