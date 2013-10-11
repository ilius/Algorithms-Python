def printSeam(sc, direction):
	"""vertical seam is a list of cols"""
	seam = sc.findSeam(direction)

	for row in range(sc._height):
		for col in range(sc._width):
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
	seam = sc.findSeam(direction)

	if direction == "vertical":
		seam_indices = zip(seam, range(sc._height))
	else:
		seam_indices = zip(range(sc._width), seam)
	totalSeamEnergy = sum(sc.energy(col, row) for col, row in seam_indices)
	print "\nTotal seam energy: {:d}".format(totalSeamEnergy)
	return totalSeamEnergy
