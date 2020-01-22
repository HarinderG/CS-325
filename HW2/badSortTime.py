# # Harinder Gakhal
# # 1/21/20

import math
import numpy as np
import time
import random

def badSort(arr, alpha):
	n = len(arr)
	if ((n == 2) and (arr[0] > arr[1])):
		arr[0] , arr[1] = arr[1] , arr[0]
	elif n > 2:
		if alpha == float(float(2)/3):
			m = int(math.ceil(alpha * n))
		elif alpha == float(float(3)/4):
			m = int(math.floor(alpha * n))
		badSort(arr[:m], alpha)
		badSort(arr[n-m:n], alpha)
		badSort(arr[:m], alpha)
	return arr

print("Alpha = 2/3")
for n in range(100, 800, 100):
	myArr = []
	for x in range(n):
		myArr.append(random.randint(0,10000))
	timeStart = time.time()
	badSort(np.array(myArr), float(float(2)/3))
	print("Array Size:", len(myArr), "\tTime:" , '%.3f'%(time.time() - timeStart), "seconds")

print("Alpha = 3/4")
for n in range(100, 800, 100):
	myArr = []
	for x in range(n):
		myArr.append(random.randint(0,10000))
	timeStart = time.time()
	badSort(np.array(myArr), float(float(3)/4))
	print("Array Size:", len(myArr), "\tTime:" , '%.3f'%(time.time() - timeStart), "seconds")
