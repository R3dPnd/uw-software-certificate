class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class MinHeap:
    def __init__(self):
        self.root = Node(None)
        self.size = 0

    """ 
    Return but do not remove the minimum value of the heap. If the heap is empty, return None.
    Must be implemented with no worse than O(1) time complexity. 
    """
    def peek(self):
        if self.root.data is None:
            return None
        return self.root.data

    """ 
    Returns and removes the minimum value from the heap. If the heap is empty, return None.
    Must be implemented with no worse than O(log n) time complexity. 
    """
    def pop(self):
        if self.root.data is None:
            return None
        min_value = self.root.data
        if self.size == 1:
            self.root = Node(None)
        else:
            self.root.data = self._remove_last_node()
            self._bubble_down(self.root)
        self.size -= 1
        return min_value

    """ 
    Insert the provided data onto the heap. Should support integers and strings at least.
    Must be implemented with no worse than O(log n) time complexity. 
    """
    def insert(self, data):
        new_node = Node(data)
        if self.root.data is None:
            self.root = new_node
        else:
            # Get the parent node for the new node based on the size of the heap
            parent = self._get_parent_for_new_node()
            # Place the new node as the left child if the parent has no left child, otherwise place it as the right child
            if parent.left is None:
                parent.left = new_node
            else:
                parent.right = new_node
            new_node.parent = parent
            # Bubble up the new node
            self._bubble_up(new_node)
        self.size += 1

    """ 
    Removes all elements from the heap. Must be implemented in no worse than O(1) time. 
    """
    def clear(self):
        self.root = Node(None)
        self.size = 0

    def _bubble_up(self, node):
        # Move up from the node while the parent exists and the node is smaller than the parent
        # This means the node moves up to the level where it is smaller than the parent, up to the root
        while node.parent and node.data < node.parent.data:
            node.data, node.parent.data = node.parent.data, node.data
            node = node.parent

    def _bubble_down(self, node):
        # Move down from the node while the left child exists
        # If it does not, we are at a leaf node and we stop
        while node.left:
            # Find the smallest child of the node, and swap the node if it is larger than the smallest child
            smallest = node.left
            if node.right and node.right.data < node.left.data:
                smallest = node.right
            if node.data <= smallest.data:
                break
            # Swap the node with the smallest child
            # This means the node moves down to the level where it is smaller than both children
            node.data, smallest.data = smallest.data, node.data
            node = smallest

    def _remove_last_node(self):
        # Remove the last 0 or 1 from the binary representation of the size
        path = bin(self.size)[3:]
        current = self.root
        # Navigate to the last parent node
        for direction in path[:-1]:
            if direction == '0':
                current = current.left
            else:
                current = current.right
        # Remove the last node by setting the left or right child of the last parent node
        data = None
        if path[-1] == '0':
            data = current.left.data
            current.left = None
        else:
            data = current.right.data
            current.right = None
        return data

    def _get_parent_for_new_node(self):
        # Add 1 to the size and get the binary representation
        path = bin(self.size + 1)[3:]
        current = self.root
        for direction in path[:-1]:
            if direction == '0':
                current = current.left
            else:
                current = current.right
        return current