from MyLinkedList import Node, SinglyLinkedList
node = Node(20)
#print(node)

l = SinglyLinkedList()
l.add(10)
l.add(20)
l.add(30)
l.add(40)
l.add(50)
l.add(60)
print(l)
#print(f"Searching a node in the list: {l.search(20)}")
#print(f"Searching a node in the list: {l.search(10)}")

# Length (size) of the linked list
#print(f"Size: {len(l)}")

# Get the data from the head node
#print(f"Head data: {l.getHead()}")

# Get node data from specified index
#When list is empty, return None
l = SinglyLinkedList()
l.add(10)
l.add(50)
l.add(70)
print(f"Data at index: {l.node_at_index(2)}")


# Remove head node
# print(f"Removed head: {l.removeHead()}")
# print(l)

# Insert a new node at requested index
# inserted_Node = l.insertAt(600, 6)
# node = l.node_at_index(6)
# print(f"Node is: {node}")
# print(inserted_Node)
# print(l)

# Get iterator
# iterator = iter(l)
# for item in iterator:
#   print(item)

# Sublist
# l = SinglyLinkedList()
# l.add(10)
# l.add(20)
# l.add(30)
# l.add(40)
# l.add(50)
# l.add(60)
# print(l)
# print(l.sublist(0, 1))  #[Head: 60]-> [Tail: 50]
# print(l.sublist(2, 6))  #Blank list
#print(l.sublist(7, 6))  #Blank list
#print(l.sublist(1, 9))  #Blank list
#print(l.sublist(4, 5))  #[Head: 20]-> [Tail: 10]

