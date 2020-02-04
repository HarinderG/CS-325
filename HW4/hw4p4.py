# Harinder Gakhal
# HW4 Problem 4
# 2/3/20

import sys

ans = [[],[]];					# Make 2D array to hold denominations and quantities
def coinAlgo(coins, ammount):
	if ammount == 0:
		return 0;
	# Recursively find the optimal set.
	for i in range(len(coins) - 1, -1, -1):
		coin = coins[i - 1];
		if ammount >= coin:
			if coin not in ans[0]:
				ans[0].append(coin);
				ans[1].append(1);
			else:
				ans[1][ans[0].index(coin)] += 1;
			return 1 + coinAlgo(coins, ammount - coin);

	print("Greedy algorithm will not work for this set.");
	return 0;

# The parse function will read from data.txt and write out to change.txt
def parse():
	orig_stdout = sys.stdout;		# Used to redirect stdout
	out = open("change.txt", "w");
	sys.stdout = out;		# Redirect stdout to file 'out'
	with open("data.txt") as data:	# Read file line by line
		for line in data:
			lineList = list(map(int, line.split()));
			del ans[0][:];	# Reset the 2D array
			del ans[1][:];
			coinAlgo(buildArr(lineList[0], lineList[1]), lineList[2]);	# Call coinAlgo() to find optimal change
			for i in range(0, len(ans[0])):
				print(ans[0][i], "\t", ans[1][i]);
			print("----------");
	sys.stdout = orig_stdout;
	out.close();
	data.close();

# buildArr() is used to build the array based on c to the power of k
def buildArr(c, k):
	arr = [];
	for i in range(0, k+1):
		arr.append(c**i);
	return arr;

parse();