from aochelper import *
import math

# https://adventofcode.com/2018

#########################################
#########################################

def TestData():
	inputdata.clear()
	inputdata.append("1, 1")
	inputdata.append("1, 6")
	inputdata.append("8, 3")
	inputdata.append("3, 4")
	inputdata.append("5, 5")
	inputdata.append("8, 9")

#########################################
#########################################

def ManhattanDistance(x1, y1, x2, y2):
	return abs(x1 - x2) + abs(y1 - y2)

def TransformToCoords():
	coords = []
	maxx = 0
	maxy = 0
	for line in inputdata:
		parts = line.split(",")
		x = int(parts[0].strip())
		y = int(parts[1].strip())
		if x > maxx:
			maxx = x
		if y > maxy:
			maxy = y
		coords.append( (x, y) )

	maxx += 1
	maxy += 1

	print(f"Extends: {maxx}x{maxy}")

	return coords, maxx, maxy

#########################################
#########################################

def PartA():
	StartPartA()

	coords, maxx, maxy = TransformToCoords()
	grid = [ [ -1 for x in range(maxx) ] for y in range(maxy)]
	distances = [ [ [] for x in range(maxx) ] for y in range(maxy)]

	for x1 in range(maxx):
		print(f"Calculating col {x1}", end = "\r")
		for y1 in range(maxy):
			for i in range(len(coords)):
				coord = coords[i]
				cx = coord[0]
				cy = coord[1]
				dist = ManhattanDistance(x1, y1, cx, cy)
				distances[y1][x1].append( (i, dist) )

	# distances is a grid that now contains a list of all distances to each coord
	# now sort them all
	for x1 in range(maxx):
		print(f"Sorting col {x1}            ", end = "\r")
		for y1 in range(maxy):
			distances[y1][x1].sort(key = lambda x: x[1] )
			if len(distances[y1][x1]) > 1:
				dist0 = distances[y1][x1][0]
				dist1 = distances[y1][x1][1]
				if dist0[1] == dist1[1]:
					grid[y1][x1] = -1
				else:
					grid[y1][x1] = dist0[0]
			else:
				grid[y1][x1] = distances[y1][x1][0][0]


	#for l in grid:
	#	for c in l:
	#		if c == -1:
	#			print(".", end = "")
	#		else:
	#			print(chr(c + 1 + 64), end = "")
	#	print("")

	infinites = []
	counts = [0 for _ in range(len(coords))]
	for x in range(maxx):
		print(f"Counting col {x}            ", end = "\r")
		for y in range(maxy):
			coordid = grid[y][x]
			if coordid != -1:
				counts[coordid] += 1
				if x == 0 or y == 0 or x == maxx - 1 or y == maxy - 1:
					if coordid not in infinites:
						infinites.append(coordid)

	print("")

	for infin in infinites:
		counts[infin] = 0
	counts.sort(reverse = True)

	# Attempt 1: 2757 = too high

	ShowAnswer(counts[0])

#########################################
#########################################

def PartB():
	StartPartB()


	coords, maxx, maxy = TransformToCoords()
	grid = [ [ 0 for x in range(maxx) ] for y in range(maxy)]

	maxdistance = 10_000
	if len(coords) < 10:
		# We are using the testdata
		maxdistance = 32

	regionsize = 0
	for x1 in range(maxx):
		print(f"Calculating col {x1}", end = "\r")
		for y1 in range(maxy):
			for i in range(len(coords)):
				coord = coords[i]
				cx = coord[0]
				cy = coord[1]
				dist = ManhattanDistance(x1, y1, cx, cy)
				grid[y1][x1] += dist
			if grid[y1][x1] < maxdistance:
				regionsize += 1

	print("")

	ShowAnswer(regionsize)

#########################################
#########################################

if __name__ == "__main__":
	StartDay(6)
	ReadInput()
	# TestData()
	PartA()
	PartB()
	print("")
