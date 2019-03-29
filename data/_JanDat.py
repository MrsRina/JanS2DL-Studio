from _JanJa import pygame
from _JanJa import sys
from _JanJa import os

from _JanJa import JanGui
from _JanJa import JanFrame

from _JanJa import JAN_ENGINE_engine

class DAT:
	def __init__(self):
		try:
			self.JanWin = JanGui.create_window(JAN_ENGINE_engine.get("Width"), JAN_ENGINE_engine.get("Height"), JAN_ENGINE_engine.get("Title"),
												JAN_ENGINE_engine.get("Color"))
			
			self.JanMenu = JanGui.create_menu(self.JanWin.get_master()) 

			self.JanRun = True

			self.JanWidthPygame  = 1024
			self.JanHeightPygame = 768

			self.JanBackgroundColorPygame = (190, 190, 190, 0)

			self.create_frame()
			self.create_designer_menu()

			while (self.JanRun):
				self.JanPygame.fill((self.JanBackgroundColorPygame))

				self.window_loop()
		except:
			raise
		return None

	def create_frame(self):
		try:
			os.environ["SDL_WINDOWID"] = str(self.JanWin.get_master().winfo_id())
			os.environ['SDL_VIDEODRIVER'] = 'windib'

			pygame.init()

			self.JanPygame = pygame.display.set_mode((int(JAN_ENGINE_engine.get("Width")), int(JAN_ENGINE_engine.get("Height"))), pygame.DOUBLEBUF)
		except:
			raise
		return None

	def create_designer_menu(self):
		try:
			self.JanMenu.create_file_menu(JAN_ENGINE_engine, None, None, None, None)
			self.JanMenu.create_tools_menu(JAN_ENGINE_engine, None, None, None, None, None)
		except:
			raise
		return None

	def window_loop(self):
		try:
			def close():
				if self.JanWin.askExit("Do you want to quit?"):
					self.JanRun=False; self.JanWin.close(); sys.exit()
			
			self.JanWin.get_master().protocol("WM_DELETE_WINDOW", close)

			pygame.display.flip()			
			self.JanWin.get_master().update()
		except:
			raise
		return None
	
DAT()