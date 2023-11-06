from aoc import Aoc
import itertools
import math
import re
import sys

# Day 11
# https://adventofcode.com/2023

class Day11Solution(Aoc):

    def Run(self):
        self.StartDay(11, "Chronal Charge")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(11)

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
        18
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return "33,45"

    def TestDataB(self):
        self.inputdata.clear()
        # self.TestDataA()    # If test data is same as test data for part A
        testdata = \
        """
        42
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return "232,251,12"

    def GetHundreds(self, v):
        if v < 100:
            return 0
        return ((v - (v % 100)) // 100) % 10

    def CalculateCellPowerLevel(self, x, y, serial):
        rackid = x + 10
        power = rackid * y
        power += serial
        power *= rackid
        power = self.GetHundreds(power)
        power -= 5
        return power

    def CalculatePowerLevel(self, grid, x, y, serial, squaresize):

        totalpower = 0

        for dx in range(squaresize):
            for dy in range(squaresize):
                xx = x + dx
                yy = y + dy
                power = grid[yy - 1][xx - 1]
                totalpower += power

        return totalpower

    def BuildGrid(self, serial, gridsize):
        grid = [ [0 for _ in range(gridsize)] for _ in range(gridsize) ]
        
        for y in range(gridsize):
            for x in range(gridsize):
                grid[y][x] = self.CalculateCellPowerLevel(x + 1, y + 1, serial)

        return grid	

    def PartA(self):
        self.StartPartA()

        serial = int(self.inputdata[0])
        print(f"Grid Serial: {serial}")

        # xx = 122
        # yy = 79
        # ss = 57
        # p = CalculateCellPowerLevel(xx, yy, ss)
        # print(f" ID {ss} ({xx},{yy}) = {p}")

        gridsize = 300
        grid = self.BuildGrid(serial, gridsize)
        print("Grid build")
        squaresize = 3

        highestpowerlevel = -1_000_000_000
        coord = None
        for y in range(gridsize - (squaresize + 1)):
            for x in range(gridsize - (squaresize + 1)):
                powerlevel = self.CalculatePowerLevel(grid, x + 1, y + 1, serial, squaresize)
                if powerlevel > highestpowerlevel:
                    highestpowerlevel = powerlevel
                    coord = f"{x + 1},{y + 1}"
                    # print(coord, highestpowerlevel)

        answer = coord

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        serial = int(self.inputdata[0])
        print(f"Grid Serial: {serial}")

        gridsize = 300
        grid = self.BuildGrid(serial, gridsize)
        print("Grid build")
        highestpowerlevel = -1_000_000_000
        coord = None
        for squaresize in range(1, gridsize + 1):
            print(f"Square Size {squaresize}", end = "\r")
            for y in range(gridsize - (squaresize + 1)):
                for x in range(gridsize - (squaresize + 1)):
                    powerlevel = self.CalculatePowerLevel(grid, x + 1, y + 1, serial, squaresize)
                    if powerlevel > highestpowerlevel:
                        highestpowerlevel = powerlevel
                        coord = f"{x + 1},{y + 1},{squaresize}"
                        # print(coord, highestpowerlevel)
        print("")

        answer = coord

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day11Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

