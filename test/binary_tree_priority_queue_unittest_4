import unittest
from binary_tree_priority_queue_4 import PriorityQueue


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.priority_queue = PriorityQueue()

    def test_insert_single_element(self):
        self.priority_queue.insert("Task 1", 3)
        self.assertEqual(self.priority_queue.root.value, "Task 1")
        self.assertIsNone(self.priority_queue.root.left_child)
        self.assertIsNone(self.priority_queue.root.right_child)

    def test_delete_highest_priority_from_empty_queue(self):
        deleted_item = self.priority_queue.delete_highest_priority()
        self.assertIsNone(deleted_item)

    def test_insert_and_delete_element(self):
        self.priority_queue.insert("Task 1", 3)
        self.assertEqual(self.priority_queue.root.value, "Task 1")
        deleted_item = self.priority_queue.delete_highest_priority()
        self.assertEqual(deleted_item, "Task 1")
        self.assertIsNone(self.priority_queue.root)


if __name__ == '__main__':
    unittest.main()
