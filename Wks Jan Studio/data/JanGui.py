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
			master.configure(menu = self.master_menu)
		except:
			raise
		return None

	def create_file_menu(self, command_Open_File, command_Save_File, command_Save_As_File, command_File_Exit):
		try:
			self.menu_file = tk.Menu(self.master_menu, tearoff = 0, bg = "Gray", fg = "White")

			self.menu_file.add_command(label = "Open File",	   commad = command_Open_File	 )
			self.menu_file.add_command(label = "Save File",	   commad = command_Save_File    )
			self.menu_file.add_command(label = "Save File As", commad = command_Save_As_File )
			self.menu_file.add_command(label = "Exit",	       commad = command_File_Exit	 )

			self.master_menu.add_cascade(label = "Project", menu = self.menu_file)	
		except:
			raise
		return None

	def create_tools_menu(self, command_Tool_Sprite, command_Tool_Objects, command_Tool_Efects, command_Tool_Text, command_tool_Background):
		try:
			self.menu_tools = tk.Menu(self.master_menu, tearoff = 0, bg = "Gray", fg = "White")

			self.menu_tools.add_command(label = "Sprites",	command = command_Tool_Sprite 		)
			self.menu_tools.add_command(label = "Objects",	command = command_Tool_Objects 		)
			self.menu_tools.add_command(label = "Effects",	command = command_Tool_Efects 		)
			self.menu_tools.add_command(label = "Text", 	command = command_Tool_Text			); self.menu_tools.add_separator()
			self.menu_tools.add_command(label = "", 		command = command_tool_Background 	)

			self.master_menu.add_cascade(label = "Tools", menu = self.menu_tools)
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