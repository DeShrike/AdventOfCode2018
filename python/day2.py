from aoc import Aoc
import itertools
import math
import re
import sys

# Day 2
# https://adventofcode.com/2023

class Day2Solution(Aoc):

    def Run(self):
        self.StartDay(2, "Inventory Management System")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(2)

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
        abcdef
        bababc
        abbcde
        abcccd
        aabcdd
        abcdee
        ababab
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 12

    def TestDataB(self):
        self.inputdata.clear()
        # self.TestDataA()    # If test data is same as test data for part A
        testdata = \
        """
        abcde
        fghij
        klmno
        pqrst
        fguij
        axcye
        wvxyz
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return "fgij"

    def CountA(self, s):
        counts = {}
        for ch in s:
            if ch in counts:
                counts[ch] += 1
            else:
                counts[ch] = 1
        two = 0
        three = 0
        for k in counts.keys():
            if counts[k] == 2:
                two += 1
            elif counts[k] >= 3:
                three += 1

        two = min(1, two)
        three = min(1, three)
        # print(s, two, three)

        return two, three

    def CountDifference(self, s1, s2):
        d = 0
        cc = ""
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                d += 1
            else:
                cc += s1[i]
        return d, cc

    def PartA(self):
        self.StartPartA()

        total2 = 0
        total3 = 0
        for m in self.inputdata:
            two, three = self.CountA(m)
            total2 += two
            total3 += three

        answer = total2 * total3

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        aa = None
        bb = None

        for a in range(len(self.inputdata)):
            for b in range(len(self.inputdata)):
                if b == a:
                    continue
                diff, _ = self.CountDifference(self.inputdata[a], self.inputdata[b])
                if diff == 1:
                    print(self.inputdata[a], self.inputdata[b])
                    aa = self.inputdata[a]
                    bb = self.inputdata[b]

        _, answer = self.CountDifference(aa, bb)

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day2Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

