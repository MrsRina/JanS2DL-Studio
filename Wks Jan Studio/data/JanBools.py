def remove(main, sprite):
	try:
		return main[sprite].delete()
	except:
		pass
	return None