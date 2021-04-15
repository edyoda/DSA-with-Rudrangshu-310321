# Python program to do inorder traversal without recursion

# A binary tree node
class Node:
	
	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# Iterative function for inorder tree traversal
def inOrder(root):
	
	# Set current to root of binary tree
	current = root
	stack = [] # initialize stack
		
	while 1:
		
		if (current):
			stack.append(current)		
			current = current.left

		elif(stack):
			current = stack.pop()
			print(current.data, end=" ") 
			current = current.right

		else:
			break
	
	print()


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inOrder(root)

