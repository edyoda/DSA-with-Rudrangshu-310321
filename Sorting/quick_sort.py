# Python program for implementation of Quicksort Sort

def partition(arr, low, high):
	pIndex = (low)		 # index of smaller element
	pivot = arr[high]	 # pivot

	for j in range(low, high):

		# If current element is smaller than or
		# equal to pivot
		if arr[j] <= pivot:

			# increment index of smaller element
			arr[pIndex], arr[j] = arr[j], arr[pIndex]
			pIndex += 1

	arr[pIndex], arr[high] = arr[high], arr[pIndex]
	return (pIndex)

# Function to do Quick sort
def quickSort(arr, low, high):
	if len(arr) == 1:
		return arr
	if low < high:

		# pi is partitioning index, arr[p] is now
		# at right place
		pi = partition(arr, low, high)

		# Separately sort elements before
		# partition and after partition
		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
	print(arr[i], end=" "),

