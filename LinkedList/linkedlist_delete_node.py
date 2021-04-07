from linkedlist import Node
from linkedlist import LinkedList

def deleteNode(linkedlist, key):
    if linkedlist.head is None:
        print("Linked List is empty")
        return

    temp = linkedlist.head
    prev = None 
    found = False
    while(temp is not None):
        if temp.data == key:
            found = True
            break
                
        prev = temp
        temp = temp.next

    if found:
        prev.next = temp.next
        temp.data = None
        temp.next = None


# Driver program
llist = LinkedList()
llist.append(4)
llist.append(5)
llist.append(7)
llist.append(8)
llist.append(9)

print("-----Before delete-----")
llist.printLL()
deleteNode(llist, 7)
length = llist.length()
print("\n------After delete------")
llist.printLL()


