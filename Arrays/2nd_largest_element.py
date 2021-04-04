# Maximum Function
def getMaxAndSecondMax(arr, n):
    large_1 = 0 
    large_2 = 0    
      
    for i in range(0,n):
        if arr[i] > large_1:
            large_1 = arr[i]
        elif arr[i] > large_2:
            large_2 = arr[i]

    print("1st largest num in arr is {}, 2nd largest is {}".format(large_1, large_2))


# Driver program
arr = [12, 4, 78, 42, 56, 2, 5, 16, 8]
n = len(arr)
getMaxAndSecondMax(arr, n)

