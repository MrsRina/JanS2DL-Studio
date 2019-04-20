from _JanJa import pygame
from _JanJa import sys
from _JanJa import os

from _JanJa import JanGui
from _JanJa import JanFrame

from _JanJa import JAN_ENGINE_engine
from _JanJa import replace_folder

from JanPort import filedialog

int_engine = lambda _int: int(JAN_ENGINE_engine.get(_int))

class DAT:
	def __init__(self):
		try:
			self.JanWin = JanGui.create_window(int_engine("Width"), int_engine("Height"), "JanJaEngine", "Gray")
			
			self.JanMenu      = JanGui.create_menu(self.JanWin.get_master())
			self.JanContainer = JanGui.create_container(self.JanWin.get_master())

			self.JanRun = True

			self.JanWidthPygame  = 1024
			self.JanHeightPygame = 768

			self. a = False

			self.JanBackgroundColorPygame = (127, 127, 127, 0)

			self.create_designer_menu()
			self.create_frame(self.JanContainer.get_id())

			while (self.JanRun):
				self.JanPygame.fill((self.JanBackgroundColorPygame))

				if self.a:
					self.JanPygame.blit(self.i, (80, 80))


				self.window_loop()
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

	def create_designer_menu(self):
		try:
			self.JanMenu.create_file_menu(None, None, None, self.close)
			self.JanMenu.create_tools_menu(self.load_image, None, None, None, None)
			self.JanMenu.create_events_menu(None, None, None, None, None)
			self.JanMenu.create_about_menu(None, None)
		except:
			raise
		return None

	def close(self):
		try:
			if   not JAN_ENGINE_engine.get("Devolper") is (False):
					self.JanRun = False; self.JanWin.close(); os.startfile(replace_folder("data/_JanJa.py", "run.cmd"))

			elif not JAN_ENGINE_engine.get("Devolper") is (True):
				if self.JanWin.askExit("Do you want to quit?"):
					self.JanRun = False; self.JanWin.close(); sys.exit()
		except:
			raise
		return None

	def load_image(self):
		try:
			filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
			if filename:
				self.a = True
				self.i = pygame.image.load(filename)
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
	
DAT()