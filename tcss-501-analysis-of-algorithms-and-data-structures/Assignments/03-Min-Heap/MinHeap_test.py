import unittest
from MinHeap import MinHeap

class TestMinHeap(unittest.TestCase):

    def setUp(self):
        self.heap = MinHeap()

    def test_insert(self):
        self.heap.insert(5)
        self.heap.insert(3)
        self.heap.insert(8)
        self.heap.insert(1)
        self.assertEqual(self.heap.peek(), 1)

    def test_pop(self):
        self.heap.insert(5)
        self.heap.insert(3)
        self.heap.insert(8)
        self.heap.insert(7)
        self.heap.insert(90)
        self.heap.insert(12)
        self.heap.insert(2)
        self.heap.insert(1)
        self.assertEqual(self.heap.pop(), 1)
        self.assertEqual(self.heap.pop(), 2)
        self.assertEqual(self.heap.pop(), 3)
        self.assertEqual(self.heap.pop(), 5)
        self.assertEqual(self.heap.pop(), 7)

    def test_peek(self):
        self.assertIsNone(self.heap.peek())
        self.heap.insert(5)
        self.assertEqual(self.heap.peek(), 5)
        self.heap.insert(3)
        self.assertEqual(self.heap.peek(), 3)
        self.heap.insert(8)
        self.assertEqual(self.heap.peek(), 3)
        self.heap.insert(1)
        self.assertEqual(self.heap.peek(), 1)

    def test_clear(self):
        self.heap.insert(5)
        self.heap.insert(3)
        self.heap.insert(8)
        self.heap.insert(1)
        self.heap.clear()
        self.assertIsNone(self.heap.peek())
        self.assertIsNone(self.heap.root.data)

    def test_bubble_up(self):
        # This method is usually tested indirectly through insert
        self.heap.insert(5)
        self.heap.insert(3)
        self.heap.insert(8)
        self.heap.insert(1)
        self.assertEqual(self.heap.peek(), 1)

    def test_bubble_down(self):
        # This method is usually tested indirectly through pop
        self.heap.insert(5)
        self.heap.insert(3)
        self.heap.insert(8)
        self.heap.insert(1)
        self.heap.pop()
        self.assertEqual(self.heap.peek(), 3)

if __name__ == '__main__':
    unittest.main()