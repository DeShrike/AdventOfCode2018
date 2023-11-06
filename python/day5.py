from aoc import Aoc
import itertools
import math
import re
import sys

# Day 5
# https://adventofcode.com/2023

class Day5Solution(Aoc):

    def Run(self):
        self.StartDay(5, "Alchemical Reduction")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(5)

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
        dabAcCaCBAcCcaDA
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 10

    def TestDataB(self):
        self.inputdata.clear()
        self.TestDataA()    # If test data is same as test data for part A
        return 4

    def React(self, polymer):
        changed = True
        while changed:
            # print(len(polymer))
            l = len(polymer)
            for i in range(1, 26 + 1):
                r1 = chr(i + 64) + chr(i + 96)
                r2 = chr(i + 96) + chr(i + 64)
                polymer = polymer.replace(r1, "")
                polymer = polymer.replace(r2, "")
            
            changed = l != len(polymer)

        return polymer

    def PartA(self):
        self.StartPartA()

        polymer = self.inputdata[0]
        polymer = self.React(polymer)

        answer = len(polymer)

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        polymer = self.inputdata[0]
        shortest = len(polymer)
        for i in range(1, 26 + 1):
            r1 = chr(i + 64)
            p = polymer.replace(r1, "")
            r2 = chr(i + 96)
            p = p.replace(r2, "")
            pp = self.React(p)
            if len(pp) < shortest:
                shortest = len(pp)

        answer = shortest

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day5Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

