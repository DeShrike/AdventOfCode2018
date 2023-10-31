from aochelper import *
import math

# https://adventofcode.com/2018

#########################################
#########################################

def TestDataA():
	inputdata.clear()
	inputdata.append("/->-(        ")
	inputdata.append("|   |  /----(")
	inputdata.append("| /-+--+-(  |")
	inputdata.append("| | |  | v  |")
	inputdata.append("(-+-/  (-+--/")
	inputdata.append("  (------/   ")
	for i in inputdata:
		i = i.replace("(", "\\")

def TestDataB():
	inputdata.clear()

#########################################
#########################################

def PartA():
	StartPartA()

	ShowAnswer("?")

#########################################
#########################################

def PartB():
	StartPartB()

	ShowAnswer("?")

#########################################
#########################################

if __name__ == "__main__":
	StartDay(0)
	ReadInput()
	TestDataA()
	PartA()
	TestDataB()
	PartB()
	print("")
