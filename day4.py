from aochelper import *
import math
import re

# https://adventofcode.com/2018

#########################################
#########################################

records = []

#########################################
#########################################

class Record():
    def __init__(self, line, rx, rxBegin, rxSleep, rxWake):
        self.day = 0
        self.month = 0
        self.year = 0
        self.hour = 0
        self.minute = 0
        self.action = 0
        self.guard = 0
        self.begin = False
        self.wake = False
        self.sleep = False

        match = rx.search(line)
        if match:
            self.year = int(match["year"])
            self.month = int(match["month"])
            self.day = int(match["day"])
            self.hour = int(match["hour"])
            self.minute = int(match["minute"])
            self.action = match["action"]

            matchb = rxBegin.search(self.action)
            if matchb:
                self.guard = int(matchb["guard"])
                self.begin = True

            matchs = rxSleep.search(self.action)
            if matchs:
                self.sleep = True

            matchw = rxWake.search(self.action)
            if matchw:
                self.wake = True
        else:
            print("Parse error: ", line)

    def __str__(self):
        value = f"[{self.year}-{self.month}-{self.day} {self.hour}:{self.minute}] "
        if self.begin:
            value += f"Guard #{self.guard} begins shift"
        elif self.wake:
            value += "Guard wakes up"
        elif self.sleep:
            value += "Guard falls asleep"
        return value

def ParseInput():
    rx = re.compile("\[(?P<year>[0-9]*)\-(?P<month>[0-9]*)\-(?P<day>[0-9]*) (?P<hour>[0-9]*):(?P<minute>[0-9]*)\] (?P<action>.*)")

    rxBegin = re.compile("Guard #(?P<guard>[0-9]*) begins shift")
    rxSleep = re.compile("falls asleep")
    rxWake = re.compile("wakes up")

    records.clear()
    for line in inputdata:
        c = Record(line, rx, rxBegin, rxSleep, rxWake)
        records.append(c)

def SortInput():
    records.sort(key = lambda x: x.year * 100_000_000 +
                                 x.month * 1_000_000 +
                                 x.day * 10_000 +
                                 x.hour * 100 +
                                 x.minute)

#########################################
#########################################

def TestDataA():
    inputdata.clear()
    inputdata.append("[1518-11-01 00:00] Guard #10 begins shift")
    inputdata.append("[1518-11-01 00:05] falls asleep")
    inputdata.append("[1518-11-01 00:25] wakes up")
    inputdata.append("[1518-11-01 00:30] falls asleep")
    inputdata.append("[1518-11-01 00:55] wakes up")
    inputdata.append("[1518-11-01 23:58] Guard #99 begins shift")
    inputdata.append("[1518-11-02 00:40] falls asleep")
    inputdata.append("[1518-11-02 00:50] wakes up")
    inputdata.append("[1518-11-03 00:05] Guard #10 begins shift")
    inputdata.append("[1518-11-03 00:24] falls asleep")
    inputdata.append("[1518-11-03 00:29] wakes up")
    inputdata.append("[1518-11-04 00:02] Guard #99 begins shift")
    inputdata.append("[1518-11-04 00:36] falls asleep")
    inputdata.append("[1518-11-04 00:46] wakes up")
    inputdata.append("[1518-11-05 00:03] Guard #99 begins shift")
    inputdata.append("[1518-11-05 00:45] falls asleep")
    inputdata.append("[1518-11-05 00:55] wakes up")

#########################################
#########################################

def NextDay(d, m):
    maxDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d += 1
    if d > maxDays[m - 1]:
        d = 1
        m += 1
    return d, m

def PartAandB():
    StartPartA()

    data = []
    guard = 0
    sleeping = False
    mins = []
    day = 0
    month = 0
    minute = 0
    for x in records:
        if x.begin:
            if guard != 0:
                data.append((guard, day, month, mins))
            if sleeping:
                print("Previous guard is still sleeping !! Must handle this")
            guard = x.guard
            sleeping = False
            mins = [0 for x in range(60)]
            day = x.day
            month = x.month
            minute = 0
            if x.hour == 23:
                day, month = NextDay(day, month)
        elif x.sleep:
            sleeping = True
            sleepstart = x.minute
            pass
        elif x.wake:
            sleeping = False
            for m in range(sleepstart, x.minute):
                mins[m] = 1
            pass

    if guard != 0:
        data.append((guard, day, month, mins))

    counts = {}
    for d in data:
        c = d[3].count(1)
        if d[0] in counts:
            counts[d[0]] += c
        else:
            counts[d[0]] = c

    sorted_counts = sorted(counts.items(), key = lambda x: x[1], reverse = True)
    # print(sorted_counts)

    selected_guard = sorted_counts[0][0]
    mins = [0 for x in range(60)]

    for d in data:
        if d[0] == selected_guard:
            for i in range(len(d[3])):
                if d[3][i] == 1:
                    mins[i] += 1
    most = 0
    mostminute = -1
    for i in range(len(mins)):
        if mins[i] > most:
            most = mins[i]
            mostminute = i

    print(f"Guard = #{selected_guard}")
    print(f"Minute = {mostminute}")
    ShowAnswer(selected_guard * mostminute)

    StartPartB()

    counts = {}
    for d in data:
        guard = d[0]
        mins = d[3]
        if guard in counts:
            perminute = counts[guard]
        else:
            perminute = [0 for x in range(60)]
            counts[guard] = perminute
        for i in range(len(mins)):
            perminute[i] += mins[i]

    fguard = 0
    fcount = 0
    fminute = 0
    for guard in counts.keys():
        perminute = counts[guard]
        for i in range(len(perminute)):
            if perminute[i] > fcount:
                fguard = guard
                fcount = perminute[i]
                fminute = i

    print(f"Guard = #{fguard}")
    print(f"Minute = {fminute}")

    ShowAnswer(fguard * fminute)

#########################################
#########################################

if __name__ == "__main__":
    StartDay(4)
    ReadInput()
    # TestDataA()
    ParseInput()
    SortInput()
    PartAandB()
    print("")
