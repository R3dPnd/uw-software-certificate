import unittest
from RedBlackBST import RedBlackBST

class TestRedBlackBST(unittest.TestCase):

    def setUp(self):
        self.bst = RedBlackBST()

    def test_insert_single_value(self):
        self.bst.insert_i(1, 'one')
        result = self.bst.search(1)
        self.assertEqual(result, 'one', f"Expected 'one', but got {result}")

    def test_insert_multiple_values(self):
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for value in values:
            self.bst.insert_i(value, value)
        for value in values:
            result = self.bst.search(value)
            self.assertEqual(result, value, f"Expected {value}, but got {result}")

    def test_update_existing_key(self):
        self.bst.insert_i(100, 'one-hundred')
        self.bst.insert_i(100, 'one hundred')
        result = self.bst.search(100)
        self.assertEqual(result, 'one hundred', f"Expected 'one hundred', but got {result}")

    def test_search_non_existent_key(self):
        result = self.bst.search(999)
        self.assertIsNone(result, f"Expected None, but got {result}")

    def test_insert_and_search_edge_cases(self):
        self.bst.insert_i(-1, 'negative one')
        self.bst.insert_i(0, 'zero')
        self.bst.insert_i(1, 'one')
        self.assertEqual(self.bst.search(-1), 'negative one', "Expected 'negative one'")
        self.assertEqual(self.bst.search(0), 'zero', "Expected 'zero'")
        self.assertEqual(self.bst.search(1), 'one', "Expected 'one'")

    def test_color_properties(self):
        self.bst.insert_i(10, 'ten')
        self.bst.insert_i(20, 'twenty')
        self.bst.insert_i(30, 'thirty')
        root = self.bst.root
        self.assertFalse(root.is_red, "Root should be black")
        self.assertTrue(not root.right.is_red, "Right child of root should not be red")
        self.assertEqual(root.value, 'twenty', "Root is 20")

if __name__ == '__main__':
    unittest.main()