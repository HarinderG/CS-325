#include "main.h"

void main(int argc, char const *argv[]) {
	int weightCapacity; //maximum capacity of the given bag
	Item items[MAX_ITEMS]; //items read from data.txt

	if (argc != 2) { //ensure that one command line argument is given
		printf("Please enter weight capacity.\n");
		return;
	}
	
	int ret = sscanf(argv[1], "%d", &weightCapacity);
	if(ret != 1 || weightCapacity < 1 || weightCapacity > 1024) { //check if first arg is a valid int
		printf("Please enter valid weight capacity.\n");
		return;
	}
	
	Result valueCache[weightCapacity+1]; //return values of MaxVal cached here, index 0 useless
	for (int i = 0; i < weightCapacity+1; i++) { //initialize cache
		valueCache[i].value = 0;
		for (int j = 0; j < MAX_ITEMS; j++) {
			valueCache[i].counts[j] = 0;
		}
	}
	
	int itemCount = parse(items); //parse data.txt
	if (itemCount == 0) { //fail on no items in file or file not found
		printf("Could not find any items.\n");
		return;
	}
	
	Result result = MaxVal(items, weightCapacity, itemCount, valueCache); //calculate final result
	printSummary(items, itemCount, weightCapacity, result); //output final result
}
