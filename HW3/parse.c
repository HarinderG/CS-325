#include "main.h"

//reads knapsack data from 'data.txt' and stores in an array of Items
int parse(Item *items) {
	char buffer[MAX_INPUT_LENGTH]; //input buffer
	FILE *fp = fopen("./data.txt", "r"); //open 'data.txt' in read mode
	if(fp == NULL) { //check for file existence
		return 0;
	}
	
	//store data into the structure.
	int i = 0;
	while (fgets(buffer, MAX_INPUT_LENGTH, fp) != NULL && i < MAX_ITEMS) { //reads MAX_ITEMS lines at most
		//read data into current Item, assuming data is well-formatted
		sscanf(buffer, "%d %d %s", &items[i].weight, &items[i].value, items[i].name);
		i++;
	}
	
	//close file stream
	fclose(fp);
	return i; //return the amount of items read from the knapsack
}
