# Python program for implementation of Selection
# Sort
import sys

def selectionSort(A):
    for i in range(len(A)-1):
                
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
                
        # Swap the found minimum element with
        # the first element		
        A[i], A[min_idx] = A[min_idx], A[i]

# Driver code to test above
A = [64, 25, 12, 22, 11, 3, 14]
print ("Sorted array")
selectionSort(A)
print(A)
