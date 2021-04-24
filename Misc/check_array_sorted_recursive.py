# Recursive approach to check if an
# Array is sorted or not

# Function that returns 0 if a pair
# is found unsorted


def arraySortedOrNot(arr):
	
	n = len(arr)
	
	if n == 1 or n == 0:
		return True

	return arr[0] <= arr[1] and arraySortedOrNot(arr[1:])

arr = [20, 23, 23, 45, 78, 88]

# Displaying result
if arraySortedOrNot(arr):
	print("Yes")
else:
	print("No")
