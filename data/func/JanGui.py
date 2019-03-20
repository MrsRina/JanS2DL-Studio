from tkinter import messagebox
import tkinter as tk

class create_window(object):
	def __init__(self, geometry, title, color):
		try:
			self.Window = tk.Tk()
			self.Window.geometry(geometry)
			self.Window.title(title)
			self.Window.configure(background = color)
		except:
			raise
		return None

	def askExit(self, msg):
		try:
			return messagebox.askokcancel("Quit", msg)
		except:
			raise
		return None

	def get_master(self):
		try:
			return self.Window
		except:
			raise
		return None

	def close(self):
		try:
			return self.Window.destroy()
		except:
			raise
		return None