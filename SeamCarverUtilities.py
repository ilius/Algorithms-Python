def printSeam(sc, direction):
	"""vertical seam is a list of cols"""
	if direction == "vertical":
		seam = sc.findVerticalSeam()
	else:
		seam = sc.findHorizontalSeam()

	for row in range(sc.height()):
		for col in range(sc.width()):
			if direction == "vertical":
				is_on_seam = col == seam[row]
			else:
				is_on_seam = row == seam[col]
			lmarker, rmarker = ('[', ']') if is_on_seam else (' ',' ')
			print '{:s}{:>6d}{:s}'.format(lmarker, sc.energy(col, row), rmarker),
		print

	totalSeamEnergy = calculateSeamEnergy(sc, direction)
	print "\nTotal seam energy: {:d}".format(totalSeamEnergy)

def calculateSeamEnergy(sc, direction):
	if direction == "vertical":
		seam = sc.findVerticalSeam()
	else:
		seam = sc.findHorizontalSeam()
	relevant_size = sc._height if direction == "vertical" else sc._width
	seam_indices = zip(seam, relevant_size)
	totalSeamEnergy = sum(sc.energy(col, row) for col, row in seam_indices)
	print "\nTotal seam energy: {:d}".format(totalSeamEnergy)
	return totalSeamEnergy
