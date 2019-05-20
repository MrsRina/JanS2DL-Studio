from _JanJa import pygame
from _JanJa import sys
from _JanJa import os

from _JanJa import JanGui
from _JanJa import hardware_res

from _JanJa import JAN_ENGINE_engine
from _JanJa import replace_folder
from _JanJa import replace

from JanPort import filedialog
from JanPort import JanMath
from JanPort import tk

int_engine = lambda _int: int(JAN_ENGINE_engine.get(_int))

class load_type(object):
	def __init__(self, type, tag, master, path):
		try:
			self.type    = type
			self.path    = path
			self.tag     = tag
			self.img     = pygame.image.load(self.path)
			self.rect    = self.img.get_rect()

			self.master    = master
			self.move      = False
			self.resize    = False
			self.rotate    = False
			self.rendering = True
			self.selected  = False
		except:
			raise
		return None

	def do(self, type):
		try:
			if (type) is ("delete"):
				self.path    = None
				self.img     = None
				self.rect    = None
				self.effect_ = None
				self.master  = None
				self.tag     = ("deleted")

				self.move      = False
				self.resize    = False
				self.rotate    = False
				self.rendering = False
				self.selected  = False
		except:
			raise
		return None

	def render(self):
		try:
			if self.rendering:
				self.master.blit(self.img, (self.rect.x, self.rect.y))

				if self.selected:
					if self.move:
						self.rect.center = pygame.mouse.get_pos()

					if self.rotate:
						pass

					if self.resize:
						self.rect.w, self.rect.h = pygame.mouse.get_pos()
						
						self.img = pygame.transform.scale(pygame.image.load(self.path), (self.rect.w, self.rect.h))

						pygame.display.flip()

					self.effect_ = pygame.Surface((self.rect.w, self.rect.h), pygame.SRCALPHA)
					self.effect_.fill((255, 0, 0, 50))

					self.master.blit(self.effect_, self.rect)
		except:
			raise
		return None

class DAT:
	def __init__(self):
		try:
			self.JanWin = JanGui.create_window(int_engine("Width"), int_engine("Height"), "JanCreate Studio", "Gray",
				r"{}".format(replace_folder("/_JanJa.py", "/icone.ico")))

			self.bool_click           = 0

			self.tread_load           = False
			self.some_selected        = False
			self.bool_tool_tree       = False

			self.selected_pos_sprites = None
			self.selected_tree_view   = None
			self.selected_now         = None
			self.selected             = None
			self.sprites              = {}

			self.create_widget()

			self.x_main, self.y_main = JanMath.Sync_Resolution_Pos(self.JanWin.get_master())

			self.JanRun = True

			self.JanWidthPygame  = 1024
			self.JanHeightPygame = 768

			self.JanBackgroundColorPygame = (127, 127, 127, 0)

			self.create_frame(self.JanContainer.get_id())
			
			self.Tick_Fps = pygame.time.Clock()

			while (self.JanRun):
				self.Tick_Fps.tick(102)
				self.JanPygame.fill((self.JanBackgroundColorPygame))

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
								self.some_selected  = False
								self.selected       = None

							elif self.selected != None:
								self.sprites[self.selected].selected = False
								self.bool_tool_tree                  = False
								self.some_selected                   = False
								self.selected                        = None
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
										
										self.bool_tool_tree = False
										self.selected       = None
										self.some_selected  = False

										self.JanWin.get_master().update()

									else:
										self.tool_tree.selection_remove("Class {} {}".format(self.sprites[self.selected].type, self.sprites[self.selected].tag))
										self.tool_tree.item("Class {} {}".format(self.sprites[self.selected].type, self.sprites[self.selected].tag), open = False)

										self.JanSpriteOptions.up = False

										self.bool_tool_tree = False
										self.selected       = None
										self.some_selected  = False

										self.JanWin.get_master().update()
						except:
							pass
	
					if event.button is 3:
						try:
							if self.sprites[self.selected].type is ("Sprites"):
								if self.sprites[self.selected].selected:
									self.create_selected_sprite_menu()

							elif self.sprites[self.selected].type is ("Objects"):
								if self.sprites[self.selected].selected:
									pass
						except:
							pass

					if event.button is 2:
						try:
							self.sprites[self.selected].resize = True
						except:
							pass

			if event.type is pygame.MOUSEBUTTONUP:
				if event.button is 1:
					try:
						if self.sprites[self.selected].selected:
							self.sprites[self.selected].move = False
					except:
						pass

				if event.button is 2:
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
			pass
		return None

	def remove(self, x):
		try:
			if (x) is ("sprite"):
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

			self.x_main, self.y_main = JanMath.Sync_Resolution_Pos(self.JanWin.get_master())

			self.JanSpriteOptions.show(self.tool_tree, self.sprites, self.selected, up = self.bool_tool_tree)

			try:
				self.JanStatus.set_text("{}{} {} {} {}".format(
					"" if self.selected is None else self.selected, 
					pygame.mouse.get_pos() if self.selected is None else " %d" % self.sprites[self.selected].rect.x,
					"" if self.selected is None else self.sprites[self.selected].rect.y,
					"" if self.selected is None else self.sprites[self.selected].rect.w,
					"" if self.selected is None else self.sprites[self.selected].rect.h)
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

				self.selected = os.path.splitext(os.path.basename(find))[0] + str(random.randint(100, 1000))
				self.sprites[self.selected] = load_type("Sprites", self.selected, self.JanPygame, find)
				
				self.tool_tree.insert(
				self.tool_tree_sprites, "end",
				"Class Sprites {}".format(self.sprites[self.selected].tag),
				text = self.sprites[self.selected].tag,
				open = True)

				self.selected = None
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

				self.selected = os.path.splitext(os.path.basename(find))[0] + str(random.randint(100, 1000))
				self.sprites[self.selected] = load_type("Objects", self.selected, self.JanPygame, find)

				self.tool_tree.insert(
				self.tool_tree_objects, "end",
				"Class Objects {}".format(self.sprites[self.selected].tag),
				text = self.sprites[self.selected].tag,
				open = True)

				self.selected = None
				pygame.display.update()
				self.JanWin.get_master().update()
		except:
			raise
		return None

	def create_frame(self, id):
		try:
			os.environ["SDL_WINDOWID"] = str(id.winfo_id())
			os.environ['SDL_VIDEODRIVER'] = 'windib'

			pygame.init()

			self.JanPygame = pygame.display.set_mode((id.winfo_screenwidth(), id.winfo_screenheight()), pygame.DOUBLEBUF)
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

	def create_widget(self):
		try:
			self.JanFrameTools = JanGui.create_frame_tools(self.JanWin.get_master())
			self.JanContainer  = JanGui.create_container(self.JanWin.get_master(), self.JanFrameTools.resize, "Container Developer")
			self.JanFrameTools.resize_config(self.JanContainer.container)
			self.JanStatus     = JanGui.create_status(self.JanWin.get_master(), "JanJaEngine")
			self.JanMenu       = JanGui.create_menu(self.JanWin.get_master(),
			(
				# Main container and Events container	
				None, None, None, self.load_sprite, self.load_object, None, None,
				None, self.close, None, None, None, None, None,
			),
			(
				self.delete_selected_sprite, None, None, None, None
			)
			)

			self.JanTree = JanGui.create_object_tree_view(self.JanFrameTools,
				replace_folder("/_JanJa.py", "/splash/icone_00.png"),
				replace_folder("/_JanJa.py", "/splash/icone_01.png"),
				replace_folder("/_JanJa.py", "/splash/icone_02.png"))

			self.tool_tree         = self.JanTree.tree
			self.tool_tree_sprites = self.JanTree.sprites
			self.tool_tree_objects = self.JanTree.objects
			self.tool_tree_cameras = self.JanTree.cameras

			self.JanSpriteOptions = JanGui.sprite_options(self.JanWin.window, self.JanFrameTools, self.sprites, self.selected, self.tool_tree)
		except:
			raise
		return None

	def close(self):
		try:
			if not JAN_ENGINE_engine.get("Devolper") is (False):
				self.JanRun = False; self.JanWin.close(); os.startfile(replace_folder("data/_JanJa.py", "run.cmd"))

			elif not JAN_ENGINE_engine.get("Devolper") is (True):
				if self.JanWin.askExit("Do you want to quit?"):
					self.JanRun = False; self.JanWin.close(); sys.exit()
		except:
			raise
		return None

	def refresh(self):
		try:
			for sprites in self.sprites.values():
				sprites.render()

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
	JanGui.start_(replace_folder("/_JanJa.py", "/splash/logo_00.png"), DAT)
else:
	JanGui.start_(replace_folder("/_JanJa.py", "/splash/logo_00.png"), DAT, hardware_res, JanMath,
	json    = JAN_ENGINE_engine,
	version = "Alpha 0.1.6"
	)