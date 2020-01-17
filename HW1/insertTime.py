# Harinder Gakhal
# 1/11/20
import random
import time

def insertSort(arr):
	for i in range(1, len(arr)):
		j = i
		while j > 0 and arr[j-1] > arr[j]:
			temp = arr[j-1]
			arr[j-1] = arr[j]
			arr[j] = temp
			j -= 1

	return arr

for n in range(5000, 40000, 5000):
	myArr = []
	for x in range(n):
		myArr.append(random.randint(0, 10000))
	timeStart = time.time()
	insertSort(myArr)
	print("Array Size:", len(myArr), "\tTime:" , '%.3f'%(time.time() - timeStart), "seconds")