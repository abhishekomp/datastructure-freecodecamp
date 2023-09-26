from MyLinkedList import SinglyLinkedList

def merge_sort(list:SinglyLinkedList):
  """
  Sorts a list in ascending order.
  Returns a new sorted list.
  
  Divide: Find the midpoint of the list and divide into sublists
  Conquer: Recursively sort the sublists created in previous step
  Combine: Merge the sorted sublists created in the previous step

  """

  if len(list) <= 1:
    return list
  
  left_half, right_half = split(list)
  left = merge_sort(left_half)
  right = merge_sort(right_half)

  return merge(left, right)

def split(list):
  mid = len(list)//2
  left_list = list.sublist(0, mid-1)
  right_list = list.sublist(mid, len(list)-1)
  return left_list, right_list

def merge(left, right):
    """
    Merges two linked lists, sorting by data in nodes
    Returns a new merged list
    Takes O(n) space
    Runs in O(n) time
    """

    # Create a new linked list that contains nodes from merging left and right
    merged = SinglyLinkedList()
    # Add a fake head that is discarded later.
    merged.add(0)
    # Set current to the head of the linked list
    current = merged.head

    # Obtain head nodes for left and right linked lists
    left_head = left.head
    right_head = right.head

    # Iterate over left list and right list as long until the tail node of both
    # left and right
    while left_head or right_head:
        # If the head node of left is None, we're at the tail
        # Add the tail node from right to the merged linked list
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
l.add(50)
l.add(20)
l.add(15)
l.add(80)
l.add(100)
l.add(70)
print(l)
left_half, right_half = split(l)
print(left_half)
print(right_half)
print(merge_sort(l))
