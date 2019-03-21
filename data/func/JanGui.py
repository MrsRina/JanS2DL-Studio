from tkinter import messagebox
import tkinter as tk

class create_window(object):
	def __init__(self, width, height, title, color):
		try:
			self.Window = tk.Tk()
			self.Window.geometry("{}x{}".format(width, height))
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

class create_menu(object):
	def __init__(self, master):
		try:
			self._master_menu = Menu(master, tearoff = 0)

			# Add:
			master.configure(Menu=self._master_menu)
		except:
			raise
		return None

	def create_file_menu(self, json_value, value):
		try:
			self._menu_file = Menu(self._master_menu, tearoff = 0)
			self._menu_file.add_command(label = json_value[""])			
		except:
			raise
		return None

class create_note(object):	
	def __init__(self):
		try:
			pass
		except:
			raise
		return None