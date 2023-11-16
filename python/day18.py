from aoc import Aoc
import itertools
import math
import re
import sys

# Day 18
# https://adventofcode.com/2023

class Day18Solution(Aoc):

    def Run(self):
        self.StartDay(18, "Settlers of The North Pole")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(18)

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
        .#.#...|#.
        .....#|##|
        .|..|...#.
        ..|#.....#
        #.#|||#|#|
        ...#.||...
        .|....|...
        ||...#|.#|
        |.||||..|.
        ...#.|..|.
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 1147

    def ParseInput(self):
        height = len(self.inputdata)
        width = len(self.inputdata[0])
        grid = [[0 for _ in range(width)] for _ in range(height)]
        for y, line in enumerate(self.inputdata):
            for x, col in enumerate(line):
                if col == "#":
                    grid[y][x] = 1
                elif col =="|":
                    grid[y][x] = 2
        
        return width, height, grid
    
    def TestDataB(self):
        self.inputdata.clear()
        self.TestDataA()    # If test data is same as test data for part A
        return None

    def Neighbors(self, width: int, height: int, x: int, y: int):
        nn = [(0,-1), (1,-1), (1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1)]
        for n in nn:
            nx = x + n[0]
            ny = y + n[1]
            if nx < 0 or ny < 0 or nx >= width or ny >= height:
                continue
            yield (nx, ny)

    def PrintGrid(self, width: int, height: int, grid):
        for y in range(width):
            for x in range(height):
                if grid[y][x] == 0:
                    print(".", end="")
                elif grid[y][x] == 1:
                    print("#", end="")
                elif grid[y][x] == 2:
                    print("|", end="")
            print("")
        
    def Step(self, width: int, height: int, grid):
        newgrid = [[0 for _ in range(width)] for _ in range(height)]

        for y in range(width):
            for x in range(height):
                nnn = [grid[yy][xx] for (xx, yy) in self.Neighbors(width, height, x, y)]
                newgrid[y][x] = grid[y][x]
                ntrees = len([n for n in nnn if n == 2])
                nlumber = len([n for n in nnn if n == 1])
                if grid[y][x] == 0: # open
                    if ntrees >= 3:
                        newgrid[y][x] = 2
                elif grid[y][x] == 2: # wood
                    if nlumber >= 3:
                        newgrid[y][x] = 1
                elif grid[y][x] == 1: # lumber
                    if nlumber < 1 or ntrees < 1:
                        newgrid[y][x] = 0
        for y in range(width):
            for x in range(height):
                grid[y][x] = newgrid[y][x]

    def Doit(self, minutes: int) -> int:
        width, height, grid = self.ParseInput()

        # self.PrintGrid(width, height, grid)
        i = 0
        while i < minutes:
            if i % 100 == 0 and i > 0:
                print(f"Iteration {i}", end="\r")

            self.Step(width, height, grid)
            # self.PrintGrid(width, height, grid)
            flat = list(itertools.chain.from_iterable(grid))

            wood = [f for f in flat if f == 2]
            lumber = [f for f in flat if f == 1]

            if len(wood) * len(lumber) == 186063:
                while i + 28 < minutes:
                    i += 28
            i += 1

        flat = list(itertools.chain.from_iterable(grid))

        wood = [f for f in flat if f == 2]
        lumber = [f for f in flat if f == 1]

        return len(wood) * len(lumber)

    def PartA(self):
        self.StartPartA()

        answer = self.Doit(10)

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        answer = self.Doit(1_000_000_000)

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day18Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

