def findMaximum(arr, low, high):

	if low == high:
		return arr[low]

	
	if high == low + 1 and arr[low] >= arr[high]:
		return arr[low]

	
	if high == low + 1 and arr[low] < arr[high]:
		return arr[high]

	mid = (low + high)//2 #low + (high - low)/2;*/

	
	if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
		return arr[mid]

	
	if arr[mid] > arr[mid + 1] and arr[mid] < arr[mid - 1]:
		return findMaximum(arr, low, mid-1)
	else: 
		return findMaximum(arr, mid + 1, high)

# Driver program to check above functions */
arr = [1, 3, 50, 10, 9, 7, 6]
n = len(arr)
print ("The maximum element is %d"% findMaximum(arr, 0, n-1))

