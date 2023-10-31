from aochelper import *
import math

# https://adventofcode.com/2018

#########################################
#########################################

def TestData1():
	inputdata.clear()
	inputdata.append("18")
	# Result = "33,45"

def TestData2():
	inputdata.clear()
	inputdata.append("42")
	# Result = "21,61"

#########################################
#########################################

def GetHundreds(v):
	if v < 100:
		return 0
	return ((v - (v % 100)) // 100) % 10

def CalculateCellPowerLevel(x, y, serial):
	rackid = x + 10
	power = rackid * y
	power += serial
	power *= rackid
	power = GetHundreds(power)
	power -= 5
	return power

def CalculatePowerLevel(grid, x, y, serial, squaresize):

	totalpower = 0

	for dx in range(squaresize):
		for dy in range(squaresize):
			xx = x + dx
			yy = y + dy
			power = grid[yy - 1][xx - 1]
			totalpower += power

	return totalpower

def BuildGrid(serial, gridsize):
	grid = [ [0 for _ in range(gridsize)] for _ in range(gridsize) ]
	
	for y in range(gridsize):
		for x in range(gridsize):
			grid[y][x] = CalculateCellPowerLevel(x + 1, y + 1, serial)

	return grid	

#########################################
#########################################

def PartA():
	StartPartA()
	serial = int(inputdata[0])
	print(f"Grid Serial: {serial}")

	# xx = 122
	# yy = 79
	# ss = 57
	# p = CalculateCellPowerLevel(xx, yy, ss)
	# print(f" ID {ss} ({xx},{yy}) = {p}")

	gridsize = 300
	grid = BuildGrid(serial, gridsize)
	print("Grid build")
	squaresize = 3

	highestpowerlevel = -1_000_000_000
	coord = None
	for y in range(gridsize - (squaresize + 1)):
		for x in range(gridsize - (squaresize + 1)):
			powerlevel = CalculatePowerLevel(grid, x + 1, y + 1, serial, squaresize)
			if powerlevel > highestpowerlevel:
				highestpowerlevel = powerlevel
				coord = f"{x + 1},{y + 1}"
				# print(coord, highestpowerlevel)

	ShowAnswer(coord)

#########################################
#########################################

def PartB():
	StartPartB()
	serial = int(inputdata[0])
	print(f"Grid Serial: {serial}")

	gridsize = 300
	grid = BuildGrid(serial, gridsize)
	print("Grid build")
	highestpowerlevel = -1_000_000_000
	coord = None
	for squaresize in range(1, gridsize + 1):
		print(f"Square Size {squaresize}", end = "\r")
		for y in range(gridsize - (squaresize + 1)):
			for x in range(gridsize - (squaresize + 1)):
				powerlevel = CalculatePowerLevel(grid, x + 1, y + 1, serial, squaresize)
				if powerlevel > highestpowerlevel:
					highestpowerlevel = powerlevel
					coord = f"{x + 1},{y + 1},{squaresize}"
					# print(coord, highestpowerlevel)
	print("")

	ShowAnswer(coord)

#########################################
#########################################

if __name__ == "__main__":
	StartDay(11)
	ReadInput()
	TestData1()
	#TestData2()
	PartA()
	PartB()
	print("")
