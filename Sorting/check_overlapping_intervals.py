
def sortTuple(tup): 
      
    # getting length of list of tuples
    lst = len(tup) 
    for i in range(0, lst): 
          
        for j in range(0, lst-i-1): 

            if (tup[j][0] > tup[j + 1][0]): 
                temp = tup[j] 
                tup[j]= tup[j + 1] 
                tup[j + 1]= temp 
    return tup

def checkOverlap(list):
    sortTuple(list)
    print(list)
    overlappedTuples = []

    for i in range(len(list)-1):
        if list[i][1] > list[i+1][0]:
            overlappedTuples.append(list[i])
            overlappedTuples.append(list[i+1])

    if (overlappedTuples):
        print("Overlapping intervals exist.")
        print(overlappedTuples)

# Driver programs

arr = [(1, 3), (6, 8), (12, 13), (5, 10), (13, 16)]
checkOverlap(arr)
