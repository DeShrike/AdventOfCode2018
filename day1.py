from aochelper import *
import math

# https://adventofcode.com/2018

#########################################
#########################################

def TestData():
	inputdata.clear()
	inputdata.append(7)
	inputdata.append(7)
	inputdata.append(-2)
	inputdata.append(-7)
	inputdata.append(-4)

#########################################
#########################################

def PartA():
	StartPartA()
	total = 0
	for m in inputdata:
		total += int(m)

	ShowAnswer(total)

#########################################
#########################################

def PartB():
	StartPartB()

	loop = 0
	total = 0
	history = {}
	found = False
	while found == False:
		loop += 1
		# print(loop, total, len(history), end = "\r")
		for m in inputdata:
			total += int(m)
			if total in history:
				found = True
				break
			history[total] = True

	# print("")
	ShowAnswer(total)

#########################################
#########################################

if __name__ == "__main__":
	StartDay(1)
	ReadInput()
	# TestData()
	PartA()
	PartB()
	print("")
