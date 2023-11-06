from aoc import Aoc
import itertools
import math
import re
import sys

# Day 6
# https://adventofcode.com/2023

class Day6Solution(Aoc):

    def Run(self):
        self.StartDay(6, "Chronal Coordinates")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(6)

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
        1, 1
        1, 6
        8, 3
        3, 4
        5, 5
        8, 9
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 17

    def TestDataB(self):
        self.inputdata.clear()
        self.TestDataA()    # If test data is same as test data for part A
        return 16

    def ManhattanDistance(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    def TransformToCoords(self):
        coords = []
        maxx = 0
        maxy = 0
        for line in self.inputdata:
            parts = line.split(",")
            x = int(parts[0].strip())
            y = int(parts[1].strip())
            if x > maxx:
                maxx = x
            if y > maxy:
                maxy = y
            coords.append( (x, y) )

        maxx += 1
        maxy += 1

        print(f"Extends: {maxx}x{maxy}")

        return coords, maxx, maxy

    def PartA(self):
        self.StartPartA()

        coords, maxx, maxy = self.TransformToCoords()
        grid = [ [ -1 for x in range(maxx) ] for y in range(maxy)]
        distances = [ [ [] for x in range(maxx) ] for y in range(maxy)]

        for x1 in range(maxx):
            print(f"Calculating col {x1}", end = "\r")
            for y1 in range(maxy):
                for i in range(len(coords)):
                    coord = coords[i]
                    cx = coord[0]
                    cy = coord[1]
                    dist = self.ManhattanDistance(x1, y1, cx, cy)
                    distances[y1][x1].append( (i, dist) )

        # distances is a grid that now contains a list of all distances to each coord
        # now sort them all
        for x1 in range(maxx):
            print(f"Sorting col {x1}            ", end = "\r")
            for y1 in range(maxy):
                distances[y1][x1].sort(key = lambda x: x[1] )
                if len(distances[y1][x1]) > 1:
                    dist0 = distances[y1][x1][0]
                    dist1 = distances[y1][x1][1]
                    if dist0[1] == dist1[1]:
                        grid[y1][x1] = -1
                    else:
                        grid[y1][x1] = dist0[0]
                else:
                    grid[y1][x1] = distances[y1][x1][0][0]


        #for l in grid:
        #	for c in l:
        #		if c == -1:
        #			print(".", end = "")
        #		else:
        #			print(chr(c + 1 + 64), end = "")
        #	print("")

        infinites = []
        counts = [0 for _ in range(len(coords))]
        for x in range(maxx):
            print(f"Counting col {x}            ", end = "\r")
            for y in range(maxy):
                coordid = grid[y][x]
                if coordid != -1:
                    counts[coordid] += 1
                    if x == 0 or y == 0 or x == maxx - 1 or y == maxy - 1:
                        if coordid not in infinites:
                            infinites.append(coordid)

        print("")

        for infin in infinites:
            counts[infin] = 0
        counts.sort(reverse = True)

        # Attempt 1: 2757 = too high

        answer = counts[0]

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        coords, maxx, maxy = self.TransformToCoords()
        grid = [ [ 0 for x in range(maxx) ] for y in range(maxy)]

        maxdistance = 10_000
        if len(coords) < 10:
            # We are using the testdata
            maxdistance = 32

        regionsize = 0
        for x1 in range(maxx):
            print(f"Calculating col {x1}", end = "\r")
            for y1 in range(maxy):
                for i in range(len(coords)):
                    coord = coords[i]
                    cx = coord[0]
                    cy = coord[1]
                    dist = self.ManhattanDistance(x1, y1, cx, cy)
                    grid[y1][x1] += dist
                if grid[y1][x1] < maxdistance:
                    regionsize += 1

        print("")

        answer = regionsize

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day6Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

