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

			self.JanContainer = JanGui.create_container(self.JanWin.get_master())	
			self.JanMenu      = JanGui.create_menu(self.JanWin.get_master(),
			(
				None, None, None, None, None, None, None,
				None, self.close, None, None, None, None, None,
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

			self.poop_up()

			while (self.JanRun):
				self.Tick_Fps.tick(30)

				self.up_mouse_popup_event()

				self.JanPygame.fill((self.JanBackgroundColorPygame))
				
				for event_ in pygame.event.get():
					self.dynamic_popup(event_)

				self.window_loop()
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

	def create_frame(self, id):
		try:
			os.environ["SDL_WINDOWID"] = str(id.winfo_id())
			os.environ['SDL_VIDEODRIVER'] = 'windib'

			pygame.init()

			self.JanPygame = pygame.display.set_mode((id.winfo_screenwidth(), id.winfo_screenheight()), pygame.DOUBLEBUF)
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

	def dynamic_popup(self, event):
		try:
			if event.type is pygame.MOUSEBUTTONUP and event.button is 3:
				self.create_file_tool_menu()

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

	def poop_up(self):
		try:
			self.JanContainer.frame_event_game.bind("<Button-3>", self.create_event_menu)
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
	