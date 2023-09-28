class Node:
  """
    An object for storing a single node in a linked list

    Attributes:
        data: Data stored in node
        next_node: Reference to next node in linked list
  """
  def __init__(self, data, next_node=None):
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
      Returns True if empty else False
      Takes O(1) time
      """
      return self.head is None

    def __len__(self):
      """
      Returns the length of the linked list
      Invoked as len(list_object)
      Takes n O(1) time
      """
      #print(f">>>>>>>Calculating length of the list:")
      return self.__count
    
    def add(self, data):
      """
      Adds new Node containing data to head of the list
      Also called prepend
      #Returns the new node created
      Takes O(1) time
      """
      new_head = Node(data, next_node=self.head)
      self.head = new_head
      self.__count += 1
      #return new_head
    
    def search(self, key):
      """
      Search for the first node containing data that matches the key
      Returns the node or `None` if not found
      Takes O(n) time
      """
      if self.is_empty():
        #raise Exception('List is empty')
        return None
      current = self.head
      while current:
        if current.data == key:
          return current
        else:
          current = current.next_node
      return None

    def getHead(self):
       """
       Returns the data from the head node
       """
       if self.head:
         return self.head.data
       return None
    
    def node_at_index(self, index):
       """
       Returns the node at specified index
       Return None if index is invalid for the specified list
       """
       if index < 0:
          raise ValueError('Index cannot be negative')
       if self.is_empty() or index >= len(self):
          return None
       else:
          current = self.head
          count = 0
          while current:
             if index == count:
                return current
             else:
                current = current.next_node
                count += 1
          return None
       
    def removeHead(self):
       """
       Removes head element
       Returns the removed node
       """
       if self.is_empty():
          return None
       head = self.head
       self.head = self.head.next_node
       self.__count -= 1
       return head
    
    def insertAt(self, data, insertAtIndex):
       """
       If a node exists at specified index -1, then insert a new node after it
       If there is no node at the specified index - 1, then return None
       Returns the added node
       """
       if insertAtIndex == 0:
          self.add(data)
          self.__count += 1
          return self.head
       else:
        node_at_index = self.node_at_index(insertAtIndex - 1)
        if node_at_index:
          new_node = Node(data)
          subsequent_node = node_at_index.next_node
          node_at_index.next_node = new_node
          new_node.next_node = subsequent_node
          #print(f"Returning new node: {new_node}")
          self.__count += 1
          return new_node
       return None
    
    def __iter__(self):
        """
        Returns an iterator for the list that can be iterated upon
        """
        current = self.head

        while current:
            yield current
            current = current.next_node
    
    def sublist(self, startIndex, endIndex):
       """
       Takes a startIndex and an endIndex
       Returns a new list which is a sublist of the main list starting from startIndex till endIndex (including endIndex)
       """
       #Check if the requested indices are in the allowed range of the current list
       l = SinglyLinkedList()
       if startIndex >= 0 and endIndex <= len(self) - 1 and startIndex <= endIndex:
          currentIndex = endIndex
          while currentIndex >= startIndex:
             l.add(self.node_at_index(currentIndex).data)
             currentIndex -= 1
       return l
    
    def removeAt(self, index):
       """
       Removes the node at the specified index
       Returns the removed node else None
       """
       if index >= len(self):
          return None
       if self.is_empty():
          return None
       if len(self) == 1:
          return self.removeHead()
       else:
         #print(f">>>>>>Removing from index: {index}")
         node = self.node_at_index(index - 1)
         nodeToRemove = node.next_node
         if nodeToRemove.next_node:
            node.next_node = nodeToRemove.next_node
         else:
            node.next_node = None
         self.__count -= 1
         return nodeToRemove       

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



    
