from aoc import Aoc
import itertools
import math
import re
import sys

# Day 14
# https://adventofcode.com/2023

class Day14Solution(Aoc):

    def Run(self):
        self.StartDay(14, "AOC")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(14)

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
        9
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return "5158916779"

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

    def PartA(self):
        self.StartPartA()

        steps = int(self.inputdata[0])
        reci = [ 3, 7 ]
        e1 = 0
        e2 = 1
        while len(reci) < steps + 10:
            n = str(reci[e1] + reci[e2])
            for c in n:
                reci.append(int(c))
            e1 += reci[e1] + 1
            e2 += reci[e2] + 1
            e1 = e1 % len(reci)
            e2 = e2 % len(reci)
            # print(reci)
            # a = input()
        answer = ""
        for ri in reci[steps:steps + 10]:
            answer += str(ri)

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        # Add solution here

        answer = None

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day14Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

