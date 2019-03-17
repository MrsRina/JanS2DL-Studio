from tkinter import *

import sdl2.ext as _sdl
import sdl2 	as sdl

import math
import json
import sys
import os

def embed(_embed):
	try:
		os.environ['SDL_WINDOWID'] = str(_embed.winfo_id())
		os.environ['SDL_VIDEODRIVER'] = "windib"
	except:
		raise
	return None

global path

path = json.loads("data/path.json")