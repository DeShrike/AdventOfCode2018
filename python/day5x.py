from aochelper import *
import math

# https://adventofcode.com/2018

#########################################
#########################################

def TestData():
	inputdata.clear()
	inputdata.append("dabAcCaCBAcCcaDA")

#########################################
#########################################

def React(polymer):
	changed = True
	while changed:
		# print(len(polymer))
		l = len(polymer)
		for i in range(1, 26 + 1):
			r1 = chr(i + 64) + chr(i + 96)
			r2 = chr(i + 96) + chr(i + 64)
			polymer = polymer.replace(r1, "")
			polymer = polymer.replace(r2, "")
		
		changed = l != len(polymer)

	return polymer

#########################################
#########################################

def PartA():
	StartPartA()

	polymer = inputdata[0]
	polymer = React(polymer)

	ShowAnswer(len(polymer))

#########################################
#########################################

def PartB():
	StartPartB()

	polymer = inputdata[0]
	shortest = len(polymer)
	for i in range(1, 26 + 1):
		r1 = chr(i + 64)
		p = polymer.replace(r1, "")
		r2 = chr(i + 96)
		p = p.replace(r2, "")
		pp = React(p)
		if len(pp) < shortest:
			shortest = len(pp)

	ShowAnswer(shortest)

#########################################
#########################################

if __name__ == "__main__":
	StartDay(5)
	ReadInput()
	# TestData()
	PartA()
	PartB()
	print("")
