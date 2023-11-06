from aoc import Aoc
import itertools
import math
import re
import sys

# Day 7
# https://adventofcode.com/2023

class Day7Solution(Aoc):

    def Run(self):
        self.StartDay(7, "The Sum of Its Parts")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(7)

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
        Step C must be finished before step A can begin.
        Step C must be finished before step F can begin.
        Step A must be finished before step B can begin.
        Step A must be finished before step D can begin.
        Step B must be finished before step E can begin.
        Step D must be finished before step E can begin.
        Step F must be finished before step E can begin.
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return "CABDFE"

    def TestDataB(self):
        self.inputdata.clear()
        self.TestDataA()    # If test data is same as test data for part A
        return 15

    def ParseInput(self):
        steps = []
        steps.clear()
        rx = re.compile("Step (?P<first>[A-Z]*) must be finished before step (?P<next>[A-Z]*) can begin.")
        for line in self.inputdata:
            match = rx.search(line)
            if match:
                first = match["first"]
                second = match["next"]
                steps.append((first, second))
        return steps

    def PartA(self):
        self.StartPartA()

        steps = self.ParseInput()
        # print(steps)

        todo = []
        for step in steps:
            if step[0] not in todo:
                todo.append(step[0])
            if step[1] not in todo:
                todo.append(step[1])

        # print("TODO", todo)

        execution = ""
        done = []
        available = []

        while len(todo) > 0:
            available.clear()
            for letter in todo:
                alldone = True
                for step in steps:
                    if step[1] == letter:
                        if step[0] not in done:
                            alldone = False
                            break
                if alldone:
                    available.append(letter)

            available.sort()
            first = available[0]
            execution += first
            done.append(first)
            todo.remove(first)

        self.partAresult = execution
        answer = execution

        self.ShowAnswer(answer)

    def FindNextToExecute(self, todo, completed, steps):
        for i in range(len(todo)):
            step = todo[i]
            available = True
            for s in steps:
                if s[1] == step:
                    if s[0] not in completed:
                        available = False
                        break
            if available:
                return step

        return None

    def PartB(self):
        self.StartPartB()

        steps = self.ParseInput()
        workercount = 5
        defaultstepduration = 60
        if len(steps) < 10:
            # We are using the testdata
            workercount = 2
            defaultstepduration = 0

        workers = [ [0, "."] for _ in range(workercount)]

        completed = []

        todo = []
        for ch in self.partAresult:
            todo.append(ch)
        todo.sort()

        ix = 0
        second = 0
        done = False
        while done == False:
            working = False
            while True:
                for w in range(len(workers)):
                    if workers[w][0] > 0:
                        workers[w][0] -= 1
                        if workers[w][0] == 0:
                            completed.append(workers[w][1])
                            workers[w][1] = "."
                            # print(f"Step {workers[w][1]} done by worker {w + 1} on second {second}")

                    if workers[w][0] == 0:
                        nextstep = self.FindNextToExecute(todo, completed, steps)
                        if nextstep is not None:
                            todo.remove(nextstep)
                            step = nextstep
                            # print(f"Worker {w + 1} starting {step} on second {second}")
                            stepduration = defaultstepduration + (ord(step) - 64)
                            workers[w] = [stepduration, step]

                    if workers[w][0] > 0:
                        working = True
                
                # check if there are free workers and if there are jobs available (L should start at 80, not 81)
                idle = 0
                for w in range(len(workers)):
                    if workers[w][0] == 0:
                        idle += 1
                nextstep = self.FindNextToExecute(todo, completed, steps)
                if idle > 0 and nextstep is not None:
                    pass
                else:
                    break

            if False:
                print(f"{second:4}", end = " ")
                for w in workers:
                    if w[1] == ".":
                        print("  /  ", end = " ")
                    else:
                        print(f"{w[1]}({w[0]:2})", end = " ")
                for ch in completed:
                    print(ch, end = "")
                print("")

            if len(todo) == 0 and not working:
                done = True
            else:
                second += 1

        # Attempt 1: 425 is too low
        # Attempt 2: 1116 is too high

        answer = second

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day7Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

