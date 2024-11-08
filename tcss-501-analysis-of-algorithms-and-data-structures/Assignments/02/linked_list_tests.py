import unittest
from linked_list_and_queue import LinkedList

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()

    def test_init(self):
        self.assertIsNone(self.ll.first)
        self.assertIsNone(self.ll.last)
        self.assertEqual(self.ll.count, 0)
        self.assertEqual(self.ll.char_count, 0)

    def test_append(self):
        self.ll.append("test")
        self.assertEqual(self.ll.first.data, "test")
        self.assertEqual(self.ll.last.data, "test")
        self.assertEqual(self.ll.count, 1)

    def test_size(self):
        self.ll.append("test")
        self.assertEqual(self.ll.size(), 1)

    def test_iter(self):
        self.ll.append("test1")
        self.ll.append("test2")
        self.assertEqual(list(self.ll.iter()), ["test1", "test2"])

    def test_delete(self):
        self.ll.append("test1")
        self.ll.append("test2")
        self.ll.delete("test1")
        self.assertEqual(list(self.ll.iter()), ["test2"])
        self.assertEqual(self.ll.count, 1)

    def test_contains(self):
        self.ll.append("test")
        self.assertTrue(self.ll.contains("test"))
        self.assertFalse(self.ll.contains("not_in_list"))

    def test_search(self):
        self.ll.append("test")
        node = self.ll.search("test")
        self.assertIsNotNone(node)
        self.assertEqual(node.data, "test")

    def test_clear(self):
        self.ll.append("test")
        self.ll.clear()
        self.assertIsNone(self.ll.first)
        self.assertIsNone(self.ll.last)
        self.assertEqual(self.ll.char_count, 0)
    
    def test_char_count_empty_list(self):
        self.assertIsNone(self.ll.charCount(aggregated=True))
        self.assertIsNone(self.ll.charCount(aggregated=False))

    def test_char_count_aggregated_true(self):
        self.ll.append("hello")
        self.ll.append("world")
        self.assertEqual(self.ll.charCount(aggregated=True), 10)

    def test_char_count_aggregated_false(self):
        self.ll.append("hello")
        self.ll.append("world")
        self.assertEqual(list(self.ll.charCount()), [5, 5])
        
    def test_reverse_empty_list_in_place(self):
        self.ll.reverse(in_place=True)
        self.assertIsNone(self.ll.first)
        self.assertIsNone(self.ll.last)

    def test_reverse_empty_list_not_in_place(self):
        self.ll.reverse(in_place=False)
        self.assertIsNone(self.ll.first)
        self.assertIsNone(self.ll.last)

    def test_reverse_in_place(self):
        self.ll.append("a")
        self.ll.append("b")
        self.ll.append("c")
        self.ll.reverse(in_place=True)
        self.assertEqual(list(self.ll.iter()), ["c", "b", "a"])

    def test_reverse_not_in_place(self):
        self.ll.append("a")
        self.ll.append("b")
        self.ll.append("c")
        self.ll.reverse(in_place=False)
        self.assertEqual(list(self.ll.iter()), ["c", "b", "a"])
        

if __name__ == '__main__':
    unittest.main()