from aochelper import *
import math
import re
# https://adventofcode.com/2018

#########################################
#########################################

def TestData():
	inputdata.clear()
	inputdata.append("position=< 9,  1> velocity=< 0,  2>")
	inputdata.append("position=< 7,  0> velocity=<-1,  0>")
	inputdata.append("position=< 3, -2> velocity=<-1,  1>")
	inputdata.append("position=< 6, 10> velocity=<-2, -1>")
	inputdata.append("position=< 2, -4> velocity=< 2,  2>")
	inputdata.append("position=<-6, 10> velocity=< 2, -2>")
	inputdata.append("position=< 1,  8> velocity=< 1, -1>")
	inputdata.append("position=< 1,  7> velocity=< 1,  0>")
	inputdata.append("position=<-3, 11> velocity=< 1, -2>")
	inputdata.append("position=< 7,  6> velocity=<-1, -1>")
	inputdata.append("position=<-2,  3> velocity=< 1,  0>")
	inputdata.append("position=<-4,  3> velocity=< 2,  0>")
	inputdata.append("position=<10, -3> velocity=<-1,  1>")
	inputdata.append("position=< 5, 11> velocity=< 1, -2>")
	inputdata.append("position=< 4,  7> velocity=< 0, -1>")
	inputdata.append("position=< 8, -2> velocity=< 0,  1>")
	inputdata.append("position=<15,  0> velocity=<-2,  0>")
	inputdata.append("position=< 1,  6> velocity=< 1,  0>")
	inputdata.append("position=< 8,  9> velocity=< 0, -1>")
	inputdata.append("position=< 3,  3> velocity=<-1,  1>")
	inputdata.append("position=< 0,  5> velocity=< 0, -1>")
	inputdata.append("position=<-2,  2> velocity=< 2,  0>")
	inputdata.append("position=< 5, -2> velocity=< 1,  2>")
	inputdata.append("position=< 1,  4> velocity=< 2,  1>")
	inputdata.append("position=<-2,  7> velocity=< 2, -2>")
	inputdata.append("position=< 3,  6> velocity=<-1, -1>")
	inputdata.append("position=< 5,  0> velocity=< 1,  0>")
	inputdata.append("position=<-6,  0> velocity=< 2,  0>")
	inputdata.append("position=< 5,  9> velocity=< 1, -2>")
	inputdata.append("position=<14,  7> velocity=<-2,  0>")
	inputdata.append("position=<-3,  6> velocity=< 2, -1>")

#########################################
#########################################

class Star():
	def __init__(self, x, y, dx, dy):
		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy

	def __repr__(self):
		return f"Star({self.x}, {self.y}, {self.dx}, {self.dy})"

	def DoStep(self, stepsize):
		self.x += self.dx * stepsize
		self.y += self.dy * stepsize

#########################################
#########################################

stars = []

def ParseInput():
	stars.clear()
	rx = re.compile("position=<(?P<x>[\-0-9]*), (?P<y>[\-0-9]*)> velocity=<(?P<dx>[\-0-9]*), (?P<dy>[\-0-9]*)>")
	for line in inputdata:
		match = rx.search(line.replace("  ", " ").replace("< ", "<"))
		if match:
			x = int(match["x"])
			y = int(match["y"])
			dx = int(match["dx"])
			dy = int(match["dy"])
			star = Star(x, y, dx, dy)
			stars.append(star)

#########################################
#########################################

def CalculateExtent():
	minx = miny = 1_000_000_000
	maxx = maxy = -1_000_000_000
	for star in stars:
		if star.x < minx:
			minx = star.x
		if star.y < miny:
			miny = star.y
		if star.x > maxx:
			maxx = star.x
		if star.y > maxy:
			maxy = star.y

	return minx, maxx, miny, maxy

#########################################
#########################################

def PrintStars():
	minx, maxx, miny, maxy = CalculateExtent()
	sizex = maxx - minx
	sizey = maxy - miny

	grid = [ [ 0 for _ in range(maxx + 1) ] for _ in range(maxy + 1)]
	for star in stars:
		try:
			grid[star.y][star.x] = 1
		except Exception as e:
			print("ERROR")
			print(f"{star.x} {star.y}")
			print(f"X = {minx} to {maxx} : Y = {miny} to {maxy} ( {sizex}x{sizey} )")
			raise
		else:
			pass
		finally:
			pass

	for y, line in enumerate(grid):
		if y < miny:
			continue
		for x, col in enumerate(line):
			if x < minx:
				continue
			if col == 1:
				print("*", end = "")
			else:
				print(" ", end = "")
		print("")
	
	# a = input()

#########################################
#########################################

def DoStars(showstars):
	ParseInput()

	waitseconds = 0
	# print(stars)
	# print(len(stars))
	prevsizex = 1_000_000_000

	for i in range(100000):
		minx, maxx, miny, maxy = CalculateExtent()
		
		sizex = maxx - minx
		sizey = maxy - miny
		# print(f"Second {i} : X = {minx} to {maxx} : Y = {miny} to {maxy} ( {sizex}x{sizey} )")

		if sizey < 10 and minx >= 0 and miny >= 0:
			if showstars:
				PrintStars()
			break

		if sizex > prevsizex:
			break

		prevsizex = sizex

		stepsize = 1
		if sizex > 10000:
			stepsize = 1000
		if sizex > 1000:
			stepsize = 100
		if sizex > 1000:
			stepsize = 10
		waitseconds += stepsize
		for star in stars:
			# print(waitseconds)
			star.DoStep(stepsize)

	return waitseconds

#########################################
#########################################

def PartA():
	StartPartA()
	DoStars(True)
	ShowAnswer("BLGNHPJC")

#########################################
#########################################

def PartB():
	StartPartB()
	seconds = DoStars(False)
	ShowAnswer(seconds)

#########################################
#########################################

if __name__ == "__main__":
	StartDay(10)
	ReadInput()
	# TestData()
	PartA()
	PartB()
	print("")
