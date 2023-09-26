class Node:
    """
    An object for storing a single node in a linked list

    Attributes:
        data: Data stored in node
        next_node: Reference to next node in linked list
    """

    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return "<Node data: %s>" % self.data

class SinglyLinkedList:
    """
    Linear data structure that stores values in nodes. The list maintains a reference to the first node, also called head. Each node points to the next node in the list

    Attributes:
        head: The head node of the list
    """

    def __init__(self):
        self.head = None
        # Maintaining a count attribute allows for len() to be implemented in
        # constant time
        self.__count = 0

    def is_empty(self):
        """
        Determines if the linked list is empty
        Takes O(1) time
        """

        return self.head is None

    def node_at_index(self, index):
        """
        Returns the Node at specified index
        Takes O(n) time
        """

        if index >= self.__count:
            raise IndexError('index out of range')

        if index == 0:
            return self.head

        current = self.head
        position = 0

        while position < index:
            current = current.next_node
            position += 1

        return current

    def __len__(self):
        """
        Returns the length of the linked list
        Takesn O(1) time
        """

        return self.__count
    
    def size(self):
        """
        Returns the length of the linked list
        Takesn O(1) time
        """

        return self.__count
    
    def add(self, data):
        """
        Adds new Node containing data to head of the list
        Also called prepend
        Takes O(1) time
        """

        new_head = Node(data, next_node=self.head)
        self.head = new_head
        self.__count += 1

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return  '-> '.join(nodes)

# Global function to split a list in two halves
# The implementation from the freeCodeCamp tutorial has a problem that after splitting a linked list, if you attempt to get the length of the splitted list you will get incorrect result. 
def split(linked_list):
    """
    Divides the linked list in 2 halves
    Returns left list and right list after division
    """
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size//2
        mid_node = linked_list.node_at_index(mid-1)

        left_half = linked_list #Source of error in getting the length of the splitted list. Try performing to get the size of the splitted list after split.
        right_half = SinglyLinkedList() #Source of error in getting the length of the splitted list
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half
    

l = SinglyLinkedList()
l.add(2)
l.add(1)
l.add(68)
l.add(45)
print(l)
print(len(l))
#print(size(l))
print(l.size())
left_half, right_half = split(l)
print(f"Left_half -> {left_half}")
print(f"Right_half -> {right_half}")
print(f"Length of left_half: {len(left_half)}")
print(f"Length of left_half: {len(right_half)}")
print(f"Size of left_half: {left_half.size()}")
