class Node:
  # constructor
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

# A Linked List class with a single head node
class LinkedList:
  def __init__(self):  
    self.head = None
  
  def append(self, new_data):
    new_node = Node(new_data)

    if self.head is None:
        self.head = new_node
        return

    last = self.head
    while (last.next is not None):
      last = last.next

    last.next = new_node
  
  def length(self):
    temp = self.head
    count = 0 
    while(temp is not None):
      temp = temp.next
      count +=1

    return count

  # print method for the linked list
  def printLL(self):
    current = self.head
    while(current):
      print(current.data, end='=>')
      current = current.next

  def deleteNode(self, temp, pos):

      if temp is None:
          temp = self.head
      pos -= 1
      prev = temp
      temp = temp.next

      if pos == 1:
          prev.next = temp.next
          temp.data = None
          temp.next = None
          return
      
      self.deleteNode(temp, pos)
      

#Driver program
ll = LinkedList()
ll.append(1)
ll.append(4)
ll.append(6)
ll.append(2)
ll.append(11)

ll.printLL()
print("\nAfter delete...")
ll.deleteNode(None, 3)
ll.printLL()