def remove(main, sprite):
	try:
		if sprite is "None":
			pass
		else:
			return main[sprite].delete()
	except:
		pass
	return None