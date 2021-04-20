class Data:
    def __init__(self, value, index, count=0):
        self.value = value
        self.index = index
        self.count = count
 
 
# Custom sort by element's frequency and index
def customSort(arr):
    if arr is None or len(arr) < 2:
        return
 
    hm = {}
 
    # for each array element, insert into the dictionary
    # its frequency and index of its first occurrence in the array
    for i in range(len(arr)):
        hm.setdefault(arr[i], Data(arr[i], i)).count += 1
 
    # get the values
    values = [*hm.values()]
 
    '''
        Sort the values based on a custom comparator
 
        1. If two elements have different frequencies, then
        the one which has more frequency should come first.
 
        2. If two elements have the same frequencies, then the
        one which has less index should come first.
    '''
 
    values.sort(key=lambda x: (-x.count, x.index))
 
    k = 0
    for data in values:
        for j in range(data.count):
            arr[k] = data.value
            k += 1
 
 
if __name__ == '__main__':
 
    arr = [3, 3, 1, 1, 1, 8, 3, 6, 8, 7, 8]
    customSort(arr)
    print(arr)