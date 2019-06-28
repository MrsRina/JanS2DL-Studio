from _JanJa  import *
from JanPort import JanCompiler, JanConsoleText, JanDecode

int_engine = lambda _int: int(JAN_ENGINE_engine.get(_int))

class DAT:
	def __init__(self):
		try:
			self.JanWin = JanGui.create_window(int_engine("Width"), int_engine("Height"), "JanS2DL-Studio", "Gray",
				r"{}".format(replace_folder("/_JanJa.py", "/icone.ico")))

			self.bool_click     = 0
			self.tread_load     = False
			self.some_selected  = False
			self.bool_tool_tree = False

			self.selected_pos_sprites = None
			self.selected_tree_view   = None
			self.selected_now         = None
			self.selected             = None
			self.sprites              = {}

			self.camera_x = 0
			self.camera_y = 0

			self.project         = None
			self.event_file      = 0
			self.new_folder_path = None

			self.create_widget()

			self.x_main, self.y_main = JanMath.Sync_Resolution_Pos(self.JanWin.get_master())

			self.JanRun = True

			self.JanWidthPygame  = 1024
			self.JanHeightPygame = 768

			self.JanBackgroundColorPygame = (127, 127, 127, 0)

			self.create_frame(self.JanContainer.get_id())

			self.Tick_Fps = pygame.time.Clock()

			while self.JanRun:
				self.JanPygame.fill((self.JanBackgroundColorPygame))
				self.background_(JanDecode.JAN_IMAGE_DECODE_ALPHA)
				
				for event_ in pygame.event.get():
					self.events_sprite(event_)
					self.dynamic_popup(event_)

				self.up_events()

				self.refresh()
				self.window_loop()
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
		except:
			raise
		return None

	def events_sprite(self, event):
		try:
			if event.type is pygame.MOUSEBUTTONDOWN:
				for sprite_selected in self.sprites.values():
					if event.button is 1:
						try:
							if sprite_selected.rect.collidepoint(event.pos):
								if self.bool_click is 0:
									self.bool_click = 0.1

								elif self.bool_click <= 1.5:
									if self.selected != None:
										self.handling_cmouse = False

										self.sprites[self.selected].selected = False
										self.sprites[self.selected].move     = False
										self.selected = sprite_selected.tag

										self.sprites[self.selected].selected = True
										self.sprites[self.selected].move     = True

										self.bool_tool_tree = True
										self.some_selected  = True

										self.JanSpriteOptions.up = True

										self.tool_tree.item("Class {} {}".format(self.sprites[self.selected].type, self.sprites[self.selected].tag), open = True)
										self.tool_tree.selection_set("Class {} {}".format(self.sprites[self.selected].type, self.sprites[self.selected].tag))
										self.tool_tree.focus_set()
										self.tool_tree.focus("Class {} {}".format(self.sprites[self.selected].type, self.sprites[self.selected].tag))

										self.JanWin.get_master().update()

									elif self.selected is None:
										self.handling_cmouse = False

										self.selected = sprite_selected.tag

										self.sprites[self.selected].selected = True
										self.sprites[self.selected].move     = True

										self.JanSpriteOptions.up = True

										self.bool_tool_tree = True
										self.some_selected  = True

										self.tool_tree.item("Class {} {}".format(self.sprites[self.selected].type, self.sprites[self.selected].tag), open = True)
										self.tool_tree.selection_set("Class {} {}".format(self.sprites[self.selected].type, self.sprites[self.selected].tag))
										self.tool_tree.focus_set()
										self.tool_tree.focus("Class {} {}".format(self.sprites[self.selected].type, self.sprites[self.selected].tag))

										self.JanWin.get_master().update()
						except:
							pass

					if event.button is 1:
						try:
							if self.sprites[self.selected].selected:
								if self.sprites[self.selected].rect.collidepoint(event.pos):
									self.sprites[self.selected].move = True

								elif not self.sprites[self.selected].rect.collidepoint(event.pos):
									if self.selected != None:
										self.tool_tree.selection_remove("Class {} {}".format(self.sprites[self.selected].type, self.sprites[self.selected].tag))
										self.tool_tree.item("Class {} {}".format(self.sprites[self.selected].type, self.sprites[self.selected].tag), open = False)

										self.sprites[self.selected].selected = False
										self.sprites[self.selected].move     = False

										self.JanSpriteOptions.up = False

										self.bool_tool_tree  = False
										self.selected        = None
										self.some_selected   = False

										self.JanWin.get_master().update()

									else:
										self.tool_tree.selection_remove("Class {} {}".format(self.sprites[self.selected].type, self.sprites[self.selected].tag))
										self.tool_tree.item("Class {} {}".format(self.sprites[self.selected].type, self.sprites[self.selected].tag), open = False)

										self.JanSpriteOptions.up = False

										self.bool_tool_tree  = False
										self.selected        = None
										self.some_selected   = False

										self.JanWin.get_master().update()
						except:
							pass

					if event.button is 2:
						try:
							if self.sprites[self.selected].selected:
								self.sprites[self.selected].resize = True
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

			pygame.display.flip()
			self.JanWin.get_master().update()
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
			self.events_select_tree()
			self.poop_up()

			self.JanContainer.container.configure(width = self.JanWin.get("Width"), height = self.JanWin.get("Height"))
			self.JanTree.up(self.bool_tool_tree)
			self.JanConsoleDebug.up()

			self.tool_tree.heading("#0", text = "..." if self.project is None else self.project.json["Name"])

			self.JanMenu.menu_file_tools.entryconfig(2, state = JanMath.Sync_File(self.event_file))
			self.JanMenu.menu_file_tools.entryconfig(3, state = JanMath.Sync_File_As(self.event_file))

			self.x_main, self.y_main = JanMath.Sync_Resolution_Pos(self.JanWin.get_master())

			self.JanSpriteOptions.show(self.sprites, self.selected, ref = self.ref_sprite, up = self.bool_tool_tree)

			try:
				self.JanStatus.set_text("{} {}{} {} {} {} {}".format(
					"" if self.project is None else self.project.local,
					"" if self.selected is None else self.selected,
					pygame.mouse.get_pos() if self.selected is None else " ",
					"" if self.selected is None else self.sprites[self.selected].x,
					"" if self.selected is None else self.sprites[self.selected].y,
					"" if self.selected is None else self.sprites[self.selected].w,
					"" if self.selected is None else self.sprites[self.selected].h)
				)

				self.JanEditorStatus.set_text("{} x {}".format(
					self.camera_x, self.camera_y
					))
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
			if self.cache_project_name.get(1.0, tk.INSERT) != "":
				try:
					self.project = JanCompiler.create_project(
					local    = self.new_folder_path,
					name     = self.cache_project_name.get(1.0, tk.INSERT),
					camera   = (self.camera_x, self.camera_y),
					comments = self.cache_project_comment.get(1.0, tk.INSERT),
					version  = "1.3"
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

					self.JanWin.get_master().update()

				except:
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
 
					self.JanWin.get_master().update()
			else:
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

				self.JanWin.get_master().update()
		except:
			raise
		return None

	def cancel_new_project(self):
		try:
			self.new_folder_path = None
			self.some_selected   = False
			self.cache_project_window.destroy()

			self.JanWin.get_master().update()
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

				project_window = JanGui.project_window(self.JanWin.get_master(), self.create_new_project, self.cancel_new_project)

				self.cache_project_window  = project_window
				self.cache_project_name    = project_window.text_name_project_
				self.cache_project_width   = project_window.text_widht_project_
				self.cache_project_height  = project_window.text_height_project_
				self.cache_project_comment = project_window.text_comment_project_

				project_window.tought_loop()

				self.JanWin.get_master().update()
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
	
							self.sprites[self.selected] = load_type([self.project, "project_load"], master = self.JanPygame, state = self,
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
	
							self.sprites[self.selected] = load_type([self.project, "project_load"], master = self.JanPygame, state = self,
							tag = objects.replace("Class Objects ", ""), type = "Objects", cam_x = self.camera_x, cam_y = self.camera_y)
	
							self.tool_tree.insert(
							self.tool_tree_objects, "end",
							"Class Objects {}".format(self.sprites[self.selected].tag),
							text = self.sprites[self.selected].tag,
							open = True)
	
							self.selected = None

					self.console_print(JanConsoleText.print_load_project(self.project.json))
				except:
					self.console_print("This file corrupted or old version ... \n{}".format(find))
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
				import random

				self.selected               = os.path.splitext(os.path.basename(find))[0] + str(random.randint(100, 1000))
				self.sprites[self.selected] = load_type([self.project, "load"], "Sprites", self.selected, self.JanPygame, find, self)

				self.tool_tree.insert(
				self.tool_tree_sprites, "end",
				"Class Sprites {}".format(self.sprites[self.selected].tag),
				text = self.sprites[self.selected].tag,
				open = True)

				if self.project != None:
					self.selected   = None
					self.event_file = 3

				else:
					self.selected   = None
					self.event_file = 1

				pygame.display.update()
				self.JanWin.get_master().update()
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
				import random

				self.selected               = os.path.splitext(os.path.basename(find))[0] + str(random.randint(100, 1000))
				self.sprites[self.selected] = load_type([self.project, "load"], "Objects", self.selected, self.JanPygame, find, self)

				self.tool_tree.insert(
				self.tool_tree_objects, "end",
				"Class Objects {}".format(self.sprites[self.selected].tag),
				text = self.sprites[self.selected].tag,
				open = True)

				if self.project != None:
					self.selected   = None
					self.event_file = 3

				else:
					self.selected   = None
					self.event_file = 1

				pygame.display.update()
				self.JanWin.get_master().update()
		except:
			raise
		return None

	def clear(self):
		try:
			self.tool_tree.delete(*self.tool_tree.get_children())
			self.sprites = {}

			self.console_print("Work cleaned")
		except:
			raise
		return None

	def ref_sprite(self, old = None, replace = None):
		try:
			if old is replace:
				pass

			else:
				self.tool_tree.delete("Class {} {}".format(self.sprites[old].type, self.sprites[old].tag))

				self.sprites[old].tag = replace
				self.sprites[replace] = self.sprites[old]
	
				del self.sprites[old]
	
				self.selected = replace

				self.tool_tree.insert(
				self.tool_tree_sprites if self.sprites[self.selected].type is "Sprites" else self.tool_tree_objects,
				"end",
				"Class {} {}".format(self.sprites[self.selected].type, self.sprites[self.selected].tag),
				text = self.sprites[self.selected].tag,
				open = True)
		except:
			raise
		return None

	def create_frame(self, id):
		try:
			os.environ["SDL_WINDOWID"] = str(id.winfo_id())
			os.environ['SDL_VIDEODRIVER'] = 'windib'

			pygame.init()

			self.JanPygame = pygame.display.set_mode((id.winfo_screenwidth(), id.winfo_screenheight()), pygame.DOUBLEBUF)

			self.JanEditorStatus = JanGui.create_status(id, (self.camera_x, self.camera_y))
		except:
			raise
		return None

	def dynamic_popup(self, event):
		try:
			if not self.some_selected:
				if event.type is pygame.MOUSEBUTTONUP and event.button is 3:
					self.create_file_tool_menu()

					pygame.display.update()
					self.JanWin.get_master().update()
		except:
			raise
		return None

	def create_file_tool_menu(self):
		try:
			try:
				self.JanMenu.get("Main").tk_popup(self.x_main, self.y_main, 0)
			finally:
				self.JanMenu.get("Main").grab_release()
		except:
			raise
		return None

	def create_event_menu(self, event):
		try:
			try:
				self.JanMenu.get("Events").tk_popup(event.x_root, event.y_root, 0)
			finally:
				self.JanMenu.get("Events").grab_release()
		except:
			raise
		return None

	def create_selected_sprite_menu(self):
		try:
			try:
				self.JanMenu.get("MainSprite").tk_popup(self.x_main, self.y_main, 0)
			finally:
				self.JanMenu.get("MainSprite").grab_release()
		except:
			raise
		return None

	def poop_up(self):
		try:
			self.JanContainer.frame_event_game.bind("<Button-3>", self.create_event_menu)
		except:
			raise
		return None

	def background_(self, img):
		try:
			import io
			import base64
			return self.JanPygame.blit(pygame.transform.scale(pygame.image.load(io.BytesIO(base64.b64decode(img))), (self.JanPygame.get_size())), (0, 0))
		except:
			raise
		return None

	def create_widget(self):
		try:
			self.JanFrameTools = JanGui.create_frame_tools(self.JanWin.get_master())
			self.JanMenu       = JanGui.create_menu(self.JanWin.get_master(),
			(
				# Main container and Events container
				self.new_project, self.open_project, self.save_project, self.save_as_project, self.load_sprite, self.load_object, None,
				None, None, self.close, None, None, None, None, None
			),
			(
				self.delete_selected_sprite, None, None, None, None
			)
			)

			self.JanContainer  = JanGui.create_container(self.JanWin.get_master(), self.JanFrameTools.resize, "Container Developer")

			self.JanDebugTools = JanGui.frame_debug_tools(self.JanWin.get_master(), self.JanFrameTools.resize, self.JanContainer)
			
			self.JanFrameTools.resize_config([self.JanContainer.container, self.JanContainer.resize_height], self.JanDebugTools)
			self.JanContainer.resize_config(self.JanDebugTools.frame)

			self.JanStatus = JanGui.create_status(self.JanWin.get_master(), "JanJaEngine")

			self.JanTree = JanGui.create_object_tree_view(self.JanFrameTools,
				replace_folder("/_JanJa.py", "/splash/icone_00.png"),
				replace_folder("/_JanJa.py", "/splash/icone_01.png"),
				replace_folder("/_JanJa.py", "/splash/icone_02.png"))

			self.JanTree.create_class()

			self.tool_tree         = self.JanTree.tree
			self.tool_tree_sprites = self.JanTree.sprites
			self.tool_tree_objects = self.JanTree.objects
			self.tool_tree_cameras = self.JanTree.cameras

			self.JanSpriteOptions = JanGui.sprite_options(self.JanWin.window, self.JanFrameTools, self.sprites, self.selected, self.tool_tree)

			self.JanConsoleDebug = JanGui.console_debug(self.JanDebugTools.frame, self.JanWin.get_master())

			self.console_print("WKs Jan Studio")
		except:
			raise
		return None

	def console_print(self, item):
		try:
			return self.JanConsoleDebug.ENGINE_PROCESS_PRINT_FROM_CONSOLE(item)
		except:
			raise
		return None

	def close(self):
		try:
			if not JAN_ENGINE_engine.get("Devolper") is False:
				self.JanRun = False; self.JanWin.close(); os.startfile(replace_folder("data/_JanJa.py", "run.cmd"))

			elif not JAN_ENGINE_engine.get("Devolper") is True:
				if self.JanWin.askExit("Do you want to quit?"):
					self.JanRun = False; self.JanWin.close(); sys.exit()
		except:
			raise
		return None

	def refresh(self):
		try:
			for sprites in self.sprites.values():
				sprites.render(self.camera_x, self.camera_y)

		except:
			raise
		return None

	def window_loop(self):
		try:
			self.JanWin.get_master().protocol("WM_DELETE_WINDOW", self.close)

			pygame.display.flip()
			self.JanWin.get_master().update()
		except:
			raise
		return None

if __name__ is "__main__":
	JanGui.start_(replace_folder("/_JanJa.py", "/splash/logo_00.png"), DAT, hardware_res, JanMath,

json    = JAN_ENGINE_engine,
version = "Alpha 0.2.2"
)

else:
	JanGui.start_(replace_folder("/_JanJa.py", "/splash/logo_00.png"), DAT, hardware_res, JanMath,

json    = JAN_ENGINE_engine,
version = "Alpha 0.2.2"

)