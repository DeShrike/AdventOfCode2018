from aoc import Aoc
from enum import Enum
import itertools
import math
import re
import sys

# Day 13
# https://adventofcode.com/2023

Direction = Enum("Direction", ["UP", "RIGHT", "DOWN", "LEFT"])

class Cart():
    def __init__(self, chr: str, x: int, y: int):
        self.x = x
        self.y = y
        self.step = 0
        self.direction = None
        self.removed = False
        if chr == "v":
            self.direction = Direction.DOWN
        if chr == "^":
            self.direction = Direction.UP
        if chr == ">":
            self.direction = Direction.RIGHT
        if chr == "<":
            self.direction = Direction.LEFT

    def SortKey(self):
        return f"{self.x:03}{self.y:03}"

    def TurnLeft(self):
        if self.direction == Direction.UP:
            self.direction = Direction.LEFT
        elif self.direction == Direction.LEFT:
            self.direction = Direction.DOWN
        elif self.direction == Direction.DOWN:
            self.direction = Direction.RIGHT
        elif self.direction == Direction.RIGHT:
            self.direction = Direction.UP

    def TurnRight(self):
        if self.direction == Direction.UP:
            self.direction = Direction.RIGHT
        elif self.direction == Direction.LEFT:
            self.direction = Direction.UP
        elif self.direction == Direction.DOWN:
            self.direction = Direction.LEFT
        elif self.direction == Direction.RIGHT:
            self.direction = Direction.DOWN

    def Move(self, grid):
        if self.direction == Direction.DOWN:
            self.y += 1
        elif self.direction == Direction.UP:
            self.y -= 1
        elif self.direction == Direction.LEFT:
            self.x -= 1
        elif self.direction == Direction.RIGHT:
            self.x += 1
        # print(f"  x: {self.x}  y: {self.y}")
        chr = grid[self.y][self.x]
        # print(f" = {chr}")
        if chr == "+":
            if self.step == 0:
                # turn left
                self.TurnLeft()
            elif self.step == 1:
                # go straight
                # nothing to do
                pass
            elif self.step == 2:
                # turn right
                self.TurnRight()

            self.step += 1
            self.step = self.step % 3
        elif chr == "/":
            if self.direction == Direction.UP:
                self.direction = Direction.RIGHT
            elif self.direction == Direction.DOWN:
                self.direction = Direction.LEFT
            elif self.direction == Direction.LEFT:
                self.direction = Direction.DOWN
            elif self.direction == Direction.RIGHT:
                self.direction = Direction.UP
        elif chr == "\\":
            if self.direction == Direction.UP:
                self.direction = Direction.LEFT
            elif self.direction == Direction.DOWN:
                self.direction = Direction.RIGHT
            elif self.direction == Direction.LEFT:
                self.direction = Direction.UP
            elif self.direction == Direction.RIGHT:
                self.direction = Direction.DOWN

    def __repr__(self):
        return f"{self.x},{self.y} - {self.direction} {self.step} {self.SortKey()}"

class Day13Solution(Aoc):

    def Run(self):
        self.StartDay(13, "Mine Cart Madness")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(13)

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
        /->-\\
        |   |  /----\\
        | /-+--+-\  |
        | | |  | v  |
        \-+-/  \-+--/
        ..\------/
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return "7,3"

    def TestDataB(self):
        self.inputdata.clear()
        # self.TestDataA()    # If test data is same as test data for part A
        testdata = \
        """
        />-<\\
        |   |
        | /<+-\\
        | | | v
        \>+</ |
        ..|   ^
        ..\<->/
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return "6,4"

    def BuildGrid(self):
        rows = len(self.inputdata)
        cols = max(len(line) for line in self.inputdata)
        print(f"{cols},{rows}")

        grid = [[" " for y in range(cols)] for x in range(rows)]
        carts = []

        for y in range(rows):
            for x in range(cols):
                if x >= len(self.inputdata[y]):
                    continue
                c = self.inputdata[y][x]
                if c in "v^<>":
                    cart = Cart(c, x, y)
                    carts.append(cart)
                if c in "<>":
                    c = "-"
                if c in "v^":
                    c = "|"
                if c == ".":
                    c = " "
                grid[y][x] = c

        return grid, carts

    def CheckCollision(self, carts):
        posses = []
        for cart in carts:
            p = (cart.x, cart.y)
            if p in posses:
                return f"{cart.x},{cart.y}"
            posses.append(p)
        return None

    def CheckCollisionAndRemove(self, carts):
        posses = {}
        for cart in carts:
            if cart.removed:
                continue
            p = (cart.x, cart.y)
            if p in posses:
                cart.removed = True
                posses[p].removed = True
            posses[p] = cart

    def PrintGrid(self, grid):
        for line in grid:
            for c in line:
                print(c, end="")
            print("")

    def PartA(self):
        self.StartPartA()

        grid, carts = self.BuildGrid()

        # self.PrintGrid(grid)
        # for cart in carts:
        #     print(cart)

        answer = None

        while True:
            carts.sort(key=lambda c: c.SortKey())
            for cart in carts:
                cart.Move(grid)
                c = self.CheckCollision(carts)
                if c is not None:
                    answer = c
                    break
            if answer is not None:
                break

        # Attempt 1 = 68,62 is wrong
        # Attempt 2 = 26,92 is correct

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        grid, carts = self.BuildGrid()
        answer = None

        while True:
            carts.sort(key=lambda c: c.SortKey())
            for cart in carts:
                if cart.removed:
                    continue
                cart.Move(grid)
                self.CheckCollisionAndRemove(carts)

            active_carts = [cart for cart in carts if cart.removed == False]
            # print(active_carts)
            if answer is None and len(active_carts) == 1:
                answer = f"{active_carts[0].x},{active_carts[0].y}"

            if answer is not None:
                break

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day13Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

