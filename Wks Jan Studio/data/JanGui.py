from JanPort import tk, ttk, messagebox, _JanJa, os

class start_(object):
	def __init__(self, image, callback, hardware, math, json = None, version = None):
		try:
			self.callback    = callback
			self.load_number = 0
			self.hardware    = hardware
			self.json        = json
			self.math        = math
			self.ver         = version

			self.window = tk.Tk()
			self.window.overrideredirect(True)

			self.window.configure(background = "Gray")

			self.window.geometry("640x640+200+200")

			self.image(image)
			self.text()

			self.loading = ttk.Progressbar(self.window, orient = "horizontal", length = 620, mode = "determinate")
			self.loading.place(x = 10, y = 610)

			self.loading_tread()
		except:
			raise
		return None

	def image(self, image):
		try:
			image = tk.PhotoImage(file = image)

			image_show = tk.Label(self.window, image = image)
			image_show.photo = image
			image_show.place(x = 0, y = 0)
		except:
			raise
		return None

	def text(self):
		try:
			credit = tk.Label(self.window, text = "Wks Jan Studio", font = "Arial 10", bg = "Gray")
			credit.place(x = 10, y = 490)

			programer = tk.Label(self.window, text = "Programer - Sr_Rina", font = "Arial 10", bg = "Gray")
			programer.place(x = 10, y = 510)

			designer = tk.Label(self.window, text = "Designer - PEDRIN", font = "Arial 10", bg = "Gray")
			designer.place(x = 10, y = 530)

			version = tk.Label(self.window, text = self.ver, font = "Arial 10", bg = "Gray")
			version.place(x = 10, y = 560)

			self.progress_text = tk.Label(self.window, text = "Loading...", font = "Arial 10", bg = "Gray")
			self.progress_text.place(x = 10, y = 585)
		except:
			raise
		return None

	def loading_tread(self):
		try:
			self.loading["maximum"] = 200
			
			run = True
			while (run):
				self.load_number += 0.1
				self.loading["value"] = self.load_number

				if self.load_number >= 25:
					self.progress_text.configure(text = self.json.get("Default Resolution"))

				if self.load_number >= 50:
					self.progress_text.configure(text = self.json.get("Width"))

				if self.load_number >= 75:
					self.progress_text.configure(text = self.json.get("Height"))

				if self.load_number >= 100:
					self.progress_text.configure(text = self.json.get("Devolper"))

				if self.load_number >= 125:
					self.math.Sync_Resolution(self.json, self.hardware)
					self.progress_text.configure(text = os.path.abspath("_JanDat.py") + "...")

				if self.load_number >= 200:
					self.window.destroy()
					run = False

				try:
					self.window.update()
				except:
					pass

			self.callback()
		except:
			raise
		return None

class create_window(object):
	def __init__(self, width, height, title, color, icon):
		try:
			self.window = tk.Tk()
			self.window.geometry("{}x{}".format(width, height))
			self.window.title(title)
			
			self.window.iconbitmap(icon)
			self.window.configure(background = color)

			self.style = ttk.Style()
			self.style.theme_use("clam")

			self.style.configure("Treeview", background = "Gray", fieldbackground = "Gray")

			self.window.update()
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
			return self.window
		except:
			raise
		return None

	def get(self, x):
		try:
			if ("Width") is (x):
				return self.window.winfo_width()

			if ("Height") is (x):
				return self.window.winfo_height()
		except:
			raise
		return None

	def close(self):
		try:
			return self.window.destroy()
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

			self.menu_file_tools.add_command(label = "Open File"    , command = self.cmds[0] )
			self.menu_file_tools.add_command(label = "Save File"    , command = self.cmds[1] )
			self.menu_file_tools.add_command(label = "Save File As" , command = self.cmds[2] ); self.menu_file_tools.add_separator()
			self.menu_file_tools.add_command(label = "Sprites"      , command = self.cmds[3] )
			self.menu_file_tools.add_command(label = "Objects"      , command = self.cmds[4] )
			self.menu_file_tools.add_command(label = "Text"         , command = self.cmds[5] )
			self.menu_file_tools.add_command(label = "Background"   , command = self.cmds[6] )
			self.menu_file_tools.add_command(label = "Camera"       , command = self.cmds[7] ); self.menu_file_tools.add_separator()
			self.menu_file_tools.add_command(label = "Exit"         , command = self.cmds[8] )
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
			self.menu_selected_sprites = tk.Menu(self.master_menu, tearoff = 0, bg = "Gray", fg = "White")

			self.menu_selected_sprites.add_command(label = "Delete (delete)"          , command = self.sub_cmds[0]); self.menu_selected_sprites.add_separator()
			self.menu_selected_sprites.add_command(label = "Set Name (f2)"            , command = self.sub_cmds[1])
			self.menu_selected_sprites.add_command(label = "Set Size (mouse 2)"  	  , command = self.sub_cmds[2])
			self.menu_selected_sprites.add_command(label = "Collide (shift + d)"      , command = self.sub_cmds[3])
			self.menu_selected_sprites.add_command(label = "Color (ctrl + shift + b)" , command = self.sub_cmds[4])
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
	def __init__(self, master, frame, tag):
		try:
			self.master = master

			self.container = ttk.Notebook(self.master)

			self.frame_game_developer = tk.Frame(self.master, width = self.master.winfo_screenwidth  () , height = self.master.winfo_screenheight(), bg = "Gray")
			self.frame_event_game     = tk.Frame(self.master, width = self.master.winfo_screenheight () , height = self.master.winfo_screenheight(), bg = "Gray")

			self.container.add(self.frame_game_developer , text = "Game    "   )
			self.container.add(self.frame_event_game     , text = "Events    " )

			self.container.place(x = 405, y = 0)
		except:
			raise
		return None

	def get_id(self):
		try:
			return self.frame_game_developer
		except:
			raise
		return None

class create_status(object):
	def __init__(self, master, text):
		try:
			self.master = master

			self.label = tk.Label(self.master, text = text, bg = "Gray", anchor = "w", relief = tk.SUNKEN)

			self.label.pack(fill = tk.X, side = tk.BOTTOM)
		except:
			raise
		return None

	def set_text(self, text):
		try:
			return self.label.configure(text = text)
		except:
			raise
		return None

class create_frame_tools(object):
	def __init__(self, master):
		try:
			self.master    = master

			self.resize = tk.Frame(master, width = 400, height = master.winfo_screenheight(), bg = "Gray", bd = 5)
			self.frame  = tk.Frame(master, width = 400, height = master.winfo_screenheight(), bg = "Gray")

			self.resize.place(x = 3, y = 0)
			self.frame.place(x = 0, y = 0)

			self.container = ttk.Notebook(self.resize)
		except:
			raise
		return None

	def resize_config(self, container):
		try:
			def mouse(event):
				try:
					self.resize.config(cursor = "sb_h_double_arrow")
				except:
					pass
				return None

			def res(event):
				try:
					if event.x > 0:
						self.frame.config(width = event.x); self.resize.config(width = event.x)
						container.place(x = event.x + 5)

					else:
						self.frame.config(width = 2); self.resize.config(width = 2)
						container.place(x = 5)
				except:
					pass
				return None

			self.resize.bind("<B1-Motion>", res)
			self.resize.bind("<Enter>", mouse)
		except:
			raise
		return None

	def get_raise(self):
		try:
			return self.frame
		except:
			raise
		return None

class create_object_tree_view(object):
	def __init__(self, master, icon_path_00, icon_path_01):
		try:
			self.master        = master.frame
			self.master_master = master.master

			self.tree = ttk.Treeview(self.master)

			image_icone_00 = tk.PhotoImage(file = icon_path_00)
			icone_00       = tk.Label(image = image_icone_00)
			icone_00.photo = image_icone_00

			image_icone_01 = tk.PhotoImage(file = icon_path_01)
			icone_01       = tk.Label(image = image_icone_01)
			icone_01.photo = image_icone_01

			self.sprites = self.tree.insert("", "end", "Sprites", image = icone_00.photo, text = " " + "Sprites")
			self.objects = self.tree.insert("", 'end', "Objects", image = icone_01.photo, text = " " + "Objects")
			self.cameras = self.tree.insert("", 'end', "Cameras", text = " " + "Cameras")

			self.tree.place(x = 10, y = 10, width = self.master.winfo_width() - 25, height = self.master.winfo_height() - 50)
		except:
			raise
		return None

	def up(self, bool):
		try:
			if bool == True:
				self.tree.place(width = self.master.winfo_width() - 25, height = self.master_master.winfo_height() - self.master_master.winfo_height() / 2)

			elif bool is False:
				self.tree.place(width = self.master.winfo_width() - 25, height = self.master_master.winfo_height() - 45)

		except:
			raise
		return None

class sprite_options(object):
	def __init__(self, master, sprites, selected, about_frame):
		try:
			self.master      = master.frame
			self.sprites     = sprites
			self.selected    = selected
			self.about_frame = about_frame

			self.canvas = tk.Canvas(self.master, width = self.master.winfo_width() - 5, height = self.master.winfo_height() - 66, bg = "Gray")

			self.canvas.place(x = 10, y = self.about_frame.winfo_height() - 25)
		except:
			raise
		return None

	def show(self, master, sprites, selected, up = None):
		try:
			self.master   = master
			self.sprites  = sprites
			self.selected = selected

			if up:
				self.canvas.place(x = 10, y = self.about_frame.winfo_height() + 25)
				self.canvas.configure(width = self.master.winfo_width() - 5, height = self.master.winfo_height() - 66)

			else:
				self.canvas.place_forget()
		except:
			raise
		return None