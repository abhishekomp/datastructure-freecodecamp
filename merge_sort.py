def merge_sort(list):
  """
  Sorts a list in ascending order.
  Returns a new sorted list.
  
  Divide: Find the midpoint of the list and divide into sublists
  Conquer: Recursively sort the sublists created in previous step
  Combine: Merge the sorted sublists created in the previous step

  Takes overall O(n log n) time
  """

  if len(list) <= 1:
    return list
  
  left_half, right_half = split(list)
  left = merge_sort(left_half)
  right = merge_sort(right_half)

  return merge(left, right)

# LP: A function returning 2 values
def split(list):
  """
  Divide the unsorted list at the midpoint into sublists
  Returns two sublists - left and right

  Takes overall O(log n) time
  Caveat: For python, slicing takes time hence it will be more than O(log n)
  """
  # LP: Floor Division
  mid = len(list)//2
  # LP: List slicing
  left_list = list[:mid]
  right_list = list[mid:]

  return left_list, right_list

def merge(left, right):
  """
  Merges two lists (arrays), sorting them in the process
  Returns a new merged list

  Takes overall O(n) time
  """

  l = []
  i = 0
  j = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      l.append(left[i])
      i += 1
    else:
      l.append(right[j])
      j += 1
    
  while i < len(left):
    l.append(left[i])
    i += 1
  
  while j < len(right):
    l.append(right[j])
    j += 1

  return l

# alist = [54, 62, 93, 25, 15, 30, 60, 90]
# l = merge_sort(alist)
# print(l)


alist = [54, 62, 93, 25, 15, 30, 60, 90, 100]
sorted_list = merge_sort(alist)
print(sorted_list)

def verify_sorted(list):
  """
  Checks if a list of integers is sorted or not
  Returns True if sorted else False
  """
  n = len(list)
  if n == 0 or n == 1:
    return True
  
  return list[0] < list[1] and verify_sorted(list[1:])

print(verify_sorted(alist))
print(f"Sorted list: {sorted_list}")
print(verify_sorted(sorted_list))
