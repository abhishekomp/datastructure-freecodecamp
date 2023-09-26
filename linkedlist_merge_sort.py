from linked_list import SinglyLinkedList

# l = SinglyLinkedList()
# l.add(1)
# print(l)


def merge_sort(linked_list):
  """
  Sorts a linked list in ascending order
  - Recursively divide the linked list into sublists containing a single node
  - Repeatedly merge the sublists to produce sorted sublists until one remains
  
  Returns a sorted linked list

  Takes O(n log n) time
  Takes O(n) space
  """
  print(f">>>>merge_sort() called with linkedList: {linked_list} having size: {linked_list.size()}")
  if linked_list.size() == 1:
     return linked_list
  elif linked_list.head is None:
    return linked_list
  
  left_half, right_half = split(linked_list)
  print(f"left: {left_half}")
  print(f"right: {right_half}")
  left = merge_sort(left_half)
  right = merge_sort(right_half)

  return merge(left, right)

def split(linked_list):
    """
    Divide the unsorted list at midpoint into sublists
    Takes O(log n) time
    """
    if linked_list == None or linked_list.head.next_node == None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size//2
        print(f"mid: {mid}")
        mid_node = linked_list.node_at_index(mid-1)

        left_half = linked_list
        right_half = SinglyLinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half

def merge(left, right):
    """
    Merges two linked lists, sorting by data in nodes
    Returns a new merged list
    Takes O(n) space
    Runs in O(n) time
    """

    # Create a new linked list that contains nodes from merging left and right
    merged = SinglyLinkedList()
    # Add a fake head that is discarded later. As said, this makes the code easier
    merged.add(0)
    # Set current to the head of the linked list
    current = merged.head

    # Obtain head nodes for left and right linked lists
    left_head = left.head
    right_head = right.head

    # Iterate over left and right as long until we reach the tail node of both
    # left and right
    while left_head or right_head:
        # If the head node of left is None, we're at the tail
        # Add the tail node from right linked list to the merged linked list
        if left_head is None:
            current.next_node = right_head
            # Call next on right to set loop condition to False
            right_head = right_head.next_node 
        # If the head node of right is None, we're at the tail
        # Add the tail node from left to the merged linked list
        elif right_head is None:
            current.next_node = left_head
            # Call next on left to set loop condition to False
            left_head = left_head.next_node
        else:
            # Not at either tail node
            # Obtain node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data

            # If data on left is lesser than right set current to left node
            # Move left head to next node
            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node
            # If data on left is greater than right set current to right node
            # Move right head to next node
            else:
                current.next_node = right_head
                right_head = right_head.next_node

        # Move current to next node
        current = current.next_node

    # Discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head

    return merged

l = SinglyLinkedList()
l.add(10)
l.add(20)
l.add(44)
# l.add(15)
# l.add(200)

print(l)
print(l.size())

sorted_linked_list = merge_sort(l)
print(sorted_linked_list)


# left_half, right_half = split(l)
# print(f"Left half: {left_half}")
# print(f"Left half: {right_half}")
