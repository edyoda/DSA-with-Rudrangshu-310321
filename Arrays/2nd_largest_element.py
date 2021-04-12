# Maximum Function
def getMaxAndSecondMax(arr, n):
    large_1 = 0
    large_2 = 0   
      
    for i in range(1,n):
        if arr[i] > large_1:
            large_2 = large_1
            large_1 = arr[i]
        elif arr[i] > large_2 and arr[i] != large_1:
            large_2 = arr[i]

    print("1st largest num in arr is {}, 2nd largest is {}".format(large_1, large_2))


# Driver program
arr = [1, 2, 5, 8, 12, 34, 45]
n = len(arr)
getMaxAndSecondMax(arr, n)

