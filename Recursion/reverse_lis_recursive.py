# Recursive python program to reverse an array

# Function to reverse A[] from start to end
def reverseList(A, start, end):
	if start >= end:
		return
	A[start], A[end] = A[end], A[start]
	reverseList(A, start+1, end-1)

# Driver function to test above function
A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A, 0, 5)
print("Reversed list is")
print(A)
# This program is contributed by Pratik Chhajer
