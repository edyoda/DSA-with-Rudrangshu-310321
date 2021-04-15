# Print consecutive numbers from 1 to n using recursion

def recursivePrint(n):    
    if n==0:
        return
    recursivePrint(n-1)
    print(n)
    

recursivePrint(10)