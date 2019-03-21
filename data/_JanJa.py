import ctypes
import math
import sys
import os

sys.path.insert(0, "{}\\SDL.dll".format(os.getcwd()))
sys.path.insert(0, "{}\\data\\func".format(os.getcwd()))

from func import JanJson

global JAN_ENGINE_path
global JAN_ENGINE_embed

JAN_ENGINE_path  = JanJson.load("data/_np/JanEnginePath.json")
JAN_ENGINE_cdll  = ctypes.CDLL("SDL.dll")
JAN_ENGINE_reso  = JAN_ENGINE_cdll.SDL_ListModes(None, None)

# Fix paths
JAN_ENGINE_path.rem("Jan_Dll")
JAN_ENGINE_path.new("Jan_Engine", "{}\\data\\_np\\JanEngine.json".format(os.getcwd()))
JAN_ENGINE_path.new("Jan_Engine", "{}".format(JAN_ENGINE_reso))

try:
	# pygame import
	from pygame import *
	import pygame
except:
	raise

global JAN_ENGINE_engine

JAN_ENGINE_engine = JanJson.load(JAN_ENGINE_path.get("Jan_Engine"))

J

from func import JanGui
from func import JanFrame