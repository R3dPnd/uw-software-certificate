class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    """ 
        Returns and removes the minimum value from the heap. If the heap is empty, return None.
        Must be implemented with no worse than O(log n) time complexity. 
    """
    def pop():
        pass
    
    """ 
        Return but do not remove the minimum value of the heap. If the heap is empty, return None.
        Must be implemented with no worse than O(1) time complexity. 
    """
    def peek():
        pass
    
    """ 
        Insert the provided data onto the heap. Should support integers and strings at least.
        Must be implemented with no worse than O(log n) time complexity. 
    """
    def insert():
        pass

    """ 
        Removes all elements from the heap. Must be implemented in no worse than O(1) time. 
    """
    def clear():
        pass
    
    def print_heap(self):
        print(self.heap)