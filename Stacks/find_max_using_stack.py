from my_stack import Stack

def findMax(arr):
    stack = Stack()
    for elem in arr:
        if stack.isEmpty():
            stack.push(elem)
        else:
            if stack.peek() < elem:
                stack.push(elem)
            
    return stack.remove()

def findSecondMax(arr):
    stack = Stack()
    for elem in arr:
        if stack.isEmpty():
            stack.push(elem)
        else:
            if stack.peek() < elem:
                stack.push(elem)
            else:
                temp = stack.remove()
                if stack.peek() < elem:
                    stack.remove()
                    stack.push(elem)
                stack.push(temp)
    
    stack.remove()     
    return stack.remove()

#Driver program

list = [1, 4, 5, 23, 6, 17, -5, 6, 12, 34, 71, 32]
max = findMax(list)
secondMax = findSecondMax(list)
print("max = {}".format(max))
print("second max ={}".format(secondMax))