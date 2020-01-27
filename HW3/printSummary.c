//This program implements the knapsack problem
#include "main.h"

//displays possible contents of knapsack and optimal solution
void printSummary(Item *items, int itemCount, int weightCapacity, Result result) {
	printf(" Weight\tValue\tName\n");
	printf(" ------\t-----\t----\n");
	
	for(int i = 0; i < itemCount; i++){ //iterate over Items in inventory
		printf(" %4d\t%4d\t%s\n", items[i].weight, items[i].value, items[i].name);
	}
	
	printf("----------------------\n");
	printf("Bag's capacity: %d\n", weightCapacity);
	printf("Item count: %d\n", itemCount);
	printf("Maximum Value: $%d\n", result.value);
	
	//print items if they are used in the optimal solution
	for (int i = 0; i < itemCount; i++) {
		if (result.counts[i] != 0) {
			printf("Item #%d (%s): %d\n", i+1, items[i].name, result.counts[i]);
		}
	}
}
