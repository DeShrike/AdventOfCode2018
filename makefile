CC=gcc
AR=ar

all: day9

rmbin:
	rm day9

###################################00

day9: day9.o
	$(CC) -o day9 day9.o

day9.o: day9.c
	$(CC) -c -O3 day9.c

###################################00

clean:
	rm *.o
