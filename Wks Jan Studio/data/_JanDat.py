from _JanJa import pygame
from _JanJa import sys
from _JanJa import os

from _JanJa import JanGui
from _JanJa import JanFrame

from _JanJa import JAN_ENGINE_engine
from _JanJa import replace_folder

from JanPort import filedialog
from JanPort import JanMath

from JanPort import JanBools

int_engine = lambda _int: int(JAN_ENGINE_engine.get(_int))

class load(object):
	def __init__(self, master, path):
		try:
			self.tag     = str(os.path.basename(path))
			self.img     = pygame.image.load(path)
			self.rect    = self.img.get_rect()
			self.effect_ = pygame.Surface((self.rect.w, self.rect.h), pygame.SRCALPHA)
			self.effect_.fill((255, 0, 0, 50))

			self.master    = master
			self.move      = False
			self.rendering = True
			self.selected  = False
		except:
			raise
		return None

	def do(self, type):
		try:
			if (type) is ("delete"):
				self.img     = None
				self.rect    = None
				self.effect_ = None
				self.master  = None
				self.tag     = ("deleted")

				self.move      = False
				self.rendering = False
				self.selected  = False

			elif (type) is ("select"):
				self.selected = True

			elif (type) is ("dselect"):
				self.selected = False

			elif (type) is ("move"):
				self.move = True

			elif (type) is ("dmove"):
				self.move = False

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

					self.master.blit(self.effect_, (self.rect.x, self.rect.y))
		except:
			raise
		return None

class DAT:
	def __init__(self):
		try:
			self.JanWin = JanGui.create_window(int_engine("Width"), int_engine("Height"), "JanJaEngine", "Gray")

			self.selected_pos_sprites = None
			self.some_selected        = False
			self.selected_now         = None
			self.selected             = None
			self.sprites              = {}

			self.JanContainer = JanGui.create_container(self.JanWin.get_master())	
			self.JanStatus    = JanGui.create_status(self.JanWin.get_master(), "JanJaEngine")
			self.JanMenu      = JanGui.create_menu(self.JanWin.get_master(),
			(
				# Main container and Events container	
				None, None, None, self.load_image, None, None, None,
				None, self.close, None, None, None, None, None,
			),
			(
				self.delete_selected, None, None, None, None
			)
			)

			self.x_main, self.y_main = (self.JanWin.get_master().winfo_pointerx() - self.JanWin.get_master().winfo_vrootx(),
										self.JanWin.get_master().winfo_pointery() - self.JanWin.get_master().winfo_vrooty())

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

				self.up_mouse_event()
				self.poop_up()

				for sprites in self.sprites.values():
					sprites.render()

				self.window_loop()
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
								if self.selected != None:
									self.sprites[self.selected].selected = False
									self.sprites[self.selected].move     = False

									self.selected = sprite_selected.tag

									self.sprites[self.selected].selected = True
									self.sprites[self.selected].move     = True

									self.some_selected = True

								elif self.selected is None:
									self.selected = sprite_selected.tag

									self.sprites[self.selected].selected = True
									self.sprites[self.selected].move     = True

									self.some_selected = True

							elif not self.sprites[self.selected].rect.collidepoint(event.pos):
								if self.selected != None:
									self.sprites[self.selected].selected = False
									self.sprites[self.selected].move     = False

									self.selected      = None
									self.some_selected = False

								elif self.selected is None:
									self.selected      = None
									self.some_selected = False
						except:
							pass
	
					if event.button is 3:
						try:						
							if self.sprites[self.selected].selected:
								self.create_selected_sprite_menu()
						except:
							pass

			if event.type is pygame.MOUSEBUTTONUP:
				if event.button is 1:
					try:
						self.sprites[self.selected].move = False
					except:
						pass

			if event.type is pygame.KEYUP:
				if event.key is pygame.K_DELETE:
					try:
						self.sprites[self.selected].do("delete")
						self.some_selected = False
						self.selected = None
					except:
						pass

			if event.type is pygame.KEYDOWN:
				if event.key is pygame.K_LCTRL and pygame.key.get_mods() & pygame.K_w:
					print("Print")
		except:
			raise
		return None

	def delete_selected(self):
		try:
			self.sprites[self.selected].do("delete")
			self.some_selected = False
			self.selected = None
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

	def up_mouse_event(self):
		try:
			self.x_main, self.y_main = (self.JanWin.get_master().winfo_pointerx() - self.JanWin.get_master().winfo_vrootx(),
										self.JanWin.get_master().winfo_pointery() - self.JanWin.get_master().winfo_vrooty())

			self.JanStatus.set_text("{}{} {}".format(
				"" if self.selected is None else self.selected, 
				pygame.mouse.get_pos() if self.selected is None else " %d" % self.sprites[self.selected].rect.x,
				"" if self.selected is None else self.sprites[self.selected].rect.y)
			)
		except:
			raise
		return None

	def load_image(self):
		try:
			find = filedialog.askopenfilename(initialdir = os.path.realpath(__file__), title = "Select file", filetypes = (
			(
				"files", "*.jpg *.png *.gif *.bmp *.pcx *.tga *.tif *.lbm *.pbm *.xpm"
			),
			(
				"all files", "*.*"
			)))

			if find:
				self.sprites[os.path.basename(find)] = load(self.JanPygame, find)

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

	def window_loop(self):
		try:			
			self.JanWin.get_master().protocol("WM_DELETE_WINDOW", self.close)

			pygame.display.flip()			
			self.JanWin.get_master().update()
		except:
			raise
		return None

if __name__ is "__main__":
	DAT()
else:
	DAT()
	