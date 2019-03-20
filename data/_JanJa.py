rom tkinter import *

import sdl2.ext as _sdl
import sdl2 	as sdl

import math
import json
import sys
import os

JAN_load_json = lambda x_path : (json.load(open(x_path, "r")))
JAN_embed     = lambda x_id   : (setattr(os.environ['SDL_WINDOWID'], str(x_id.winfo_id())))

path = JAN_load_json("data/bin/path.json")

print(path)