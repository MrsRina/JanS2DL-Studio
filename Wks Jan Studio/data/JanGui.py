from JanPort import tk, ttk, messagebox

class create_window(object):
	def __init__(self, width, height, title, color):
		try:
			self.Window = tk.Tk()
			self.Window.geometry("{}x{}+1280+0".format(width, height))
			self.Window.title(title)
			self.Window.configure(background = color)

			self.Style = ttk.Style()
			self.Style.theme_use("clam")
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

			master.configure(menu = self.master_menu)
		except:
			raise
		return None

	def create_file_menu(self, command_Open_File, command_Save_File, command_Save_As_File, command_File_Exit):
		try:
			self.menu_file = tk.Menu(self.master_menu, tearoff = 0, bg = "Gray", fg = "White")

			self.menu_file.add_command(label = "Open File",	   command = command_Open_File	  )
			self.menu_file.add_command(label = "Save File",	   command = command_Save_File    )
			self.menu_file.add_command(label = "Save File As", command = command_Save_As_File ); self.menu_file.add_separator()
			self.menu_file.add_command(label = "Exit",	       command = command_File_Exit	  )

			self.master_menu.add_cascade(label = "Project", menu = self.menu_file)	
		except:
			raise
		return None

	def create_tools_menu(self, command_Tool_Sprite, command_Tool_Objects, command_Tool_Efects, command_Tool_Text, command_tool_Background):
		try:
			self.menu_tools = tk.Menu(self.master_menu, tearoff = 0, bg = "Gray", fg = "White")

			self.menu_tools.add_command(label = "Sprites",	  command = command_Tool_Sprite 		)
			self.menu_tools.add_command(label = "Objects",	  command = command_Tool_Objects 		)
			self.menu_tools.add_command(label = "Effects",	  command = command_Tool_Efects 		)
			self.menu_tools.add_command(label = "Text", 	  command = command_Tool_Text			); self.menu_tools.add_separator()
			self.menu_tools.add_command(label = "Background", command = command_tool_Background 	)

			self.master_menu.add_cascade(label = "Tools", menu = self.menu_tools)
		except:
			raise
		return None

	def create_events_menu(self, command_New_Event_Mouse, command_New_Event_Keyboard, command_New_Event_Collide, command_New_Event_Window, command_Event_Settings):
		try:
			self.menu_events = tk.Menu(self.master_menu, tearoff = 0, bg = "Gray", fg = "White")

			self.menu_events.add_command(label = "New Event Mouse"    , command = command_New_Event_Mouse	 )
			self.menu_events.add_command(label = "New Event Keyboard" , command = command_New_Event_Keyboard )
			self.menu_events.add_command(label = "New Event Collide"  , command = command_New_Event_Collide  )
			self.menu_events.add_command(label = "New Event Window"   , command = command_New_Event_Window   )
			self.menu_events.add_command(label = "Event Settings"     , command = command_Event_Settings     )

			self.master_menu.add_cascade(label = "Events", menu = self.menu_events)
		except:
			raise

	def create_about_menu(self, command_About_Wks_Jan_Studio, command_About_Engine):
		try:
			self.menu_about = tk.Menu(self.master_menu, tearoff = 0, bg = "Gray", fg = "White")

			self.menu_about.add_command(label = "About Wks Jan Studio" , command = None )
			self.menu_about.add_command(label = "About JanJaEngine"    , command = None )

			self.master_menu.add_cascade(label = "About", menu = self.menu_about)
		except:
			raise
		return None

class create_container(object):
	def __init__(self, master):
		try:
			self.master = master

			self.container = ttk.Notebook(self.master)

			self.frame_game_devolper = tk.Frame(self.master, width = self.master.winfo_screenwidth  () , height = self.master.winfo_screenheight(), bg = "Gray")
			self.frame_event_game    = tk.Frame(self.master, width = self.master.winfo_screenheight () , height = self.master.winfo_screenheight(), bg = "Gray")
			
			self.container.add(self.frame_game_devolper , text = "Game    ")
			self.container.add(self.frame_event_game    , text = "Events    ")

			self.container.place(x = 0, y = 0)
		except:
			raise
		return None

	def get_id(self):
		try:
			cache_x = [self.frame_game_devolper, self.frame_event_game]
			for x in cache_x:
				return x
		except:
			raise
		return None