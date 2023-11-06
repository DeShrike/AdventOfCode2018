from aoc import Aoc
import itertools
import math
import re
import sys

# Day 12
# https://adventofcode.com/2023

class Day12Solution(Aoc):

    def Run(self):
        self.StartDay(12, "Subterranean Sustainability")
        self.ReadInput()
        self.PartA()
        # self.PartB()

    def Test(self):
        self.StartDay(12)

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
        initial state: #..#.#..##......###...###

        ...## => #
        ..#.. => #
        .#... => #
        .#.#. => #
        .#.## => #
        .##.. => #
        .#### => #
        #.#.# => #
        #.### => #
        ##.#. => #
        ##.## => #
        ###.. => #
        ###.# => #
        ####. => #
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 325

    def TestDataB(self):
        self.inputdata.clear()
        self.TestDataA()    # If test data is same as test data for part A
        return None

    def ParseInput(self):
        self.rules.clear()
        self.pots.clear()

        stufing = 3

        initial = self.inputdata[0][15:]
        self.offset = len(initial) * stufing
        for i in range(len(initial) * stufing):
            self.pots.append(0)
        for ch in initial:
            if ch == '#':
                self.pots.append(1)
            else:
                self.pots.append(0)
        for i in range(len(initial)):
            self.pots.append(0)

        for i in range(2, len(self.inputdata)):
            line = self.inputdata[i]
            parts = line.split(" => ")
            rule =  [ (1 if x == "#" else 0) for x in parts[0]]
            self.rules.append( (rule, 1 if parts[1] == "#" else 0) )

    def CopyNewToPots(self, newpots):
        for i in range(len(self.pots)):
            self.pots[i] = newpots[i]

    def CheckPot(self, pos):
        plant = 0
        for rule in self.rules:
            foundrule = True
            for i in range(5):
                ii = i - 2
                if self.pots[pos + ii] == rule[0][i]:
                    pass
                else:
                    foundrule = False
                    break
            if foundrule:
                plant = rule[1]
                break

        return plant

    def ShowPots(self, gen):
        print(f"#{gen}:", end = "")
        for p in self.pots:
            print("#" if p == 1 else ".", end = "")
        print("")
        # xxx = input()

    def DoGeneration(self, gen):

        newpots = [ 0 for _ in range(len(self.pots))]
        for pos in range(2, len(self.pots) - 2):
            plant = self.CheckPot(pos)
            newpots[pos] = plant
        
        self.CopyNewToPots(newpots)

        # if gen % 1000 == 0:
        #	ShowPots(gen)

    def CountPots(self):
        som = 0
        for ix, p in enumerate(self.pots):
            if p == 1:
                som += (ix - self.offset)
        return som

    def PartA(self):
        self.StartPartA()

        self.rules = []
        self.pots = []
        self.offset = 0

        self.ParseInput()

        generations = 20
        for g in range(generations):
            self.DoGeneration(g)

        som = self.CountPots()

        answer = som

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        self.rules = []
        self.pots = []
        self.offset = 0

        self.ParseInput()

        prevsom = 0
        generations = 320
        for g in range(generations):
            self.DoGeneration(g)
            som = self.CountPots()
            print(f"#{g}\t{som}\t{som - prevsom}")
            prevsom = som
            if self.pots[0] == 1 or self.pots[1] == 1 or self.pots[-1] == 1 or self.pots[-2] == 1:
                break

        self.ShowPots(0)

        answer = 0

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day12Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

