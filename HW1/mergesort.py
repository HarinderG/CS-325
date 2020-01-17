# Harinder Gakhal
# 1/11/20
import random
import time

timeStart = time.time()

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

# sortArrays() reads in arrays from file data.txt, sorts each one, then puts the results into merge.out
def sortArrays():
	out = open("merge.out", "w")
	with open("data.txt") as data:
		for line in data:
			lineList = list(map(int, line.split()))
			out.write(' '.join(map(str, mergeSort(lineList[1:]))))
			out.write('\n')
	out.close()
	data.close()

sortArrays()