from aoc import Aoc
import itertools
import math
import re
import sys

# Day 8
# https://adventofcode.com/2023

class Node():
	def __init__(self, l):
		self.children = []
		self.meta = []

		self.level = l

	def AddChild(self, c):
		self.children.append(c)

	def AddMeta(self, value):
		self.meta.append(value)

	def BuildChildren(self, ix, data):
		child = Node(ix, data)
		self.children.append(child)

	def MetaSum(self):
		som = 0
		for m in self.meta:
			som += m
		return som

	def MetaSumRecurse(self):
		som = self.MetaSum()
		for c in self.children:
			som += c.MetaSumRecurse()
		return som

	def GetValue(self):
		if len(self.children) == 0:
			return self.MetaSum()
		else:
			som = 0
			for m in self.meta:
				if m >= 1 and m <= len(self.children):
					som += self.children[m - 1].GetValue()
			return som

	def Show(self):
		for i in range(self.level):
			print("   ", end = "")
		print(f"Children: {len(self.children)} Meta: {len(self.meta)}")
		for i in range(self.level):
			print("   ", end = "")
		print(self.meta)
		print("")

		for child in self.children:
			child.Show()

	@staticmethod
	def CreateNode(ix, data, level):
		childcount = data[ix]
		metacount = data[ix + 1]

		ix += 2
		node = Node(level)

		for c in range(childcount):
			child, ix = Node.CreateNode(ix, data, level + 1)
			node.AddChild(child)

		for m in range(metacount):
			node.AddMeta(data[ix])
			ix += 1

		return node, ix

class Day8Solution(Aoc):

    def Run(self):
        self.StartDay(8, "Memory Maneuver")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(8)

        goal = self.TestDataA()
        self.PartA()
        self.Assert(self.GetAnswerA(), goal)

        goal = self.TestDataB()
        self.PartB()
        self.Assert(self.GetAnswerB(), goal)

    def TestDataA(self):
        self.inputdata.clear()
        testdata = \
        """
        2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 138

    def TestDataB(self):
        self.inputdata.clear()
        self.TestDataA()    # If test data is same as test data for part A
        return 66

    def PartA(self):
        self.StartPartA()

        data = [ int(x) for x in self.inputdata[0].split(" ") ]
        root, _ = Node.CreateNode(0, data, 0)

        # print(data)
        # root.Show()
        answer = root.MetaSumRecurse()

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        data = [ int(x) for x in self.inputdata[0].split(" ") ]
        root, _ = Node.CreateNode(0, data, 0)

        answer = root.GetValue()

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day8Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

