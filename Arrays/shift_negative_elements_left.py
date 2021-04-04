# Python3 program of the
# above approach

# Function to shift all the
# the negative elements to
# the left of the array
def shiftall(arr,left,right):

# Loop to iterate while the
# left pointer is less than
# the right pointer
    while left<=right:
        
        # Condition to check if the left
        # and right pointer negative
        if arr[left] < 0 and arr[right] < 0:
            left+=1
        
        # Condition to check if the left
        # pointer element is positive and
        # the right pointer element is
        # negative
        elif arr[left]>0 and arr[right]<0:
            arr[left], arr[right] = \
                    arr[right],arr[left]
            left+=1
            right-=1
        
        # Condition to check if the left
        # pointer is positive and right
        # pointer as well
        elif arr[left]>0 and arr[right]>0:
            right-=1
        else:
            left+=1
            right-=1
        
# Function to print the array
def display(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
print()

# Driver Code
if __name__ == "__main__":
    arr=[-12, 11, -13, -5, 6, -7, 5, -3, 11]
    n=len(arr)
    shiftall(arr,0,n-1)
    display(arr)

# Sumit Singh
