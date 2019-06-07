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

			self.window.geometry("640x640+10+10")

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
			self.menu_file_tools = tk.Menu(self.master_menu, tearoff = 0, bg = "Gray50", fg = "Black")

			self.menu_file_tools.add_command(label = "New Project"     , command = self.cmds[0] )
			self.menu_file_tools.add_command(label = "Open Project"    , command = self.cmds[1] )
			self.menu_file_tools.add_command(label = "Save Project"    , command = self.cmds[2] )
			self.menu_file_tools.add_command(label = "Save Project As" , command = self.cmds[3] ); self.menu_file_tools.add_separator()
			self.menu_file_tools.add_command(label = "Sprites"         , command = self.cmds[4] )
			self.menu_file_tools.add_command(label = "Objects"         , command = self.cmds[5] )
			self.menu_file_tools.add_command(label = "Text"            , command = self.cmds[6] )
			self.menu_file_tools.add_command(label = "Background"      , command = self.cmds[7] )
			self.menu_file_tools.add_command(label = "Camera"          , command = self.cmds[8] ); self.menu_file_tools.add_separator()
			self.menu_file_tools.add_command(label = "Exit"            , command = self.cmds[9] )
		except:
			raise
		return None

	def create_events_menu(self):
		try:
			self.menu_events = tk.Menu(self.master_menu, tearoff = 0, bg = "Gray50", fg = "Black")

			self.menu_events.add_command(label = "New Event Mouse"    , command = self.cmds[10]  )
			self.menu_events.add_command(label = "New Event Keyboard" , command = self.cmds[11] )
			self.menu_events.add_command(label = "New Event Collide"  , command = self.cmds[12] )
			self.menu_events.add_command(label = "New Event Window"   , command = self.cmds[13] ); self.menu_events.add_separator()
			self.menu_events.add_command(label = "Event Settings"     , command = self.cmds[14] )
		except:
			raise
		return None

	def create_selected_sprite_menu(self):
		try:
			self.menu_selected_sprites = tk.Menu(self.master_menu, tearoff = 0, bg = "Gray50", fg = "Black")

			self.menu_selected_sprites.add_command(label = "Delete"   , command = self.sub_cmds[0]); self.menu_selected_sprites.add_separator()
			self.menu_selected_sprites.add_command(label = "Set Name" , command = self.sub_cmds[1])
			self.menu_selected_sprites.add_command(label = "Set Size" , command = self.sub_cmds[2])
			self.menu_selected_sprites.add_command(label = "Collide"  , command = self.sub_cmds[3])
			self.menu_selected_sprites.add_command(label = "Color"    , command = self.sub_cmds[4])
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

			self.resize_height = tk.Frame(self.master, bg = "Gray49")

			self.container = ttk.Notebook(self.master)

			self.frame_game_developer = tk.Frame(self.master, bg = "Gray")
			self.frame_event_game     = tk.Frame(self.master, bg = "Gray")

			self.container.add(self.frame_game_developer, text = "Game")
			self.container.add(self.frame_event_game, text = "Events")

			self.resize_height.place(x = 405, y = 0, width = self.master.winfo_screenwidth() - 215)
			self.container.place(x = 405, y = 0, height = self.master.winfo_screenheight() - 230)
		except:
			raise
		return None

	def resize_config(self, bottom_widget):
		try:
			self.resize_height.place(width = self.master.winfo_width(), height = self.master.winfo_height())

			def mouse(event):
				try:
					return self.resize_height.config(cursor = "sb_v_double_arrow")
				except:
					raise
				return None

			def res(event):
				try:
					if event.y < self.master.winfo_height() - 30:
						self.container.place(height = event.y)
						self.resize_height.place(height = event.y + 7.5)

						bottom_widget.place(y = event.y + 7.5)
						bottom_widget.place(height = self.master.winfo_screenheight())

					else:
						bottom_widget.place(y = self.master.winfo_height() - 15)
						bottom_widget.place(height = self.master.winfo_screenheight())

						self.resize_height.place(height = self.master.winfo_height() - 15)
						self.container.place(height = self.master.winfo_height() - 37.5)
				except:
					raise
				return None

			self.resize_height.bind("<B1-Motion>", res)
			self.resize_height.bind("<Enter>", mouse)
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

			self.resize = tk.Frame(master, width = 400, height = master.winfo_screenheight(), bg = "Gray49", bd = 5)
			self.frame  = tk.Frame(master, width = 400, height = master.winfo_screenheight(), bg = "Gray")

			self.resize.place(x = 3, y = 0)
			self.frame.place(x = 0, y = 0)
		except:
			raise
		return None

	def resize_config(self, container, widget_right):
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
						self.frame.config(width = event.x)
						self.resize.config(width = event.x)

						container[0].place(x = event.x + 5)
						container[1].place(x = event.x + 5)

						widget_right.frame.place(x = event.x)

					else:
						self.frame.config(width = 2)
						self.resize.config(width = 2)

						container[0].place(x = 5)
						container[1].place(x = 5)						
						widget_right.frame.place(x = 5)
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
	def __init__(self, master, icon_path_00, icon_path_01, icon_path_02):
		try:
			self.icon_path_00 = icon_path_00
			self.icon_path_01 = icon_path_01
			self.icon_path_02 = icon_path_02

			self.master        = master.frame
			self.master_master = master.master

			self.tree = ttk.Treeview(self.master)

			self.tree.place(x = 10, y = 10, width = self.master.winfo_width() - 25, height = self.master.winfo_height() - 50)
		except:
			raise
		return None

	def create_class(self):
		try:
			image_icone_00 = tk.PhotoImage(file = self.icon_path_00)
			icone_00       = tk.Label(image = image_icone_00)
			icone_00.photo = image_icone_00

			image_icone_01 = tk.PhotoImage(file = self.icon_path_01)
			icone_01       = tk.Label(image = image_icone_01)
			icone_01.photo = image_icone_01

			image_icone_02 = tk.PhotoImage(file = self.icon_path_02)
			icone_02       = tk.Label(image = image_icone_02)
			icone_02.photo = image_icone_02

			self.sprites = self.tree.insert("", "end", "Sprites", image = icone_00.photo, text = " " + "Sprites")
			self.objects = self.tree.insert("", 'end', "Objects", image = icone_01.photo, text = " " + "Objects")
			self.cameras = self.tree.insert("", 'end', "Cameras", image = icone_02.photo, text = " " + "Cameras")
		except:
			raise
		return None

	def up(self, bool):
		try:
			if bool is True:
				self.tree.place(width = self.master.winfo_width() - 25, height = self.master_master.winfo_height() - self.master_master.winfo_height() / 2)

			elif bool is False:
				self.tree.place(width = self.master.winfo_width() - 25, height = self.master_master.winfo_height() - 45)

		except:
			raise
		return None

class sprite_options(object):
	def __init__(self, master_win, master, sprites, selected, about_frame):
		try:
			self.master_win  = master_win
			self.master      = master.frame
			self.sprites     = sprites
			self.selected    = selected
			self.about_frame = about_frame

			self.tag    = None
			self.path   = None

			self.x = 0
			self.y = 0
			self.w = 0
			self.h = 0

			self.width  = 0
			self.height = 0

			self.canvas = tk.Canvas(self.master, width = self.master.winfo_width() - 5, height = self.master.winfo_height() - 66, bg = "Gray")

			self.text_tag    = tk.Label(self.canvas, text = self.tag, bg = "Gray")
			self.text_xpos   = tk.Label(self.canvas, text = "x {}".format(self.x), bg = "Gray")
			self.text_ypos   = tk.Label(self.canvas, text = "y {}".format(self.y), bg = "Gray")
			self.text_width  = tk.Label(self.canvas, text = "width {}".format(self.w), bg = "Gray")
			self.text_height = tk.Label(self.canvas, text = "height {}".format(self.h), bg = "Gray")
			self.text_path   = tk.Label(self.canvas, text = "Path: {}".format(self.path), bg = "Gray")

			self.canvas.place(x = 10, y = self.about_frame.winfo_height() - 25)

			self.widgets = [self.canvas]
		except:
			raise
		return None

	def show(self, master, sprites, selected, up = None):
		try:
			if up:
				try:
					self.master   = master
					self.selected = sprites[selected]
					self.tag      = sprites[selected].tag
					self.path     = sprites[selected].path
	
					self.x = sprites[selected].rect.x
					self.y = sprites[selected].rect.y
					self.w = sprites[selected].rect.w
					self.h = sprites[selected].rect.h
	
					self.canvas.configure(width = self.master.winfo_width() - 5, height = self.master.winfo_height() - 66)
	
					self.canvas.place(x = 10, y = self.about_frame.winfo_height() + 25)
					
					self.text_tag.configure(text = self.tag)
					self.text_path.configure(text = "{}".format(self.path))
					self.text_xpos.configure(text = "x: {}".format(self.x))
					self.text_ypos.configure(text = "y: {}".format(self.y))
					self.text_width.configure(text = "Width: {}".format(self.w))
					self.text_height.configure(text = "Height: {}".format(self.h))
	
					self.text_tag.place(x = 10, y = 10)
					self.text_path.place(x = 10, y = 25)
					self.text_xpos.place(x = 10, y = 50)
					self.text_ypos.place(x = 10, y = 75)
					self.text_width.place(x = 75, y = 50)
					self.text_height.place(x = 75, y = 75)
	
					self.master_win.update()
				except:
					pass
			else:
				for widgets in self.widgets:
					widgets.place_forget()
		except:
			raise
		return None

class frame_debug_tools(object):
	def __init__(self, master, left_widget, container):
		try:
			self.master      = master
			self.left_widget = left_widget
			self.container   = container

			left_widget.update()

			self.frame = tk.Frame(self.master, width = master.winfo_screenwidth(), height = 200, bg = "Gray")

			self.frame.place(x = self.left_widget.winfo_width() + 5, y = self.master.winfo_height() - 200)
		except:
			raise
		return None

class console_debug(object):
	def __init__(self, master, master_):
		try:
			self.master  = master
			self.master_ = master_

			self.master_.update()
			self.master.update()

			self.console = tk.Text(self.master, bg = "Gray49", state = "disabled")
		except:
			raise
		return None

	def ENGINE_PROCESS_PRINT_FROM_CONSOLE(self, x):
		try:
			self.console.config(state = "normal")
			self.console.insert(tk.END, "{}\n".format(x))
			self.console.config(state = "disabled")
		except:
			raise
		return None

	def up(self):
		try:
			self.console.place(x = 150, y = 10, width = self.master_.winfo_width() - self.master.winfo_x() - 165, height = self.master_.winfo_height() - self.master.winfo_y() - 50)
		except:
			raise
		return None