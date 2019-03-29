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
			self.master_menu = tk.Menu(master, tearoff = 0)

			# Add:
			master.configure(menu=self.master_menu)
		except:
			raise
		return None

	def create_file_menu(self, json_value, command_Open_FILE, command_Save_FILE, command_Save_As_File, command_File_Exit):
		try:
			self.menu_file = tk.Menu(self.master_menu, tearoff = 0, bg = "Gray", fg = "White")
			self.menu_file.add_command(label = json_value.get("Menu_Open_File"),	 commad = command_Open_FILE)
			self.menu_file.add_command(label = json_value.get("Menu_Save_File"),	 commad = command_Save_FILE)
			self.menu_file.add_command(label = json_value.get("Menu_Save_File_As"),  commad = command_Save_As_File)
			self.menu_file.add_command(label = json_value.get("Menu_File_Exit"), 	 commad = command_File_Exit)

			self.master_menu.add_cascade(label = json_value.get("Menu_File"), menu = self.menu_file)	
		except:
			raise
		return None

	def create_tools_menu(self, json_value, command_Tool_SPRITE, command_Tool_OBJECTS, command_Tool_EFFECTS, command_Tool_TEXT, command_tool_BACKGROUND):
		try:
			self.menu_tools = tk.Menu(self.master_menu, tearoff = 0, bg = "Gray", fg = "White")
			self.menu_tools.add_command(label = json_value.get("Menu_Tool_Sprite"), 	command=command_Tool_SPRITE)
			self.menu_tools.add_command(label = json_value.get("Menu_Tool_Objects"), command=command_Tool_OBJECTS)
			self.menu_tools.add_command(label = json_value.get("Menu_Tool_Effects"), command=command_Tool_EFFECTS)
			self.menu_tools.add_command(label = json_value.get("Menu_Tool_Text"), 	command=command_Tool_TEXT)
			self.menu_tools.add_separator()
			self.menu_tools.add_command(label = json_value.get("Menu_Tool_Background"), command=command_tool_BACKGROUND)

			self.master_menu.add_cascade(label = json_value.get("Menu_Tools"), menu = self.menu_tools)
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