from tkinter import *
from tkinter import ttk


class ProcessWindow:
	def __init__(self):
		self.Win = Tk()
		self.Win.geometry("1280x720")
		self.Win.title("Container_TEST_!")
		self.Win.configure(background="Gray")

		self.Quad = Frame(self.Win, width=400, height=400)
		self.Quad2 = Frame(self.Win, width=400, height=400)
		self.Quad3 = Frame(self.Win, width=400, height=400)

		note = ttk.Notebook(self.Win)
		note.add(self.Quad, text="aka")
		note.add(self.Quad2, text="aka")
		note.add(self.Quad3, text="aka")

		note.pack()

		self.Win.mainloop()

Run = ProcessWindow()