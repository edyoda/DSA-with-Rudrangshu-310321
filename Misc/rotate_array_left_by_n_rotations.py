# d is number of rotations
def rotateLeftRecursive(d, arr):
    # Write your code here
    if d == 1:
        return arr
    l = len(arr)
    if d > l:
        return arr
    
    temp = arr[0]
    for i in range(l-1):
        arr[i] = arr[i+1]

    arr[l-1] = temp
   
    return rotateLeft(d-1, arr)

def rotateLeft(d, arr):
    # Write your code here
    
    list = arr
    for i in range(d):
        list.append(arr[i])

    return list[d:]
   
def rotateLeftV(arr, k):

    new_arr=[]
    for i in range(len(arr)-1,k-1,-1):
        new_arr.append(arr[i])
    for i in range(k):
        new_arr.append(arr[i])
    
    print(new_arr)

arr = [1, 2, 3, 4, 5, 6, 7, 8]
d = 3
rotateLeftV(arr, d)
#print(res)