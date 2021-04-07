# A single node of a singly linked list
class Node:
  # constructor
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

# A Linked List class with a single head node
class LinkedList:
  def __init__(self):  
    self.head = None
  
  # This function is defined in Linked List class
  # Appends a new node at the end. This method is
  # defined inside LinkedList class shown above */
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

# Function to reverse the linked list
  def reverse(self):
    prev = None
    current = self.head
    while(current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next
    self.head = prev

if __name__=='__main__':
  
    llist = LinkedList()
  
    llist.append(5)
    llist.append(7)
    llist.append(10)
    llist.append(9)
    llist.append(21)
    llist.append(13)

    llist.printLL()
    llist.reverse()
    print("\nAfter reversal")
    llist.printLL()
    
  
