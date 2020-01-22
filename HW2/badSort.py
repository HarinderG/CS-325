# # Harinder Gakhal
# # 1/21/20

import math
import numpy as np

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

def sortArrays():
	out = open("bad.out", "w")
	with open("data.txt") as data:
		for line in data:
			line_int = list(map(int, line.split()))
			out.write(' '.join(map(str, badSort(np.array(line_int[1:]), float(float(2)/3)))))
			out.write('\n')
	out.close()
	data.close()

sortArrays()