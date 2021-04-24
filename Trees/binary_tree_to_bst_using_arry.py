# Program to convert binary tree to BST

# A binary tree node
class Node:
	
	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# Helper function to store the inroder traversal of a tree
def storeInorder(root, inorder):	
	if root is None:
		return
	
	storeInorder(root.left, inorder)
	
	inorder.append(root.data)

	storeInorder(root.right, inorder)

# A helper funtion to count nodes in a binary tree
def countNodes(root):
	if root is None:
		return 0

	return countNodes(root.left) + countNodes(root.right) + 1

# Helper function that copies contents of sorted array
# to Binary tree
def arrayToBST(arr, root):	
	if root is None:
		return	
	
	arrayToBST(arr, root.left)
	
	root.data = arr[0]
	arr.pop(0)
	
	arrayToBST(arr, root.right)

# This function converts a given binary tree to BST
def binaryTreeToBST(root):
	
	# Base Case: Tree is empty
	if root is None:
		return
	
	n = countNodes(root)

	arr = []
	storeInorder(root, arr)
	
	# Sort the array
	arr.sort()

	arrayToBST(arr, root)

# Print the inorder traversal of the tree
def printInorder(root):
	if root is None:
		return
	printInorder(root.left)
	print(root.data)
	printInorder(root.right)

# Driver program to test above function
root = Node(10)
root.left = Node(30)
root.right = Node(15)
root.left.left = Node(20)
root.right.right = Node(5)

# Convert binary tree to BST
binaryTreeToBST(root)

print("Following is the inorder traversal of the converted BST")
printInorder(root)

