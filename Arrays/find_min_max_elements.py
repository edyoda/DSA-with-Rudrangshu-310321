# Python3 program to find minimum
# (or maximum) element in an array

# Minimum Function
def getMin(arr, n):
	res = arr[0]
	for i in range(1,n):
		res = min(res, arr[i])
	return res

# Maximum Function
def getMax(arr, n):
	res = arr[0]
	for i in range(1,n):
		res = max(res, arr[i])
	return res

# Driver Program
arr = [12, 1234, 45, 67, 1]
n = len(arr)
print ("Minimum element of array:", getMin(arr, n))
print ("Maximum element of array:", getMax(arr, n))

# This code is contributed
# by Shreyanshi Arun.
