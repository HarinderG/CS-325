# Harinder Gakhal
# 1/11/20
import random
import time

def mergeSort(arr):
	if len(arr) > 1:			# if array length is 1, return it
		mid = len(arr)//2		# Split array in half
		left = arr[:mid]
		right = arr[mid:]

		mergeSort(left)	# Recursively sort left and right side
		mergeSort(right)

		i, j, k = 0, 0, 0

		while i < len(left) and j < len(right):		# Sort both sides and place into correct positions
			if left[i] < right[j]:
				arr[k] = left[i]
				i+=1
			else:
				arr[k] = right[j]
				j+=1
			k+=1

		while i < len(left):
			arr[k] = left[i]
			i+=1
			k+=1

		while j < len(right):
			arr[k] = right[j]
			j+=1
			k+=1

	return arr 					# return the final array

for n in range(5000, 40000, 5000):
	myArr = []
	for x in range(n):
		myArr.append(random.randint(0,10000))
	timeStart = time.time()
	mergeSort(myArr)
	print("Array Size:", len(myArr), "\tTime:" , '%.3f'%(time.time() - timeStart), "seconds")