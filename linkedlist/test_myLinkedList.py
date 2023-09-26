import unittest
from MyLinkedList import SinglyLinkedList


class TestMyLinkedList(unittest.TestCase):

  # To run this test method: python test_myLinkedList.py TestMyLinkedList.test_isEmpty_should_return_True_for_an_empty_list
  def test_isEmpty_should_return_True_for_an_empty_list(self):
    l = SinglyLinkedList()
    self.assertTrue(l.is_empty())
  
  # To run this test method: python test_myLinkedList.py TestMyLinkedList.test_isEmpty_should_return_False_for_a_nonempty_list
  def test_isEmpty_should_return_False_for_a_nonempty_list(self):
    l = SinglyLinkedList()
    l.add(10)
    self.assertTrue(l.is_empty())

  # To run this test method: python test_myLinkedList.py TestMyLinkedList.test_len_should_return_zero_for_empty_list
  def test_len_should_return_zero_for_empty_list(self):
    l = SinglyLinkedList()
    self.assertEqual(len(l), 0)
  
  # To run this test method: python test_myLinkedList.py TestMyLinkedList.test_len_should_not_return_zero_for_nonempty_list
  def test_len_should_not_return_zero_for_nonempty_list(self):
    l = SinglyLinkedList()
    l.add(10)
    l.add(20)
    self.assertEqual(len(l), 1)

  # To run this test method: python test_myLinkedList.py TestMyLinkedList.test_removeHead_should_return_None_for_empty_list
  def test_removeHead_should_return_None_for_empty_list(self):
    l = SinglyLinkedList()
    self.assertEqual(l.removeHead(), None)

  # To run this test method: python test_myLinkedList.py TestMyLinkedList.test_removeHead_should_return_head_as_None_for_singleNodeList
  def test_removeHead_should_return_head_as_None_for_singleNodeList(self):
    l = SinglyLinkedList()
    l.add(10)
    l.removeHead()
    self.assertEqual(l.head, None)
  
  # To run this test method: python test_myLinkedList.py TestMyLinkedList.test_removeHead_should_return_correct_head_for_multiNodeList
  def test_removeHead_should_return_correct_head_for_multiNodeList(self):
    l = SinglyLinkedList()
    l.add(10)
    l.add(20)
    l.removeHead()
    self.assertEqual(l.head.data, 10)

  # To run: python test_myLinkedList.py TestMyLinkedList.test_removeAt_zero_from_singleNodeList_should_return_empty_list
  def test_removeAt_zero_from_singleNodeList_should_return_empty_list(self):
    l = SinglyLinkedList()
    l.add(10)
    print(f"Size before removal: {len(l)}")
    removed_node = l.removeAt(0)
    print(f"Size after removal: {len(l)}")
    self.assertEqual(l.head, None)
    self.assertTrue(l.is_empty())
    self.assertEqual(removed_node.data, 10)
    self.assertEqual(len(l), 0)

  # To run this test method: python test_myLinkedList.py TestMyLinkedList.test_removeAt_should_return_None_for_empty_list
  def test_removeAt_should_return_None_for_empty_list(self):
    l = SinglyLinkedList()
    removed_node = l.removeAt(0)
    #print(f"Length after removal: {len(l)}")
    self.assertEqual(l.head, None)
    self.assertEqual(removed_node, None)
    self.assertEqual(len(l), 0)
  
  # To run this test method: python test_myLinkedList.py TestMyLinkedList.test_removeAt_should_return_the_correct_node_after_removal
  def test_removeAt_should_return_the_correct_node_after_removal(self):
    l = SinglyLinkedList()
    l.add(10)
    l.add(20)
    l.add(30)
    self.assertEqual(len(l), 3)
    removed_node = l.removeAt(1)
    #print(removed_node)
    self.assertEqual(l.head.data, 30)
    self.assertEqual(len(l), 2)
    self.assertEqual(removed_node.data, 20)
  
    # To run this test method: python test_myLinkedList.py TestMyLinkedList.test_removeAt_should_return_the_correct_node_after_removal_from_multiNodeList
  def test_removeAt_should_return_the_correct_node_after_removal_from_multiNodeList(self):
    l = SinglyLinkedList()
    l.add(10)
    l.add(20)
    l.add(30)
    l.add(25)
    l.add(12)
    print(f"List before removal: {l}")
    self.assertEqual(len(l), 5)
    removed_node = l.removeAt(2)
    print(removed_node)
    print(f"List after removal: {l}")
    self.assertEqual(l.head.data, 12)
    self.assertEqual(len(l), 4)
    self.assertEqual(removed_node.data, 30)

  # To run: python test_myLinkedList.py TestMyLinkedList.test_removeAt_should_return_None_when_list_size_is_less_than_requested_index
  def test_removeAt_should_return_None_when_list_size_is_less_than_requested_index(self):
    l = SinglyLinkedList()
    l.add(10)
    #print(f"Size before removal: {len(l)}")
    removed_node = l.removeAt(4)
    print(f"Size after removal: {len(l)}")
    self.assertEqual(l.head.data, 10)
    self.assertEqual(removed_node, None)
    self.assertEqual(len(l), 1)

  # To run: python test_myLinkedList.py TestMyLinkedList.test_iter_should_throw_StopIteration_when_next_is_invoked_on_iterator_for_empty_list
  def test_iter_should_throw_StopIteration_when_next_is_invoked_on_iterator_for_empty_list(self):
    l = SinglyLinkedList()
    #l.add(10)
    iterator = iter(l)
    #self.assertRaises(StopIteration, next(iterator))
    #print(next(iterator))
    with self.assertRaises(StopIteration):
      next(iterator)

  # To run: python test_myLinkedList.py TestMyLinkedList.test_iter_should_return_element_as_next_when_list_is_singleNodeList
  def test_iter_should_return_element_as_next_when_list_is_singleNodeList(self):
    l = SinglyLinkedList()
    l.add(10)
    iterator = iter(l)
    #self.assertRaises(StopIteration, next(iterator))
    #print(next(iterator))
    self.assertEqual(next(iterator).data, 10)
    # with self.assertRaises(StopIteration):
    #   next(iterator)

  def test_add(self):
    l = SinglyLinkedList()
    l.add(10)
    expected_head_data = 10
    self.assertEqual(l.head.data, expected_head_data)
  
  def test_dunder_len_should_return_correct_length_of_the_list(self):
    l = SinglyLinkedList()
    l.add(10)
    l.add(50)
    l.add(70)
    print(len(l))
  
  # To run the test case: python test_myLinkedList.py TestMyLinkedList.test_getHead_gives_correct_head
  def test_getHead_gives_correct_head(self):
    l = SinglyLinkedList()
    l.add(10)
    l.add(50)
    l.add(70)
    actual_headData = l.getHead()
    expected_headData = 70
    self.assertEqual(actual_headData, expected_headData)
  
  # To run the test case: python test_myLinkedList.py TestMyLinkedList.test_getHead_gives_correct_head_for_empty_list
  def test_getHead_gives_correct_head_for_empty_list(self):
    l = SinglyLinkedList()
    actual_headData = l.getHead()
    expected_headData = None
    self.assertEqual(actual_headData, expected_headData)
      
  def test_getNodeAtIndex_should_return_correct_node(self):
    wanted_index = 2
    l = SinglyLinkedList()
    l.add(10)
    l.add(50)
    l.add(70)
    node = l.node_at_index(wanted_index)
    expected_node_data = 10
    self.assertEqual(node.data, expected_node_data)

  def test_insertAt_should_add_a_new_node_at_index_zero(self):
    l = SinglyLinkedList()
    l.add(10)
    insertedNode = l.insertAt(20, 0)
    # After inserting at index 0, we should be able to verify that the correct node is available at index 0
    expected_node_data = insertedNode.data
    actual_node_data = l.head.data
    self.assertEqual(actual_node_data, expected_node_data)

  def test_insertAt_should_add_a_new_node_after_last_index(self):
    wanted_index = 3
    l = SinglyLinkedList()
    l.add(10)
    l.add(50)
    l.add(70)
    insertedNode = l.insertAt(100, wanted_index)
    expected_node_data = insertedNode.data
    actual_node_data = l.node_at_index(wanted_index).data
    self.assertEqual(actual_node_data, expected_node_data)
  
  #To run the test method: python test_myLinkedList.py TestMyLinkedList.test_insertAt_should_add_a_new_node_somewhere_in_between_head_and_tail
  def test_insertAt_should_add_a_new_node_somewhere_in_between_head_and_tail(self):
    insert_at_index = 2
    l = SinglyLinkedList()
    l.add(10)
    l.add(50)
    l.add(70)
    #[Head: 70]-> [50]-> [Tail: 10]
    print(l)
    insertedNode = l.insertAt(100, insert_at_index)
    print(l)
    expected_node_data = insertedNode.data
    actual_node_data = l.node_at_index(insert_at_index).data
    self.assertEqual(actual_node_data, expected_node_data)

# In order to run the test cases by running the module directly.
# Without this, we need to issue the command 'python -m unittest test_myLinkedList.py' to run the unit test cases.
if __name__ == '__main__':
  unittest.main()