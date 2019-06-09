import os

def is_project_file(path):
	try:
		try:
			with open(("{}.jpf".format(path.replace("{}".format(os.path.splitext(os.path.basename(path))[1]), ""))), "r"):
				return True
		except FileNotFoundError:
			return False
	except:
		raise
	return None

def print_load_project(json):
	try:
		return (
"""
Opened the project file .JPF ...
Project name: {PN} ...
Master path project: {MPP} ...
Sprites: {lS} ...
Objects: {lO} ...
Project comments: ...
{PC} ...
Version project: {VP} ..
"""
			.format(
			PN  = json["Name"],
			MPP = json["Local Path Project"],
			lS  = len(json["Game Sprites"]),
			lO  = len(json["Game Objects"]),
			PC  = json["Game Comments"],
			VP  = json["File Version"]))
	except:
		raise
	return None

def print_create_project(json):
	try:
		return (
"""
Created new file project .JPF ...
Project name: {PN} ...
Master path project: {MPP} ...
Sprites: {lS} ...
Objects: {lO} ...
Project comments: 
{PC} ...
Version project: {VP} ...
"""
			.format(
			PN  = json["Name"],
			MPP = json["Local Path Project"],
			lS  = len(json["Game Sprites"]),
			lO  = len(json["Game Objects"]),
			PC  = json["Game Comments"],
			VP  = json["File Version"]))
	except:
		raise
	return None