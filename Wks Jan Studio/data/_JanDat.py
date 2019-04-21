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

			self.delete_function = None
		except:
			raise
		return None

	def render(self):
		try:
			if self.rendering:
				if self.move:
					self.rect.center = pygame.mouse.get_pos()

				self.master.blit(self.img, (self.rect.x, self.rect.y))

				if self.selected:
					key = pygame.key.get_pressed()

					if key[pygame.K_DELETE]: self.delete_function()

					self.master.blit(self.effect_, (self.rect.x, self.rect.y))
		except:
			raise
		return None

class DAT:
	def __init__(self):
		try:
			self.JanWin = JanGui.create_window(int_engine("Width"), int_engine("Height"), "JanJaEngine", "Gray")

			self.selected = "None"
			self.sprites  = {}

			self.some_not_selected = True
			self.selected_type = "None"

			self.JanContainer = JanGui.create_container(self.JanWin.get_master())	
			self.JanMenu      = JanGui.create_menu(self.JanWin.get_master(),
			(
				# Main container and Events container	
				None, None, None, self.load_image, None, None, None,
				None, self.close, None, None, None, None, None,
			),
			(
				JanBools.remove(self.sprites, self.selected), None
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
				self.Tick_Fps.tick(75)
				self.JanPygame.fill((self.JanBackgroundColorPygame))

				for event_ in pygame.event.get():
					self.images_select(event_)

					self.dynamic_popup(event_)

				self.up_mouse_popup_event()
				self.poop_up()

				for sprites in self.sprites.values():
					sprites.render()

			#print(self.selected_type, self.selected, self.some_not_selected)

				self.window_loop()
		except:
			raise
		return None

	def selected_some(self):
		try:
			self.some_not_selected = False
		except:
			raise
		return None

	def no_selected_some(self):
		try:
			self.some_not_selected = True
		except:
			raise
		return None

	def images_select(self, event):
		try:
			global sprites

			for sprites in self.sprites.values():

				def delete_sprite():
					sprites.selected  = False
					sprites.rendering = False

					del self.sprites[self.selected]

				if event.type is pygame.MOUSEBUTTONDOWN and event.button is 1:
					try:
						x, y = event.pos
						if sprites.rect.collidepoint(x, y):
							sprites.selected = True
							sprites.move     = True

							sprites.delete_function = delete_sprite

							print(sprites.tag)

							self.selected_some()
							self.selected_type = "Sprite"
							self.selected = sprites.tag
	
						if not sprites.rect.collidepoint(x, y):
							sprites.selected = False

							self.no_selected_some()
							self.selected_type = "None"
							self.selected = "None"

					except:
						raise
	
				if event.type is pygame.MOUSEBUTTONUP:
					sprites.move = False
		except:
			raise
		return None

	def up_mouse_popup_event(self):
		try:
			self.x_main, self.y_main = (self.JanWin.get_master().winfo_pointerx() - self.JanWin.get_master().winfo_vrootx(),
										self.JanWin.get_master().winfo_pointery() - self.JanWin.get_master().winfo_vrooty())
		except:
			raise
		return None

	def find(self):
		try:
			return filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (
			(
				"files", "*.jpg *.png *.gif *.bmp *.pcx *.tga *.tif *.lbm *.pbm *.xpm"
			),
			(
				"all files", "*.*"
			)))
		except:
			raise
		return None

	def load_image(self):
		try:
			find = self.find()			
			if find:
				self.sprites[os.path.basename(find)] = load(self.JanPygame, find)

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
			if self.some_not_selected is True:
				if event.type is pygame.MOUSEBUTTONUP and event.button is 3:
					self.create_file_tool_menu()

			elif self.some_not_selected is False:
				if self.selected_type is "Sprite":
					if event.type is pygame.MOUSEBUTTONUP and event.button is 3:
						self.create_selected_sprite_menu()

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
	