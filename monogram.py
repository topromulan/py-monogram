#!/usr/bin/python

import os

# Capture the initials:

bannerD = os.popen('banner -w 30 D').read()
bannerA = os.popen('banner -w 50 A').read()
bannerR = os.popen('banner -w 30 R').read()


# Indent the smaller types and format them all to uniform 50 character width.

# I'm going to use string formatting because I don't know how a regular
#  expression can pad them to uniform width.

def formatSmallOne(banner):
	
	A = []

	for l in banner.splitlines():

		#Ten spaces, left formatted 40 width (30 + 10):

		A.append("          %-40s\n" % l)
	
	return ''.join(A)

def formatBigOne(banner):
	
	A = []

	for l in banner.splitlines():

		#Uniform width of 50:

		A.append("%-50s\n" % l)
	
	return ''.join(A)


formattedD = formatSmallOne(bannerD)
formattedA = formatBigOne(bannerA)
formattedR = formatSmallOne(bannerR)


#Now do a linear transform on the 50 x whatever grid.
# 
# Transform: -0.5pi
#
# Essentially a matrix rearrangement

gridOriginal = formattedD + formattedA + formattedR
gridNew = ''

for y in range(49, -1, -1):
	for x in range(len(gridOriginal) / 51):
		gridNew += gridOriginal[x*51 + y]
	gridNew += "\n"


print gridOriginal
print
print gridNew























