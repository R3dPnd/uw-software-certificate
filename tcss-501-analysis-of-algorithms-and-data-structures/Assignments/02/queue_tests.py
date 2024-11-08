import unittest
from linked_list_and_queue import Deque

class TestDeque(unittest.TestCase):

    def setUp(self):
        self.deque = Deque()

    def test_add_front(self):
        self.deque.addFirst(1)
        self.assertEqual(self.deque.size, 1)
        self.assertEqual(self.deque.removeFirst(), 1)

    def test_add_rear(self):
        self.deque.addLast(1)
        self.assertEqual(self.deque.size, 1)
        self.assertEqual(self.deque.removeLast(), 1)

    def test_remove_front(self):
        self.deque.addFirst(1)
        self.deque.addFirst(2)
        self.assertEqual(self.deque.removeFirst(), 2)
        self.assertEqual(self.deque.removeFirst(), 1)
        self.assertTrue(self.deque.size == 0)

    def test_remove_rear(self):
        self.deque.addLast(1)
        self.deque.addLast(2)
        self.assertEqual(self.deque.removeLast(), 2)
        self.assertEqual(self.deque.removeLast(), 1)
        self.assertTrue(self.deque.size == 0)

    def test_is_empty(self):
        self.assertTrue(self.deque.size == 0)
        self.deque.addFirst(1)
        self.assertFalse(self.deque.size == 0)

    def test_size(self):
        self.assertEqual(self.deque.size, 0)
        self.deque.addFirst(1)
        self.assertEqual(self.deque.size, 1)
        self.deque.addLast(2)
        self.assertEqual(self.deque.size, 2)
        self.deque.removeFirst()
        self.assertEqual(self.deque.size, 1)
        self.deque.removeLast()
        self.assertEqual(self.deque.size, 0)

if __name__ == '__main__':
    unittest.main()