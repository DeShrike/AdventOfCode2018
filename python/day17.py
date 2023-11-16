from aoc import Aoc
from utilities import dirange
from canvas import Canvas
import itertools
import math
import re
import sys

# Day 17
# https://adventofcode.com/2023

class Day17Solution(Aoc):

    def Run(self):
        self.StartDay(17, "Reservoir Research")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(17)

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
        x=495, y=2..7
        y=7, x=495..501
        x=501, y=3..7
        x=498, y=2..4
        x=506, y=1..2
        x=498, y=10..13
        x=504, y=10..13
        y=13, x=498..504
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 57

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

    def ParseXY(self, line: str):
        rxy = re.compile("x=(?P<XXX>[0-9]*), y=(?P<YYfrom>[0-9]*)\.\.(?P<YYto>[0-9]*)")
        match = rxy.search(line)
        if match:
            xxx = int(match["XXX"])
            yyyfrom = int(match["YYfrom"])
            yyyto = int(match["YYto"])
            return xxx, yyyfrom, yyyto
        return None, None, None
    
    def ParseYX(self, line: str):
        ryx = re.compile("y=(?P<YYY>[0-9]*), x=(?P<XXfrom>[0-9]*)\.\.(?P<XXto>[0-9]*)")
        match = ryx.search(line)
        if match:
            yyy = int(match["YYY"])
            xxxfrom = int(match["XXfrom"])
            xxxto = int(match["XXto"])
            return yyy, xxxfrom, xxxto
        return None, None, None

    def ParseLine(self, line: str, grid):
        xxx, yyyfrom, yyyto = self.ParseXY(line)
        if xxx is not None:
            for y in dirange(yyyfrom, yyyto):
                grid[y][xxx] = 1
            return

        yyy, xxxfrom, xxxto = self.ParseYX(line)
        for x in dirange(xxxfrom, xxxto):
            grid[yyy][x] = 1

    def CalcExtent(self):
        minx = 1_000_000
        maxx = 0
        miny = 1_000_000
        maxy = 0
        for line in self.inputdata:
            xxx, yyyfrom, yyyto = self.ParseXY(line)
            if xxx is not None:
                minx = min(minx, xxx)
                maxx = max(maxx, xxx)
                miny = min(miny, yyyfrom)
                maxy = max(maxy, yyyfrom)
                miny = min(miny, yyyto)
                maxy = max(maxy, yyyto)
            else:
                yyy, xxxfrom, xxxto = self.ParseYX(line)
                miny = min(miny, yyy)
                maxy = max(maxy, yyy)
                minx = min(minx, xxxfrom)
                maxx = max(maxx, xxxfrom)
                minx = min(minx, xxxto)
                maxx = max(maxx, xxxto)
        return minx, maxx, miny, maxy
    
    def ParseInput(self):
        minx, maxx, miny, maxy = self.CalcExtent()
        print(f"Extent: X from {minx} to {maxx}")
        print(f"Extent: Y from {miny} to {maxy}")

        gridwidth = maxx + 20
        gridheight = maxy + 10

        grid = [ [0 for _ in range(gridwidth)] for _ in range(gridheight) ]

        for line in self.inputdata:
            self.ParseLine(line, grid)

        canvas = Canvas(gridwidth, gridheight)
        canvas.set_pixel(500, 0, (255, 0, 0))
        for y in range(gridheight):
            for x in range(gridwidth):
                if grid[y][x] == 1:
                    canvas.set_pixel(x, y, (255, 255, 255))
        canvas.save_PNG("day17.png")

    def PartA(self):
        self.StartPartA()

        self.ParseInput()

        answer = None

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        # Add solution here

        answer = None

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day17Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

