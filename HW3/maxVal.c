#include "main.h"

//recursively computes the optimal amount of each item
//that can fit in a knapsack with a given capacity
//caches results for better performance
Result MaxVal(Item *items, int weightCapacity, int itemCount, Result * valueCache) {
	if(weightCapacity <= 0) { //base case
		return valueCache[weightCapacity];
	}
	
	if (valueCache[weightCapacity].value != 0) { //check cache for previously computed solution
		return valueCache[weightCapacity];
	}
	
	//running trackers of optimal solution
	int bestValue = 0; //value of best solution
	int bestIndex = 0; //index of item used for best solution
	Result bestResult; //result from MaxVal(weightCapacity - item) for best item
	
	for (int i = 0; i < itemCount; i++) { //iterate over possible items
		int currentValue;
		Result currentResult;
		if(weightCapacity >= items[i].weight) { //don't bother calculating impossible values
			//calculate maximum value, given that current item is in bag
			currentResult = MaxVal(items, weightCapacity - items[i].weight, itemCount, valueCache);
			currentValue = items[i].value + currentResult.value;
		}
		
		if(currentValue > bestValue) { //we have a new winner!
			bestValue = currentValue;
			bestIndex = i;
			bestResult = currentResult;
		}
	}
	
	//populate result of current weight with that of previous weight
	for (int i = 0; i < itemCount; i++) {
		valueCache[weightCapacity].counts[i] = bestResult.counts[i];
	}
	
	valueCache[weightCapacity].counts[bestIndex]++; //increment winning item's count
	valueCache[weightCapacity].value = bestValue; //set result's value to best
	return valueCache[weightCapacity];
}
