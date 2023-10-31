from aoc import Aoc
import itertools
import math
import re
import sys

# Day 3
# https://adventofcode.com/2023

class Claim():
	def __init__(self, id, left, top, width, height):
		self.id = id
		self.left = left
		self.top = top
		self.width = width
		self.height = height

class Day3Solution(Aoc):

    def Run(self):
        self.StartDay(3, "No Matter How You Slice It")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(3)

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
        #1 @ 1,3: 4x4
        #2 @ 3,1: 4x4
        #3 @ 5,5: 2x2
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return None

    def TestDataB(self):
        self.inputdata.clear()
        # self.TestDataA()    # If test data is same as test data for part A
        testdata = \
        """
        1000
        2000
        3000
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return None

    def FindExtends(self, claims):
        # Finding extends
        maxx = 0
        maxy = 0
        for claim in claims:
            if claim.left + claim.width > maxx:
                maxx = claim.left + claim.width
            if claim.top + claim.height > maxy:
                maxy = claim.top + claim.height

        print(f"Extends: {maxx}x{maxy}")
        return maxx, maxy	

    def Parse(self, line, rx):
        match = rx.search(line)
        if match:
            id = int(match["id"])
            left = int(match["left"])
            top = int(match["top"])
            width = int(match["width"])
            height = int(match["height"])
            # print(line, id, left, top, width, height)
            return Claim(id, left, top, width, height)
        else:
            return None

    def ParseInput(self):
        rx = re.compile("#(?P<id>[0-9]*) @ (?P<left>[0-9]*),(?P<top>[0-9]*): (?P<width>[0-9]*)x(?P<height>[0-9]*)")

        claims = []
        for line in self.inputdata:
            c = self.Parse(line, rx)
            if c is not None:
                claims.append(c)
            else:
                print("Parse error: ", line)
        return claims

    def PartA(self):
        self.StartPartA()

        claims = self.ParseInput()
        maxx, maxy = self.FindExtends(claims)
        grid = [ [ 0 for x in range(maxx) ] for y in range(maxy)]

        for claim in claims:
            for x in range(claim.left, claim.left + claim.width):
                for y in range(claim.top, claim.top + claim.height):
                    grid[y][x] += 1

        overlaps = 0
        for y in range(maxy):
            for x in range(maxx):
                if grid[y][x] > 1:
                    overlaps += 1

        answer = overlaps

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        claims = self.ParseInput()
        maxx, maxy = self.FindExtends(claims)
        grid = [ [ 0 for x in range(maxx) ] for y in range(maxy)]

        # apply claims
        for claim in claims:
            for x in range(claim.left, claim.left + claim.width):
                for y in range(claim.top, claim.top + claim.height):
                    grid[y][x] += claim.id

        # verify claims
        goodclaimid = None
        for claim in claims:
            bad = False
            for x in range(claim.left, claim.left + claim.width):
                for y in range(claim.top, claim.top + claim.height):
                    if grid[y][x] != claim.id:
                        bad = True
                        break
            if bad == False:
                goodclaimid = claim.id

        answer = goodclaimid

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day3Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

