# Efficient Python3 program to find first
# non-repeating element.
from collections import defaultdict

def firstNonRepeating(arr, n):
	mp = defaultdict(lambda:0)

	# Insert all array elements in hash table
	for i in range(n):
		mp[arr[i]] += 1

	# Traverse array again and return
	# first element with count 1.
	for i in range(n):
		if mp[arr[i]] == 1:
			return arr[i]
	return -1

# Driver Code
arr = [9, 4, 9, 6, 7, 4]
n = len(arr)
print(firstNonRepeating(arr, n))

# This code is contributed by Shrikant13
