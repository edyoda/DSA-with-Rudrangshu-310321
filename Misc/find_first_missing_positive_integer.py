"""
 Input:  {2, 3, 7, 6, 8, -1, -10, 15}
 Output: 1

 Input:  { 2, 3, -7, 6, 8, 1, -10, 15 }
 Output: 4

 Input: {1, 1, 0, -1, -2}
 Output: 2 
 """

def findMax(arr):
    m = -1
    for item in arr:
        m = max(m, item)

    return m

def findMissing(arr):
    max = findMax(arr)
    posArr = []

    for i in range(0,max+1):
        posArr.append(0)

    for item in arr:
        if item > 0:
            posArr[item] = 1

    missing = -1
    for i in range(1,len(posArr)):
        if posArr[i] == 0:
            missing = i
            break

    if missing == -1:
        missing = len(posArr)
    return missing

def findMissSw(arr):
    for i in range(len(arr)):
        if i not in arr and i>0:
            print(i)
            break


# Driver program
list1 = [2, 3, 7, 6, 8, -1, -10, 15]
print("First missing positive Integer in List1")
print(findMissSw(list1))
list2 = [2, 3, -7, 6, 8, 1, -10, 15]
print("First missing positive Integer in List2")
print(findMissSw(list2))
list3 = [1, 1, 0, -1, -2]
print("First missing positive Integer in List3")
print(findMissSw(list3))