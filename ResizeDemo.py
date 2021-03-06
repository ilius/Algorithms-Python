import argparse, png, array
from readPNG_2 import Picture
#from SeamCarverLib import SeamCarver
import SeamCarverLib
import SeamCarverUtilities
import pdb

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="filename of image", type=str)
parser.add_argument("rowsToRemove", help="number of rows to remove from image", type=int)
parser.add_argument("colsToRemove", help="number of cols to remove from image", type=int)
args = parser.parse_args()

print "build energy array for {}".format(args.filename)
pic = Picture(args.filename)

print "create seam carver"
sc = SeamCarverLib.SeamCarver(pic)

print "print vertical seam 1"
print sc._width, sc._height
#SeamCarverUtilities.printVerticalSeamEnergy(sc)
SeamCarverUtilities.printSeam(sc, direction="vertical")
#SeamCarverUtilities.distToArray(sc)
			
print "remove vertical seam"
s = sc.findSeam(direction="vertical")
sc.removeVerticalSeam(s)
print sc._width, sc._height
print "find vertical seam"
SeamCarverUtilities.printSeam(sc, direction="vertical")

print "print horizontal seam"
SeamCarverUtilities.printSeam(sc, direction="horizontal")
#SeamCarverUtilities.distToArray(sc)
#SeamCarverUtilities.printHorizontalSeamEnergy(sc)

print "remove horizontal seam"
s = sc.findSeam(direction="horizontal")
sc.removeHorizontalSeam(s)
print sc._width, sc._height
#SeamCarverUtilities.printHorizontalSeamEnergy(sc)
print "find horizontal seam"
SeamCarverUtilities.printSeam(sc, direction="horizontal")
#SeamCarverUtilities.distToArray(sc)

			
# s = sc.findVerticalSeam()				
# sc.removeVerticalSeam(s)

# # print "print vertical seam 2"
# print sc._width, sc._height
# SeamCarverUtilities.printVerticalSeam(sc)
# #SeamCarverUtilities.printVerticalSeamEnergy(sc)			
# # s = sc.findVerticalSeam()
# # for i in range(sc._height):
# # 	print s[i]
# # # print sc._edgeTo
# # # print sc._distTo
# # SeamCarverUtilities.printVerticalSeam(sc) 			
# # print

# s = sc.findVerticalSeam()
# sc.removeVerticalSeam(s)
# print sc._width, sc._height

# # print "print vertical seam 3"
# # print sc._width, sc._height
# SeamCarverUtilities.printVerticalSeam(sc)
# SeamCarverUtilities.distToArray(sc)
# #SeamCarverUtilities.printVerticalSeamEnergy(sc)			
# # s = sc.findVerticalSeam()
# # for i in range(sc._height):
# # 	print s[i]

# s = sc.findVerticalSeam()
# sc.removeVerticalSeam(s)
# print sc._width, sc._height

# # print "print vertical seam 4"
# # print sc._width, sc._height
# SeamCarverUtilities.printVerticalSeam(sc)
#SeamCarverUtilities.printVerticalSeamEnergy(sc)			
# s = sc.findVerticalSeam()
# for i in range(sc._height):
# 	print s[i]

# print "print vertical seam 2"
# # print sc._edgeTo
# # print sc._distTo
# s = sc.findVerticalSeam()
# sc.removeVerticalSeam(s)  							
# print sc._height, sc._width	
#SeamCarverUtilities.printVerticalSeam(sc) 			
# print

# print "print vertical seam 3"
# s = sc.findVerticalSeam()							
# sc.removeVerticalSeam(s) 							
# print sc._height, sc._width
# # print sc._edgeTo
# # print sc._distTo					
# #pdb.set_trace()
#SeamCarverUtilities.printVerticalSeam(sc) 			
# print

# print "remove vertical seam 4"
# s = sc.findVerticalSeam()
# sc.removeVerticalSeam(s)
# print sc._height, sc._width
# # print sc._edgeTo
# # print sc._distTo
# SeamCarverUtilities.printVerticalSeam(sc)

# print "remove vertical seam 5"
# s = sc.findVerticalSeam()
# sc.removeVerticalSeam(s)
# print sc._height, sc._width
# SeamCarverUtilities.printVerticalSeam(sc)


#print "remove {} rows".format(args.rowsToRemove)
#print "remove {} cols".format(args.colsToRemove)

