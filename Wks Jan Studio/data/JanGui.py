from JanPort import tk, ttk, messagebox

class create_window(object):
	def __init__(self, width, height, title, color):
		try:
			self.Window = tk.Tk()
			self.Window.geometry("{}x{}".format(width, height))
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
	def __init__(self, master, cmds, sub_cmds):
		try:
			self.master_menu = tk.Menu(master, tearoff = 0)
			self.master = master

			master.configure(menu = self.master_menu, bg = "Gray")

			self.cmds     = cmds
			self.sub_cmds = sub_cmds

			self.create_selected_sprite_menu()
			self.create_file_and_tool_menu()
			self.create_events_menu()
		except:
			raise
		return None

	def create_file_and_tool_menu(self):
		try:
			self.menu_file_tools = tk.Menu(self.master_menu, tearoff = 0, bg = "Gray", fg = "White")

			self.menu_file_tools.add_command(label = "Open File",    command = self.cmds[0] )
			self.menu_file_tools.add_command(label = "Save File",    command = self.cmds[1] )
			self.menu_file_tools.add_command(label = "Save File As", command = self.cmds[2] ); self.menu_file_tools.add_separator()
			self.menu_file_tools.add_command(label = "Sprites",      command = self.cmds[3] )
			self.menu_file_tools.add_command(label = "Objects",      command = self.cmds[4] )
			self.menu_file_tools.add_command(label = "Effects",      command = self.cmds[5] )
			self.menu_file_tools.add_command(label = "Text",         command = self.cmds[6] )
			self.menu_file_tools.add_command(label = "Background",   command = self.cmds[7] ); self.menu_file_tools.add_separator()
			self.menu_file_tools.add_command(label = "Exit",         command = self.cmds[8] )
		except:
			raise
		return None

	def create_events_menu(self):
		try:
			self.menu_events = tk.Menu(self.master_menu, tearoff = 0, bg = "Gray", fg = "White")

			self.menu_events.add_command(label = "New Event Mouse"    , command = self.cmds[9]  )
			self.menu_events.add_command(label = "New Event Keyboard" , command = self.cmds[10] )
			self.menu_events.add_command(label = "New Event Collide"  , command = self.cmds[11] )
			self.menu_events.add_command(label = "New Event Window"   , command = self.cmds[12] ); self.menu_events.add_separator()
			self.menu_events.add_command(label = "Event Settings"     , command = self.cmds[13] )
		except:
			raise
		return None

	def create_selected_sprite_menu(self):
		try:
			self.menu_selected_sprites = tk.Menu(self.master_menu, tearoff = 0, bg = "Gray", fg= "White")

			self.menu_selected_sprites.add_command(label = "Delete Sprite (del)" , command = self.sub_cmds[0])
		except:
			raise
		return None

	def get(self, x):
		try:
			if (x) is ("Main"):
				return (self.menu_file_tools)

			elif (x) is ("MainSprite"):
				return (self.menu_selected_sprites)

			elif (x) is ("Events"):
				return (self.menu_events)
		except:
			raise
		return None

class create_container(object):
	def __init__(self, master):
		try:
			self.master = master

			self.container = ttk.Notebook(self.master)

			self.frame_game_developer = tk.Canvas(self.master, width = self.master.winfo_screenwidth  () , height = self.master.winfo_screenheight(), bg = "Gray")
			self.frame_event_game     = tk.Canvas(self.master, width = self.master.winfo_screenheight () , height = self.master.winfo_screenheight(), bg = "Gray")

			self.container.add(self.frame_game_developer , text = "Game    "   )
			self.container.add(self.frame_event_game     , text = "Events    " )

			self.container.place(x = 0, y = 0)
		except:
			raise
		return None

	def get_id(self):
		try:
			return self.frame_game_developer
		except:
			raise
		return None