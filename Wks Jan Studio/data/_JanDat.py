from _JanJa  import JAN_ENGINE_engine, hardware_res, replace_folder, filedialog, load_type, sys, os
from JanPort import JanCompiler, JanConsoleText, JanDecode, JanGui, JanMath

int_engine = lambda _int: int(JAN_ENGINE_engine.get(_int))

class DAT(object):
	pygame = None
	
	def __init__(self, lib_pygame_sdl):
		try:
			self.pygame = lib_pygame_sdl

			self.jan_win = JanGui.create_window(int_engine("Width"), int_engine("Height"), "JanS2DL-Studio", "Gray",
				r"{}".format(replace_folder("/_JanJa.py", "/icone.ico")))

			self.bool_click     = 0
			self.some_selected  = False
			self.bool_tool_tree = False
			self.thread_tick    = 1

			self.selected_pos_sprites = None
			self.selected_tree_view   = None
			self.selected_now         = None
			self.selected             = None
			self.sprites              = {}

			self.camera_x = 0
			self.camera_y = 0
			self.camera   = "None"
			self.cameras  = {}

			self.project         = None
			self.event_file      = 0
			self.new_folder_path = None

			self.create_widget()

			self.x_main, self.y_main = JanMath.Sync_Resolution_Pos(self.jan_win.window)

			self.jan_run = True

			self.jan_width_pygame  = 1024
			self.jan_height_pygame = 768

			self.jan_editor_background_color = (127, 127, 127, 0)

			self.create_frame(self.jan_container.get_id())

			self.clock = self.pygame.time.Clock()

			self.whiling()

			self.window_loop()
		except:
			raise
		return None

	def whiling(self):
		try:
			self.jan_pygame.fill((self.jan_editor_background_color))
			self.background_(JanDecode.JAN_IMAGE_DECODE_ALPHA)
				
			for events in self.pygame.event.get():
				self.events_sprite(events)
				self.dynamic_popup(events)

			print(self.thread_tick)
				
			self.up_events()
			self.refresh()

			self.pygame.display.flip(); self.jan_win.window.after(self.thread_tick, self.whiling) # loop
		except:
			raise
		return None

	def events_select_tree(self):
		try:
			def selected_some_tree(event):
				try:
					for item in self.tool_tree.selection():
						if not item.find("Class Sprites"):
							selected_now = replace(item, "Class Sprites ", "")

							# Remove taf Class Sprite for select
							if self.selected is None:
								self.bool_tool_tree = True
								self.selected       = selected_now

								self.sprites[self.selected].selected = True

								self.some_selected = True

								self.thread_tick = 1

							elif self.selected != None:
								self.sprites[self.selected].selected = False
								self.selected                        = selected_now

								self.sprites[self.selected].selected = True
								self.some_selected                   = True

						elif not item.find("Class Objects"):
							selected_now = replace(item, "Class Objects ", "")

							# Remove taf Class Sprite for select
							if self.selected is None:
								self.bool_tool_tree = True
								self.selected       = selected_now

								self.sprites[self.selected].selected = True

								self.some_selected = True

							elif self.selected != None:
								self.sprites[self.selected].selected = False
								self.selected                        = selected_now

								self.sprites[self.selected].selected = True
								self.some_selected                   = True

						else:
							if self.selected is None:
								self.bool_tool_tree = False

								self.some_selected = False
								self.selected      = None

							elif self.selected != None:
								self.sprites[self.selected].selected = False
								self.bool_tool_tree                  = False

								self.some_selected = False
								self.selected      = None
				except:
					pass

			self.tool_tree.bind("<<TreeviewSelect>>", selected_some_tree)

			self.jan_win.window.update()
		except:
			raise
		return None

	def events_sprite(self, event):
		try:
			pygame = self.pygame

			if event.type is pygame.MOUSEBUTTONDOWN:
				for sprite_selected in self.sprites.values():
					if event.button is 1:
						try:
							if sprite_selected.rect.collidepoint(event.pos):
								if self.bool_click is 0:
									self.bool_click = 0.1

								elif self.bool_click <= 1.5:
									if self.selected != None:
										self.handling_cmouse                 = False
										self.sprites[self.selected].selected = False
										self.sprites[self.selected].move     = False
										self.selected                        = sprite_selected.tag
										self.sprites[self.selected].selected = True
										self.sprites[self.selected].move     = True
										self.bool_tool_tree                  = True
										self.some_selected                   = True
										self.jan_sprite_options.up           = True

										self.tool_tree.item("Class {} {}".format(self.sprites[self.selected].type, self.sprites[self.selected].tag), open = True)
										self.tool_tree.selection_set("Class {} {}".format(self.sprites[self.selected].type, self.sprites[self.selected].tag))
										self.tool_tree.focus_set()
										self.tool_tree.focus("Class {} {}".format(self.sprites[self.selected].type, self.sprites[self.selected].tag))

										self.jan_win.window.update()

									elif self.selected is None:
										self.handling_cmouse                 = False
										self.selected                        = sprite_selected.tag
										self.sprites[self.selected].selected = True
										self.sprites[self.selected].move     = True
										self.jan_sprite_options.up           = True
										self.bool_tool_tree                  = True
										self.some_selected                   = True

										self.tool_tree.item("Class {} {}".format(self.sprites[self.selected].type, self.sprites[self.selected].tag), open = True)
										self.tool_tree.selection_set("Class {} {}".format(self.sprites[self.selected].type, self.sprites[self.selected].tag))
										self.tool_tree.focus_set()
										self.tool_tree.focus("Class {} {}".format(self.sprites[self.selected].type, self.sprites[self.selected].tag))

										self.jan_win.window.update()
						except:
							pass

					if event.button is 1:
						try:
							if self.sprites[self.selected].selected:
								if self.sprites[self.selected].rect.collidepoint(event.pos):
									self.sprites[self.selected].move = True
									self.jan_sprite_options.normalize_thread()

								elif not self.sprites[self.selected].rect.collidepoint(event.pos):
									if self.selected != None:
										self.tool_tree.selection_remove("Class {} {}".format(self.sprites[self.selected].type, self.sprites[self.selected].tag))
										self.tool_tree.item("Class {} {}".format(self.sprites[self.selected].type, self.sprites[self.selected].tag), open = False)

										self.sprites[self.selected].selected = False
										self.sprites[self.selected].move     = False
										self.jan_sprite_options.up           = False
										self.bool_tool_tree                  = False
										self.selected                        = None
										self.some_selected                   = False

										self.jan_win.window.update()

									else:
										self.tool_tree.selection_remove("Class {} {}".format(self.sprites[self.selected].type, self.sprites[self.selected].tag))
										self.tool_tree.item("Class {} {}".format(self.sprites[self.selected].type, self.sprites[self.selected].tag), open = False)

										self.jan_sprite_options.up = False
										self.bool_tool_tree        = False
										self.selected              = None
										self.some_selected         = False

										self.jan_win.window.update()
						except:
							pass

					if event.button is 2:
						try:
							if self.sprites[self.selected].selected:
								self.sprites[self.selected].resize = True
								self.jan_sprite_options.normalize_thread()
						except:
							pass

					if event.button is 3:
						try:
							if self.sprites[self.selected].type is "Sprites":
								if self.sprites[self.selected].selected:
									self.create_selected_sprite_menu()

							elif self.sprites[self.selected].type is "Objects":
								if self.sprites[self.selected].selected:
									pass
						except:
							pass

			if event.type is pygame.MOUSEMOTION:
				if event.buttons[0]:
					if self.selected is None:
						self.camera_x = self.camera_x + event.rel[0]
						self.camera_y = self.camera_y + event.rel[1]

			if event.type is pygame.MOUSEBUTTONUP:
				if event.button is 1:
					try:
						if self.sprites[self.selected].selected:
							self.sprites[self.selected].move = False
					except:
						pass

				if event.button is 2:
					if self.selected != None:
						try:
							self.sprites[self.selected].resize = False
						except:
							pass

			if event.type is pygame.KEYUP:
				if event.key is pygame.K_DELETE:
					self.delete_selected_sprite()
		except:
			raise
		return None

	def delete_selected_sprite(self):
		try:
			self.tool_tree.delete("Class {} {}".format(self.sprites[self.selected].type, self.sprites[self.selected].tag))
			self.sprites[self.selected].do("delete")
			self.remove("sprite")

			self.selected       = None
			self.some_selected  = False
			self.bool_tool_tree = False

			self.pygame.display.flip()
			self.jan_win.get_master().update()
		except:
			raise
		return None

	def remove(self, x):
		try:
			if x is "sprite":
				return self.sprites.pop(self.selected)
		except:
			pass
		return None

	def up_events(self):
		try:
			#self.events_select_tree()
			self.poop_up()

			self.set_title("JanS2DL-Studio {ticks}".format(ticks = self.thread_tick))

			self.jan_frame_tools.resize_config([self.jan_container.container, self.jan_container.resize_height], self.jan_debug_tools)
			self.jan_container.resize_config(self.jan_debug_tools.frame)
			
			self.jan_tree.up(self.bool_tool_tree)
			self.jan_debug_tools.up()
			self.jan_console_debug.up(self)

			self.jan_tree.project_name.configure(text = "..." if self.project is None else self.project.json["Name"])
			self.jan_tree.menus(self, "Menus of treeview edits")

			self.jan_menu.menu_file_tools.entryconfig(2, state = JanMath.Sync_File(self.event_file))
			self.jan_menu.menu_file_tools.entryconfig(3, state = JanMath.Sync_File_As(self.event_file))

			self.x_main, self.y_main = JanMath.Sync_Resolution_Pos(self.jan_win.window)

			self.jan_sprite_options.show(self.sprites, self.selected, self, ref = self.ref_sprite, up = self.bool_tool_tree)

			try:
				self.jan_status.set_text("{project} {selected}{mouse_pos} {selected_x} {selected_y} {selected_w} {selected_h}".format(
					project    = "" if self.project is None else self.project.local,
					selected   = "" if self.selected is None else self.selected,
					mouse_pos  = self.pygame.mouse.get_pos() if self.selected is None else " ",
					selected_x = "" if self.selected is None else self.sprites[self.selected].x,
					selected_y = "" if self.selected is None else self.sprites[self.selected].y,
					selected_w = "" if self.selected is None else self.sprites[self.selected].w,
					selected_h = "" if self.selected is None else self.sprites[self.selected].h)
				)

				self.jan_editor_status.set_text("{camera} {x} x {y}".format(
					camera = self.camera,
					x = self.camera_x,
					y = self.camera_y)
				)
			except:
				pass

			if self.bool_click != 0:
				self.bool_click += 0.1

				if self.bool_click >= 2:
					self.bool_click = 0
		except:
			raise
		return None

	def create_new_project(self):
		try:
			def color_error():
				def return_color():
					try:
						self.cache_project_name.configure(bg = "Gray")
						self.cache_project_width.configure(bg = "Gray")
						self.cache_project_height.configure(bg = "Gray")
						self.cache_project_comment.configure(bg = "Gray")
					except:
						raise
					return None

				self.cache_project_name.configure(bg = "Red")
				self.cache_project_width.configure(bg = "Red")
				self.cache_project_height.configure(bg = "Red")
				self.cache_project_comment.configure(bg = "Red")

				self.cache_project_name.after(2000, return_color)

				self.jan_win.window.update()

			if self.cache_project_name.get(1.0, tk.INSERT) != "":
				try:
					self.project = JanCompiler.create_project(
					local    = self.new_folder_path,
					name     = self.cache_project_name.get(1.0, tk.INSERT),
					camera   = (self.camera_x, self.camera_y),
					comments = self.cache_project_comment.get(1.0, tk.INSERT),
					version  = "1.4"
					)

					self.new_folder_path = None

					self.project = JanCompiler.open_project(path = self.project.local)

					if self.index_type is None:
						self.clear()
						self.JanTree.create_class()

					else:
						for sprites in self.sprites.values():
							sprites.do("save", project = self.project)

					self.project.save()

					self.event_file    = 2
					self.some_selected = False

					self.cache_project_window.destroy()

					self.jan_win.window.update()

				except:
					color_error()
			else:
				color_error()
		except:
			raise
		return None

	def cancel_new_project(self):
		try:
			self.new_folder_path = None
			self.some_selected   = False
			self.cache_project_window.destroy()

			self.jan_win.window.update()
		except:
			raise
		return None

	def new_project(self, save = None):
		try:
			find = filedialog.askdirectory()

			if find:
				self.new_folder_path = find
				self.some_selected = True

				self.index_type = save

				project_window = JanGui.project_window(self.jan_win.get_master(), self.create_new_project, self.cancel_new_project)

				self.cache_project_window  = project_window
				self.cache_project_name    = project_window.text_name_project_
				self.cache_project_width   = project_window.text_widht_project_
				self.cache_project_height  = project_window.text_height_project_
				self.cache_project_comment = project_window.text_comment_project_

				project_window.tought_loop()

				self.jan_win.window.update()
		except:
			raise
		return None

	def open_project(self):
		try:
			find = filedialog.askopenfilename(initialdir = os.path.realpath(__file__), title = "Select file", filetypes = (
			(
				"files", "*.jpf"
			),
			(
				"all files", "*.*"
			)))

			self.console_print("Project JPF: {}".format(JanConsoleText.is_project_file(find)))

			if JanConsoleText.is_project_file(find):
				try:
					self.clear()
	
					self.project    = JanCompiler.open_project(path = find)
					self.event_file = 2
	
					self.JanTree.create_class()
	
					self.camera_x, self.camera_y = self.project.json["Project Camera Pos"]
	
					find_sprites = None
					find_objects = None
	
					if len(self.project.json["Game Sprites"]) > 0:
						find_sprites = list(self.project.json["Game Sprites"])

						for sprites in find_sprites:
							self.selected = sprites.replace("Class Sprites ", "")
							
							self.console_print(self.selected)
	
							self.sprites[self.selected] = load_type([self.project, "project_load"], master = self.jan_pygame, state = self,
							tag = sprites.replace("Class Sprites ", ""), type = "Sprites", cam_x = self.camera_x, cam_y = self.camera_y)
	
							self.tool_tree.insert(
							self.tool_tree_sprites, "end",
							"Class Sprites {}".format(self.sprites[self.selected].tag),
							text = self.sprites[self.selected].tag,
							open = True)
	
							self.selected = None
	
					if len(self.project.json["Game Objects"]) > 0:
						find_objects = list(self.project.json["Game Objects"])
	
						for objects in find_objects:
							self.selected = objects.replace("Class Objects ", "")
	
							self.sprites[self.selected] = load_type([self.project, "project_load"], master = self.jan_pygame, state = self,
							tag = objects.replace("Class Objects ", ""), type = "Objects", cam_x = self.camera_x, cam_y = self.camera_y)
	
							self.tool_tree.insert(
							self.tool_tree_objects, "end",
							"Class Objects {}".format(self.sprites[self.selected].tag),
							text = self.sprites[self.selected].tag,
							open = True)
	
							self.selected = None

					self.console_print(JanConsoleText.print_load_project(self.project.json))

					self.pygame.display.update()
					self.jan_win.window.update()

				except:
					self.console_print("This file corrupted or old version ... \n{}".format(find))
					
					self.pygame.display.update()
					self.jan_win.window.update()
		except:
			raise
		return None

	def save_as_project(self):
		try:
			self.new_project("Save As")
		except:
			raise
		return None

	def save_project(self):
		try:
			if self.event_file is 3:
				self.console_print("{} Saving".format(self.project.json["Name"]))
				self.event_file = 2

			elif self.event_file is 1:
				self.console_print("{} Saving".format(self.project.json["Name"]))
				self.event_file = 2

			self.project.json["Project Camera Pos"] = (self.camera_x, self.camera_y)
			self.project.save()
			self.console_print("{} Saved".format(self.project.json["Name"]))
		except:
			raise
		return None

	def load_sprite(self):
		try:
			find = filedialog.askopenfilename(initialdir = os.path.realpath(__file__), title = "Select file", filetypes = (
			(
				"files", "*.jpg *.png *.gif *.bmp *.pcx *.tga *.tif *.lbm *.pbm *.xpm"
			),
			(
				"all files", "*.*"
			)))

			if find:
				if self.camera is None:
					self.cameras[self.camera] = {}

				import random

				self.selected               = os.path.splitext(os.path.basename(find))[0] + str(random.randint(100, 1000))
				self.sprites[self.selected] = load_type([self.project, "load"], "Sprites", self.selected, self.jan_pygame, find, self, camera = self.camera)

				self.tool_tree_sprites.insert(
				"", "end",
				"Class Sprites {}".format(self.sprites[self.selected].tag),
				image = self.jan_tree.icone_00.photo,
				text  = " {}".format(self.sprites[self.selected].tag),
				open  = True)

				try:
					self.cameras[self.camera]["Class Objects {}".format(self.sprites[self.selected].tag)] = None
				except:
					self.cameras[self.camera] = {}
					self.cameras[self.camera]["Class Objects {}".format(self.sprites[self.selected].tag)] = None

				if self.project != None:
					self.selected   = None
					self.event_file = 3

				else:
					self.selected   = None
					self.event_file = 1

				self.pygame.display.update()
				self.jan_win.get_master().update()
		except:
			raise
		return None

	def load_object(self):
		try:
			find = filedialog.askopenfilename(initialdir = os.path.realpath(__file__), title = "Select file", filetypes = (
			(
				"files", "*.jpg *.png *.gif *.bmp *.pcx *.tga *.tif *.lbm *.pbm *.xpm"
			),
			(
				"all files", "*.*"
			)))

			if find:
				if self.camera is None:
					self.cameras[self.camera] = {}

				import random

				self.selected               = os.path.splitext(os.path.basename(find))[0] + str(random.randint(100, 1000))
				self.sprites[self.selected] = load_type([self.project, "load"], "Objects", self.selected, self.jan_pygame, find, self, camera = self.camera)

				self.tool_tree_objects.insert(
				"", "end",
				self.tool_tree_objects, "end",
				"Class Objects {}".format(self.sprites[self.selected].tag),
				image = self.jan_tree.icone_01.photo,
				text  = " {}".format(self.sprites[self.selected].tag),
				open  = True)

				self.cameras[self.camera]["Class Objects {}".format(self.sprites[self.selected].tag)] = None

				if self.project != None:
					self.selected   = None
					self.event_file = 3

				else:
					self.selected   = None
					self.event_file = 1

				self.pygame.display.update()
				self.jan_win.window.update()
		except:
			raise
		return None

	def clear(self):
		try:
			self.tool_tree.delete(*self.tool_tree.get_children())
			self.sprites = {}

			self.console_print("Work cleaned")

			self.pygame.display.update()
			self.jan_win.window.update()
		except:
			raise
		return None

	def ref_sprite(self, old = None, replace = None):
		try:
			if old == replace:
				pass

			else:					
				self.tool_tree.delete("Class {} {}".format(self.sprites[old].type, self.sprites[old].tag))

				self.sprites[replace] = self.sprites[old]
	
				del self.sprites[old]

				self.sprites[replace].tag = replace
				self.selected             = replace

				self.tool_tree.insert(
				self.tool_tree_sprites if self.sprites[self.selected].type is "Sprites" else self.tool_tree_objects,
				"end",
				"Class {} {}".format(self.sprites[self.selected].type, self.sprites[self.selected].tag),
				text = self.sprites[self.selected].tag,
				open = True)

				if self.project is not None:
					self.sprites[replace].do("replace", self.project, old)

			self.pygame.display.update()
			self.jan_win.window.update()
		except:
			raise
		return None

	def create_frame(self, id):
		try:
			os.environ["SDL_WINDOWID"] = str(id.winfo_id())
			os.environ['SDL_VIDEODRIVER'] = 'windib'

			self.content = self.pygame.HWSURFACE | self.pygame.DOUBLEBUF

			self.pygame.init()

			self.jan_pygame        = self.pygame.display.set_mode((id.winfo_screenwidth(), id.winfo_screenheight()), self.content)
			self.jan_editor_status = JanGui.create_status(id, (self.camera_x, self.camera_y))

			self.pygame.display.update()
			self.jan_win.window.update()
		except:
			raise
		return None

	def dynamic_popup(self, event):
		try:
			if not self.some_selected:
				if event.type is self.pygame.MOUSEBUTTONUP and event.button is 3:
					self.create_file_tool_menu()

					#pygame.display.update()
					#self.jan_win.window.update()
		except:
			raise
		return None

	def create_file_tool_menu(self):
		try:
			try:
				self.jan_menu.get("Main").post(self.x_main, self.y_main)
			finally:
				self.jan_menu.get("Main").grab_release()
		except:
			raise
		return None

	def create_event_menu(self, event):
		try:
			try:
				self.jan_menu.get("Events").post(event.x_root, event.y_root)
			finally:
				self.jan_menu.get("Events").grab_release()
		except:
			raise
		return None

	def create_selected_sprite_menu(self):
		try:
			try:
				self.jan_menu.get("MainSprite").post(self.x_main, self.y_main)
			finally:
				self.jan_menu.get("MainSprite").grab_release()
		except:
			raise
		return None

	def poop_up(self):
		try:
			self.jan_container.frame_event_game.bind("<Button-3>", self.create_event_menu)
		except:
			raise
		return None

	def background_(self, img):
		try:
			import io
			import base64
			return self.jan_pygame.blit(self.pygame.transform.scale(self.pygame.image.load(io.BytesIO(base64.b64decode(img))), (self.jan_pygame.get_size())), (0, 0))
		except:
			raise
		return None

	def set_title(self, title):
		try:
			return self.jan_win.window.title(title)
		except:
			raise
		return None

	def create_widget(self):
		try:
			self.jan_frame_tools = JanGui.create_frame_tools(self.jan_win.get_master())
			self.jan_menu        = JanGui.create_menu(self.jan_win.get_master(),
			(
				# Main container and Events container
				self.new_project, self.open_project, self.save_project, self.save_as_project, self.load_sprite, self.load_object, None,
				None, None, self.close, None, None, None, None, None
			),
			(
				self.delete_selected_sprite, None, None, None, None
			)
			)

			self.jan_container   = JanGui.create_container(self.jan_win.get_master(), self.jan_frame_tools.resize, "Container Developer")
			self.jan_debug_tools = JanGui.frame_debug_tools(self.jan_win.get_master(), self.jan_frame_tools.resize, self.jan_container)
			
			self.jan_frame_tools.resize_config([self.jan_container.container, self.jan_container.resize_height], self.jan_debug_tools)
			self.jan_container.resize_config(self.jan_debug_tools.frame)

			self.jan_status = JanGui.create_status(self.jan_win.get_master(), "JanJaEngine")
			self.jan_tree   = JanGui.create_object_tree_view(self.jan_frame_tools,
				replace_folder("/_JanJa.py", "/splash/icone_00.png"),
				replace_folder("/_JanJa.py", "/splash/icone_01.png"),
				replace_folder("/_JanJa.py", "/splash/icone_02.png"))

			self.jan_tree.create_class()

			self.tool_tree          = self.jan_tree
			self.tool_tree_sprites = self.jan_tree.tree_sprites
			self.tool_tree_objects = self.jan_tree.tree_objects
			self.tool_tree_cameras = self.jan_tree.tree_cameras
			self.tool_tree         = self.jan_tree
			self.tool_tree_sprites = self.jan_tree.tree_sprites
			self.tool_tree_objects = self.jan_tree.tree_objects
			self.tool_tree_cameras = self.jan_tree.tree_cameras

			self.jan_sprite_options = JanGui.sprite_options(self.jan_win.window, self.jan_frame_tools, self.sprites, self.selected, self.tool_tree)

			self.jan_debug_tools.create_debug_buttons(
				replace_folder("/_JanJa.py", "/splash/icone_debug_00.png"),
				replace_folder("/_JanJa.py", "/splash/icone_debug_01.png"),
				replace_folder("/_JanJa.py", "/splash/icone_debug_02.png"))

			self.debug_state = self.jan_debug_tools.set_state

			self.debug_state("play", "normal")

			self.jan_console_debug = JanGui.console_debug(self.jan_debug_tools.frame, self.jan_win.get_master())

			self.console_print("WKs Jan Studio")
		except:
			raise
		return None

	def console_print(self, item):
		try:
			return self.jan_console_debug.ENGINE_PROCESS_PRINT_FROM_CONSOLE(item)
		except:
			raise
		return None

	def close(self):
		try:
			if not JAN_ENGINE_engine.get("Devolper") is False:
				self.JanRun = False; self.jan_win.close(); os.startfile(replace_folder("data/_JanJa.py", "run.cmd"))

			elif not JAN_ENGINE_engine.get("Devolper") is True:
				if self.jan_win.askExit("Do you want to quit?"):
					self.JanRun = False; self.jan_win.close(); sys.exit()
		except:
			raise
		return None

	def refresh(self):
		try:
			for sprites in self.sprites.values():
				sprites.render(self.camera_x, self.camera_y)
		except:
			pass
		return None

	def window_loop(self):
		try:
			self.jan_win.get_master().protocol("WM_DELETE_WINDOW", self.close)
			self.jan_win.get_master().mainloop()
		except:
			raise
		return None

if True:
	JanGui.start_(
	replace_folder("/_JanJa.py", "/splash/logo_00.png"), # Splash test.
	
	DAT, # DAT import.
	hardware_res, # Hardware resolution.
	JanMath, # Prcessing maths.

	json    = JAN_ENGINE_engine, # Json engine - no working.
	version = "Alpha 0.2.2.5" # Verision of engine.
	)