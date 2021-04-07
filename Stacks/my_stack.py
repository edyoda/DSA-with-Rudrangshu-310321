class Stack:

    def __init__(self):
        self.stack = []

    def push(self, dataval):
# Use list append method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
# Use peek to look at the top of the stack

    def peek(self):     
	    return self.stack[-1]

    def remove(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()

    def isEmpty(self):
        return len(self.stack)==0