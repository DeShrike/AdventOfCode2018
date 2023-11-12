from aoc import Aoc
import itertools
import math
import re
import sys

# Day 16
# https://adventofcode.com/2023

class Sample():
    def __init__(self):
        self.before = []
        self.after = []
        self.opcode = None
        self.A = None
        self.B = None
        self.C = None
        self.possibilities = 0

    def __repr__(self):
        return f"{self.before} -> {self.after} | {self.opcode} {self.A} {self.B} {self.C} | P: {self.possibilities}"


class Cpu():
    def __init__(self):
        self.opcodes = [
            ("addr", self.addr),  
            ("addi", self.addi), 
            ("mulr", self.mulr), 
            ("muli", self.muli), 
            ("banr", self.banr), 
            ("bani", self.bani), 
            ("borr", self.borr), 
            ("bori", self.bori), 
            ("setr", self.setr), 
            ("seti", self.seti),
            ("gtir", self.gtir), 
            ("gtri", self.gtri), 
            ("gtrr", self.gtrr), 
            ("eqir", self.eqir), 
            ("eqri", self.eqri), 
            ("eqrr", self.eqrr)
        ]
        self.reset()
    
    def reset(self):
        self.R0 = 0
        self.R1 = 0
        self.R2 = 0
        self.R3 = 0

    def set_reg(self, values) -> None:
        self.R0, self.R1, self.R2, self.R3 = values

    def execute(self, opcode: int, a: int, b: int, c: int) -> None:
        self.opcodes[opcode][1](a, b, c)

    def register(self, ix: int) -> int:
        if ix == 0:
            return self.R0
        elif ix == 1:
            return self.R1
        elif ix == 2:
            return self.R2
        elif ix == 3:
            return self.R3
        else:
            print(f"register: bad index: {ix}")

    def set_register(self, ix: int, value: int) -> None:
        if ix == 0:
            self.R0 = value
        elif ix == 1:
            self.R1 = value
        elif ix == 2:
            self.R2 = value
        elif ix == 3:
            self.R3 = value
        else:
            print(f"set_register: bad index: {ix}")

    def addr(self, a: int, b: int, c: int) -> None:
        self.set_register(c, self.register(a) + self.register(b))

    def addi(self, a: int, b: int, c: int) -> None:
        self.set_register(c, self.register(a) + b)

    def mulr(self, a: int, b: int, c: int) -> None:
        self.set_register(c, self.register(a) * self.register(b))

    def muli(self, a: int, b: int, c: int) -> None:
        self.set_register(c, self.register(a) * b)

    def banr(self, a: int, b: int, c: int) -> None:
        self.set_register(c, self.register(a) & self.register(b))

    def bani(self, a: int, b: int, c: int) -> None:
        self.set_register(c, self.register(a) & b)

    def borr(self, a: int, b: int, c: int) -> None:
        self.set_register(c, self.register(a) | self.register(b))

    def bori(self, a: int, b: int, c: int) -> None:
        self.set_register(c, self.register(a) | b)

    def setr(self, a: int, b: int, c: int) -> None:
        self.set_register(c, self.register(a))

    def seti(self, a: int, b: int, c: int) -> None:
        self.set_register(c, a)

    def gtir(self, a: int, b: int, c: int) -> None:
        self.set_register(c, 1 if a > self.register(b) else 0)

    def gtri(self, a: int, b: int, c: int) -> None:
        self.set_register(c, 1 if self.register(a) > b else 0)

    def gtrr(self, a: int, b: int, c: int) -> None:
        self.set_register(c, 1 if self.register(a) > self.register(b) else 0)

    def eqir(self, a: int, b: int, c: int) -> None:
        self.set_register(c, 1 if a == self.register(b) else 0)

    def eqri(self, a: int, b: int, c: int) -> None:
        self.set_register(c, 1 if self.register(a) == b else 0)

    def eqrr(self, a: int, b: int, c: int) -> None:
        self.set_register(c, 1 if self.register(a) == self.register(b) else 0)


class Day16Solution(Aoc):

    def Run(self):
        self.StartDay(16, "Chronal Classification")
        self.ReadInput()
        self.PartA()
        self.PartB()

    def Test(self):
        self.StartDay(16)

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
        Before: [3, 2, 1, 1]
        9 2 1 2
        After:  [3, 2, 2, 1]


        1 2 3 4
        1 2 3 4
        1 2 3 4
        """
        self.inputdata = [line.strip() for line in testdata.strip().split("\n")]
        return 1

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

    def TestOpcode(self, opcode: int, sample: Sample):
        cpu = Cpu()
        cpu.set_reg(sample.before)
        cpu.execute(opcode, sample.A, sample.B, sample.C)
        return cpu.R0 == sample.after[0] and cpu.R1 == sample.after[1] and cpu.R2 == sample.after[2] and cpu.R3 == sample.after[3]

    def TestSample(self, sample: Sample) -> None:
        for opcode in range(16):
            if self.TestOpcode(opcode, sample):
                sample.possibilities += 1

    def ParseInput(self):
        samples = []
        program = []
        i = 0
        mode = 0
        while i < len(self.inputdata):
            if mode == 0:
                l1 = self.inputdata[i]
                l2 = self.inputdata[i + 1]
                l3 = self.inputdata[i + 2]
                if len(l1) == 0:
                    mode = 1
                    i += 1
                else:
                    s = Sample()
                    parts = l2.split(" ")
                    s.opcode = int(parts[0])
                    s.A = int(parts[1])
                    s.B = int(parts[2])
                    s.C = int(parts[3])
                    
                    if l1[0:9] != "Before: [":
                        print(f"Line {i}: expecting 'Before'")
                        quit(1)
                    l1 = l1[9:-1].replace(" ", "")
                    s.before = [int(i) for i in l1.split(",")]

                    if l3[0:9] != "After:  [":
                        print(f"Line {i + 2}: expecting 'After'")
                        quit(1)
                    l3 = l3[9:-1].replace(" ", "")
                    s.after = [int(i) for i in l3.split(",")]

                    samples.append(s)

                    i += 4
            if mode == 1:
                l1 = self.inputdata[i]
                program.append(l1.split(" "))
                i += 1

        return samples, program

    def PartA(self):
        self.StartPartA()

        answer = 0

        samples, _ = self.ParseInput()
        for s in samples:
            # print(s)
            self.TestSample(s)
            # print(s)
            if s.possibilities >= 3:
                answer += 1

        # Attempt 1: 143 is too low
        # Attempt 2: 636 is correct

        self.ShowAnswer(answer)

    def PartB(self):
        self.StartPartB()

        # Add solution here

        answer = None

        self.ShowAnswer(answer)


if __name__ == "__main__":
    solution = Day16Solution()
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        solution.Test()
    else:
        solution.Run()

# Template Version 1.4

