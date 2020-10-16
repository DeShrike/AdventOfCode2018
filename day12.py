from aochelper import *
import math

# https://adventofcode.com/2018

#########################################
#########################################

def TestData():
	inputdata.clear()
	inputdata.append("initial state: #..#.#..##......###...###")
	inputdata.append("")
	inputdata.append("...## => #")
	inputdata.append("..#.. => #")
	inputdata.append(".#... => #")
	inputdata.append(".#.#. => #")
	inputdata.append(".#.## => #")
	inputdata.append(".##.. => #")
	inputdata.append(".#### => #")
	inputdata.append("#.#.# => #")
	inputdata.append("#.### => #")
	inputdata.append("##.#. => #")
	inputdata.append("##.## => #")
	inputdata.append("###.. => #")
	inputdata.append("###.# => #")
	inputdata.append("####. => #")

#########################################
#########################################

rules = []
pots = []
offset = 0

def ParseInput():
	global offset
	rules.clear()
	pots.clear()

	stufing = 3

	initial = inputdata[0][15:]
	offset = len(initial) * stufing
	for i in range(len(initial) * stufing):
		pots.append(0)
	for ch in initial:
		if ch == '#':
			pots.append(1)
		else:
			pots.append(0)
	for i in range(len(initial)):
		pots.append(0)

	for i in range(2, len(inputdata)):
		line = inputdata[i]
		parts = line.split(" => ")
		rule =  [ (1 if x == "#" else 0) for x in parts[0]]
		rules.append( (rule, 1 if parts[1] == "#" else 0) )

#########################################
#########################################

def CopyNewToPots(newpots):
	for i in range(len(pots)):
		pots[i] = newpots[i]

def CheckPot(pos):
	plant = 0
	for rule in rules:
		foundrule = True
		for i in range(5):
			ii = i - 2
			if pots[pos + ii] == rule[0][i]:
				pass
			else:
				foundrule = False
				break
		if foundrule:
			plant = rule[1]
			break

	return plant

def ShowPots(gen):
	print(f"#{gen}:", end = "")
	for p in pots:
		print("#" if p == 1 else ".", end = "")
	print("")
	# xxx = input()

#########################################
#########################################

def DoGeneration(gen):

	newpots = [ 0 for _ in range(len(pots))]
	for pos in range(2, len(pots) - 2):
		plant = CheckPot(pos)
		newpots[pos] = plant
	
	CopyNewToPots(newpots)

	# if gen % 1000 == 0:
	#	ShowPots(gen)

#########################################
#########################################

def CountPots():
	som = 0
	for ix, p in enumerate(pots):
		if p == 1:
			som += (ix - offset)
	return som

#########################################
#########################################

def PartA():
	StartPartA()
	ParseInput()

	generations = 20
	for g in range(generations):
		DoGeneration(g)

	som = CountPots()
	ShowAnswer(som)

#########################################
#########################################

def PartB():
	StartPartB()
	ParseInput()

	prevsom = 0
	generations = 320
	for g in range(generations):
		DoGeneration(g)
		som = CountPots()
		print(f"#{g}\t{som}\t{som - prevsom}")
		prevsom = som
		if pots[0] == 1 or pots[1] == 1 or pots[-1] == 1 or pots[-2] == 1:
			break

	ShowPots(0)
	ShowAnswer(0)

#########################################
#########################################

if __name__ == "__main__":
	StartDay(12)
	ReadInput()
	# TestData()
	PartA()
	# PartB()
	print("")
