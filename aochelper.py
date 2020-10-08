import time

# Helper methods

## Global Data

_day = 0
_start = 0
inputdata = []

## Ansi Colors

Reversed = u"\u001b[7m"
DimBackground = u"\u001b[5m"
Reset = u"\u001b[0m"
BrightBlack =   u"\u001b[30;1m"
BrightRed =     u"\u001b[31;1m"
BrightGreen =   u"\u001b[32;1m"
BrightYellow =  u"\u001b[33;1m"
BrightBlue =    u"\u001b[34;1m"
BrightMagenta = u"\u001b[35;1m"
BrightCyan =    u"\u001b[36;1m"
BrightWhite =   u"\u001b[37;1m"

BlackBackground =   u"\u001b[40m"
RedBackground =     u"\u001b[41m"
GreenBackground =   u"\u001b[42m"
YellowBackground =  u"\u001b[43m"
BlueBackground =    u"\u001b[44m"
MagentaBackground = u"\u001b[45m"
CyanBackground =    u"\u001b[46m"
WhiteBackground =   u"\u001b[47m"

## Methods

def StartDay(day):
	global _day
	_day = day
	print(f"{DimBackground} {BrightWhite}Day {BrightYellow}{_day} {Reset}")

def ReadInput():
	inputdata.clear()
	file = open(InputFilename(), "r")
	for line in file:
		inputdata.append(line.strip())
	file.close()

def InputFilename():
	return f"input-day{_day}.txt"

def StartPartA():
	global _start
	print("")
	print(f"{BrightWhite}Part {BrightCyan}A{Reset}")
	_start = time.time()

def StartPartB():
	global _start
	print("")
	print(f"{BrightWhite}Part {BrightCyan}B{Reset}")
	_start = time.time()

def ShowAnswer(result):
	end = time.time()
	ellapsed = end - _start
	print(f"Answer: {BrightGreen}{result}{Reset} took {BrightMagenta}{ellapsed:.5f}{Reset} seconds")

## Main

if __name__ == "__main__":
	StartDay(6)
	print(InputFilename())
	StartPartA()
	ShowAnswer(42)
	StartPartB()
	ShowAnswer("Hello")
