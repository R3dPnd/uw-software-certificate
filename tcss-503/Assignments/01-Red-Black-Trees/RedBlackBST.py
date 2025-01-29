class RedBlackBST:
    """ A Python Implementation of a Red-Black Binary Search Tree
    """
    class RedBlackNode:
        """Basic node representing the Key/Value and color of a link/node.
        """
        def __init__(self, key, value):
            """Returns a newly created `RedBlackNode` initiated to be a "Red" link.
            :param key: The unique, comparable object by which to retrieve the desired value.
            :param value: The value in which to store in the `RedBlackBST` object.
            """
            self.key = key
            self.value = value
            self.left = None
            self.right = None
            self.parent = None
            self.is_red = True  # NEW NODES ARE ALWAYS RED IN THIS IMPLEMENTATION TO DEFAULT THEM TO BE SO.

        def __str__(self):
            """Returns a string representation of a node, including the ids and colors of its left and right links.
            The pattern used is: `(left.key)<-[Red|Black]--(node.key)--[Red|Black]->(right.key)
            If either left or right nodes are blank, the key is `None` and the link color defaults to `Black`.

            :return: String representation of the desired node.
            """
            l_node = "None" if self.left is None else self.left.key
            l_link = "Black" if self.left is None or not self.left.is_red else " Red "
            r_node = "None" if self.right is None else self.right.key
            r_link = "Black" if self.right is None or not self.right.is_red else " Red "
            p_node = "None" if self.parent is None else self.parent.key
            p_link = " Red " if self.is_red else "Black"
            return f"({l_node})<--[{l_link}]--({self.key})--[{r_link}]-->({r_node}) [Parent: ({p_node})]"

    def __init__(self):
        """Creates an empty `RedBlackBST` (Red-Black Binary Search Tree)
        """
        self.root = None

### THE FOLLOWING THREE METHOD STUBS REQUIRE COMPLETION FOR ASSIGNMENT

    def insert_i(self, key, value):
        """Insert the provided `value` at the provided `key` in the `RedBlackBST` using an iterative method.
        Assumes the key provided is a comparable object, and assumes uniqueness. If the `Key` already exists in the
        structure, the provided value will overwrite the previous value for this key.

        :param key: The unique, comparable object by which to retrieve the desired value.
        :param value: The value in which to store in the `RedBlackBST`
        :return: `None`
        """
        new_node = RedBlackBST.RedBlackNode(key, value)

        if self.root is None:
            self.root = new_node
            self.root.is_red = False
            return

        current = self.root
        stack = []

        while current is not None:
            stack.append(current)
            if key < current.key:
                if current.left is None:
                    current.left = new_node
                    new_node.parent = current
                    break
                current = current.left
            elif key > current.key:
                if current.right is None:
                    current.right = new_node
                    new_node.parent = current
                    break
                current = current.right
            else:
                current.value = value
                return

        while stack:
            node = stack.pop()
            if self._right_is_red(node) and not self._left_is_red(node):
                node = self._rotate_left_i(node)
            if self._left_left_is_red(node):
                node = self._rotate_right_i(node)
            if self._left_is_red(node) and self._right_is_red(node):
                self._flip_colors(node)

        self.root.is_red = False

    def _rotate_left_i(self, node):
        """Perform a `rotation_left` around the node provided. Return the new root of newly rotated local cluster.
        :param node: The node around which to rotate.
        :return: The new root that exists as a result of the rotation.
        """
        x = node.right
        node.right = x.left
        if x.left is not None:
            x.left.parent = node
        x.parent = node.parent
        if node.parent is None:
            self.root = x
        elif node == node.parent.left:
            node.parent.left = x
        else:
            node.parent.right = x
        x.left = node
        node.parent = x
        x.is_red = node.is_red
        node.is_red = True
        return x

    def _rotate_right_i(self, node):
        """Perform a `rotation_right` around the node provided. Return the new root of newly rotated local cluster.
        :param node: The node around which to rotate.
        :return: The new root that exists as a result of the rotation.
        """
        x = node.left
        node.left = x.right
        if x.right is not None:
            x.right.parent = node
        x.parent = node.parent
        if node.parent is None:
            self.root = x
        elif node == node.parent.right:
            node.parent.right = x
        else:
            node.parent.left = x
        x.right = node
        node.parent = x
        x.is_red = node.is_red
        node.is_red = True
        return x

########### THE BELOW METHODS ARE FOR STUDENT USE AND CAN BE USED AS IS IN THE ITERATIVE IMPLEMENTATION

    def _flip_colors(self, node):
        """Using the provided `node`, set both child links to black, and set the parent link to `Red`.
        :param node: The node for which the child colors and parent link should have their colors flipped.
        :return: None
        """
        node.is_red = True
        node.left.is_red = False
        node.right.is_red = False

    def _right_is_red(self, node):
        """Indicates whether the link to the right of the provided node is currently Red.
        :param node: The node of which the right link is viewed for redness.
        :return: `True` if `node.right` is red, `False` otherwise.
        """
        if node.right is None:
            return False
        else:
            return node.right.is_red

    def _left_is_red(self, node):
        """Indicates whether the link to the left of the provided node is currently Red.
        :param node: The node of which the left link is viewed for redness.
        :return: `True` if `node.left` is red, `False` otherwise.
        """
        if node.left is None:
            return False
        else:
            return node.left.is_red

    def _left_left_is_red(self, node):
        """Indicates whether there exists to consecutive left red links from the given node.
        :param node: The node from which to interrogate the left and left.left nodes for redness.
        :return: `True` if `node.left` is red and 'node.left.left` is red.  `False` otherwise.
        """
        if node is None:
            return False
        else:
            return self._left_is_red(node) and self._left_is_red(node.left)

    def search(self, key):
        """Search for the desired Key.
        Uses binary search to locate and return the Value at the provided Key.  If the Key is not found, `search` will
        return `None`, otherwise will return the Value stored at the key provided.
        :param key: The unique key by which to retrieve the desired value.  Must be comparable.
        :return: The Value at the Key provided, if the Key is not found, `search` will return `None`
        """
        n = self._node_search(key)
        return n.value if n is not None else None

    def _node_search(self, key):
        """ Searches for the desired key and returns the `RedBlackNode` associated to that key.

        :param key: The unique key by which to retrieve the desired value.  Must be comparable.
        :return: The `RedBlackNode` at the Key provided, if the Key is not found, `_node_search` will return `None`
        """
        curr = self.root

        while True:
            if curr is None:
                return None
            elif curr.key == key:
                return curr
            elif curr.key > key:
                curr = curr.left
            else:
                curr = curr.right

def test_bst(bst):
    bst.insert_i(1, 'one')
    r = bst.search(1)
    result = "PASSED" if r == 'one' else f"FAILED, expected 'one', received {r}"
    print(f"Test Inserting Single Value...{result}")

    tests = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in tests:
        try:
            bst.insert_i(i, i)
            print(f"Insertion of {i} passed (no exception thrown).")
        except Exception as e:
            print(f"Insertion of {i} failed. Exception thrown: {e}")
    for i in tests:
        try:
            r = bst.search(i)
            result = "PASSED" if r == i else f"FAILED, expected {i}, received {r}"
            print(f"Search for {i}: {result}")
        except Exception as e:
            print(f"Search for {i} failed. Exception thrown: {e}")

    bst.insert_i(100, 'one-hundred')
    bst.insert_i(100, 'one hundred')
    r = bst.search(100)
    result = "PASSED" if r == 'one hundred' else f"Failed, expected 'one hundred', received {r}"
    print(f"Test repeat Keys: {result}")


if __name__ == "__main__":
    bst = RedBlackBST()
    test_bst(bst)
