#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//constants for use everywhere
#define MAX_INPUT_LENGTH 120
#define MAX_ITEMS 128

//structure to represent an item type
typedef struct item Item;
struct item {
	int weight;
	int value;
	char name[MAX_INPUT_LENGTH];
};

//structure to represent an optimal collection
typedef struct result Result;
struct result {
	int value;
	int counts[MAX_ITEMS];
};

//prototypes for parse.c, maxVal.c, and printSummary.c
int parse(Item *);
Result MaxVal(Item *, int, int, Result*);
void printSummary(Item *, int, int, Result);
