from aoc import Aoc
import itertools
import math
import re
import sys

# Day 1
# https://adventofcode.com/2023

class Day1Solution(Aoc):

    def Run(self):
        self.StartDay(1, "Chronal Calibration")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(1)

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
        7
        7
        -2
        -7
        -4
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

    def PartA(self):
        self.StartPartA()

        answer = 0
        for m in self.inputdata:
            answer += int(m)

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        loop = 0
        answer = 0
        history = {}
        found = False
        while found == False:
            loop += 1
            # print(loop, total, len(history), end = "\r")
            for m in self.inputdata:
                answer += int(m)
                if answer in history:
                    found = True
                    break
                history[answer] = True

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day1Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

