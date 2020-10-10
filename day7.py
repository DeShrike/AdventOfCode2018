from aochelper import *
import math
import re

# https://adventofcode.com/2018

#########################################
#########################################

def TestData():
	inputdata.clear()
	inputdata.append("Step C must be finished before step A can begin.")
	inputdata.append("Step C must be finished before step F can begin.")
	inputdata.append("Step A must be finished before step B can begin.")
	inputdata.append("Step A must be finished before step D can begin.")
	inputdata.append("Step B must be finished before step E can begin.")
	inputdata.append("Step D must be finished before step E can begin.")
	inputdata.append("Step F must be finished before step E can begin.")

#########################################
#########################################

steps = []

def ParseInput():
	steps.clear()
	rx = re.compile("Step (?P<first>[A-Z]*) must be finished before step (?P<next>[A-Z]*) can begin.")
	for line in inputdata:
		match = rx.search(line)
		if match:
			first = match["first"]
			second = match["next"]
			steps.append((first, second))

#########################################
#########################################

partAresult = ""

def PartA():
	global partAresult

	StartPartA()
	ParseInput()
	# print(steps)

	todo = []
	for step in steps:
		if step[0] not in todo:
			todo.append(step[0])
		if step[1] not in todo:
			todo.append(step[1])

	# print("TODO", todo)

	execution = ""
	done = []
	available = []

	while len(todo) > 0:
		available.clear()
		for letter in todo:
			alldone = True
			for step in steps:
				if step[1] == letter:
					if step[0] not in done:
						alldone = False
						break
			if alldone:
				available.append(letter)

		available.sort()
		first = available[0]
		execution += first
		done.append(first)
		todo.remove(first)

	partAresult = execution
	ShowAnswer(execution)

#########################################
#########################################

def FindNextToExecute(todo, completed):
	for i in range(len(todo)):
		step = todo[i]
		available = True
		for s in steps:
			if s[1] == step:
				if s[0] not in completed:
					available = False
					break
		if available:
			return step

	return None

def PartB():
	StartPartB()
	ParseInput()

	workercount = 5
	defaultstepduration = 60
	if len(steps) < 10:
		# We are using the testdata
		workercount = 2
		defaultstepduration = 0

	workers = [ [0, "."] for _ in range(workercount)]

	completed = []

	todo = []
	for ch in partAresult:
		todo.append(ch)
	todo.sort()

	ix = 0
	second = 0
	done = False
	while done == False:
		working = False
		while True:
			for w in range(len(workers)):
				if workers[w][0] > 0:
					workers[w][0] -= 1
					if workers[w][0] == 0:
						completed.append(workers[w][1])
						workers[w][1] = "."
						# print(f"Step {workers[w][1]} done by worker {w + 1} on second {second}")

				if workers[w][0] == 0:
					nextstep = FindNextToExecute(todo, completed)
					if nextstep is not None:
						todo.remove(nextstep)
						step = nextstep
						# print(f"Worker {w + 1} starting {step} on second {second}")
						stepduration = defaultstepduration + (ord(step) - 64)
						workers[w] = [stepduration, step]

				if workers[w][0] > 0:
					working = True
			
			# check if there are free workers and if there are jobs available (L should start at 80, not 81)
			idle = 0
			for w in range(len(workers)):
				if workers[w][0] == 0:
					idle += 1
			nextstep = FindNextToExecute(todo, completed)
			if idle > 0 and nextstep is not None:
				pass
			else:
				break

		if False:
			print(f"{second:4}", end = " ")
			for w in workers:
				if w[1] == ".":
					print("  /  ", end = " ")
				else:
					print(f"{w[1]}({w[0]:2})", end = " ")
			for ch in completed:
				print(ch, end = "")
			print("")

		if len(todo) == 0 and not working:
			done = True
		else:
			second += 1

	# Attempt 1: 425 is too low
	# Attempt 2: 1116 is too high

	ShowAnswer(second)

#########################################
#########################################

if __name__ == "__main__":
	StartDay(7)
	ReadInput()
	# TestData()
	PartA()
	PartB()
	print("")
