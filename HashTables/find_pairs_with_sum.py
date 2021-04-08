# Python 3 implementation of simple method
# to find count of pairs with given sum.
import sys

# Returns number of pairs in arr[0..n-1]
# with sum equal to 'sum'


def getPairsCount(arr, n, sum):

	m = [0] * 1000

	# Store counts of all elements in map m
	for i in range(0, n):
		m[arr[i]] += 1

	twice_count = 0

	# Iterate through each element and increment
	# the count (Notice that every pair is
	# counted twice)
	for i in range(0, n):

		twice_count += m[sum - arr[i]]

		# if (arr[i], arr[i]) pair satisfies the
		# condition, then we need to ensure that
		# the count is decreased by one such
		# that the (arr[i], arr[i]) pair is not
		# considered
		if (sum - arr[i] == arr[i]):
			twice_count -= 1

	# return the half of twice_count
	return int(twice_count / 2)

def findPairsWithMap(arr, sum):
	map = dict()
	for i in arr:
		if i not in map.keys():
			map[i] = 1
		else:
			map[i]+= 1

	s = set()
	for j in arr:
		k = sum - j
		if k in map.keys():
			pair = (j, k)
			
			if j not in s and k not in s:
				s.add(j)
				s.add(k)
				print("Pair found {}".format(pair))	

# Driver function
arr = [3,7,9,12,5,11,23,15,11]
n = len(arr)
sum = 22

#print("Count of pairs is", getPairsCount(arr,n, sum))
print(findPairsWithMap(arr, sum))

