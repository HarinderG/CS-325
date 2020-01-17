# Harinder Gakhal
# 1/11/20
import random
import time

timeStart = time.time()

def insertSort(arr):
	for i in range(1, len(arr)):
		j = i
		while j > 0 and arr[j-1] > arr[j]:
			temp = arr[j-1]
			arr[j-1] = arr[j]
			arr[j] = temp
			j -= 1

	return arr

# sortArrays() reads in arrays from file data.txt, sorts each one, then puts the results into insert.out
def sortArrays():
	out = open("insert.out", "w")
	with open("data.txt") as data:
		for line in data:
			line_int = list(map(int, line.split()))
			out.write(' '.join(map(str, insertSort(line_int[1:]))))
			out.write('\n')
	out.close()
	data.close()

sortArrays()