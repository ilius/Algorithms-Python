def printSeam(sc, direction):
	"vertical seam is a list of cols"
	if direction == "vertical":
		seam = sc.findVerticalSeam()
		seam_indices = zip(seam, range(sc.height()))
	else:
		seam = sc.findHorizontalSeam()
		seam_indices = zip(range(sc.width()), seam)

	for row in range(sc.height()):
		for col in range(sc.width()):
			if direction == "vertical":
				is_on_seam = col == seam[row]
			else:
				is_on_seam = row == seam[col]
			lmarker, rmarker = ('[', ']') if is_on_seam else (' ',' ')
			print '{:s}{:>6d}{:s}'.format(lmarker, sc.energy(col, row), rmarker),
		print

	totalSeamEnergy = sum(sc.energy(col, row) for col, row in seam_indices)
	print "\nTotal seam energy: {:d}".format(totalSeamEnergy)

def printVerticalSeamEnergy(sc):
	"vertical seam is a list of cols"
	seam = sc.findVerticalSeam()
	totalSeamEnergy = 0
	for row in range(sc.height()):
		for col in range(sc.width()):
			if col == seam[row]:
				totalSeamEnergy += sc.energy(col, row)
	print "\nTotal seam energy: {:d}".format(totalSeamEnergy)