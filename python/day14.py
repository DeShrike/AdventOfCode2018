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
        testdata = \
        """
        92510
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 18

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
        answer = ""
        for ri in reci[steps:steps + 10]:
            answer += str(ri)

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        steps = str(self.inputdata[0])
        l = len(steps)
        reci = [ 3, 7 ]
        e1 = 0
        e2 = 1
        answer = 0
        while True:
            n = str(reci[e1] + reci[e2])
            for c in n:
                reci.append(int(c))
            e1 += reci[e1] + 1
            e2 += reci[e2] + 1
            e1 = e1 % len(reci)
            e2 = e2 % len(reci)
            answer += 1

            if len(reci) > l:
                lastx = reci[-l:]
                # print(reci)
                lastxstr = "".join([str(x) for x in lastx])
                # print(answer, lastx, lastxstr)
                if lastxstr == steps:
                    print(answer, lastx, lastxstr)
                    break
                # a = input()
        answer -= 1

        # Attempt 1: 15538187 is too low
        # Attempt 2: 132671793 is too high

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day14Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

