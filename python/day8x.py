from aochelper import *
import math

# https://adventofcode.com/2018

#########################################
#########################################

def TestData():
	inputdata.clear()
	inputdata.append("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2")

#########################################
#########################################

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

#########################################
#########################################

def PartA():
	StartPartA()

	data = [ int(x) for x in inputdata[0].split(" ") ]
	root, _ = Node.CreateNode(0, data, 0)

	# print(data)
	# root.Show()
	answer = root.MetaSumRecurse()

	ShowAnswer(answer)

#########################################
#########################################

def PartB():
	StartPartB()

	data = [ int(x) for x in inputdata[0].split(" ") ]
	root, _ = Node.CreateNode(0, data, 0)

	answer = root.GetValue()

	# Attempt 1: 0 
	# Attempt 2: 19 
	# Attempt 3: 67

	ShowAnswer(answer)

#########################################
#########################################

if __name__ == "__main__":
	StartDay(8)
	ReadInput()
	# TestData()
	PartA()
	PartB()
	print("")
