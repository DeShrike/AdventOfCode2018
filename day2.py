from aochelper import *
import math

# https://adventofcode.com/2018

#########################################
#########################################

def TestDataA():
	inputdata.clear()
	inputdata.append("abcdef")
	inputdata.append("bababc")
	inputdata.append("abbcde")
	inputdata.append("abcccd")
	inputdata.append("aabcdd")
	inputdata.append("abcdee")
	inputdata.append("ababab")

def TestDataB():
	inputdata.clear()
	inputdata.append("abcde")
	inputdata.append("fghij")
	inputdata.append("klmno")
	inputdata.append("pqrst")
	inputdata.append("fguij")
	inputdata.append("axcye")
	inputdata.append("wvxyz")

#########################################
#########################################

def CountA(s):
	counts = {}
	for ch in s:
		if ch in counts:
			counts[ch] += 1
		else:
			counts[ch] = 1
	two = 0
	three = 0
	for k in counts.keys():
		if counts[k] == 2:
			two += 1
		elif counts[k] >= 3:
			three += 1

	two = min(1, two)
	three = min(1, three)
	# print(s, two, three)

	return two, three

def PartA():
	StartPartA()
	total2 = 0
	total3 = 0
	for m in inputdata:
		two, three = CountA(m)
		total2 += two
		total3 += three

	ShowAnswer(total2 * total3)

#########################################
#########################################

def CountDifference(s1, s2):
	d = 0
	cc = ""
	for i in range(len(s1)):
		if s1[i] != s2[i]:
			d += 1
		else:
			cc += s1[i]
	return d, cc

def PartB():
	StartPartB()

	aa = None
	bb = None

	for a in range(len(inputdata)):
		for b in range(len(inputdata)):
			if b == a:
				continue
			diff, _ = CountDifference(inputdata[a], inputdata[b])
			if diff == 1:
				print(inputdata[a], inputdata[b])
				aa = inputdata[a]
				bb = inputdata[b]

	_, common = CountDifference(aa, bb)
	ShowAnswer(common)

#########################################
#########################################

if __name__ == "__main__":
	StartDay(2)
	ReadInput()
	# TestDataA()
	PartA()
	# TestDataB()
	PartB()
	print("")
