CC=gcc -std=gnu11

hw3: main.o parse.o printSummary.o maxVal.o
	$(CC) -o hw3 main.o parse.o printSummary.o maxVal.o
main.o: main.c main.h
	$(CC) -c main.c
parse.o: parse.c main.h
	$(CC) -c parse.c
printSummary.o: printSummary.c main.h
	$(CC) -c printSummary.c
maxVal.o: maxVal.c main.h
	$(CC) -c maxVal.c
clean:
	rm -f *.o hw3
zip:
	zip hw3.zip main.c main.h Makefile parse.c printSummary.c maxVal.c data.txt README.txt
