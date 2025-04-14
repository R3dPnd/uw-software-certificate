# class TwoNode:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.left = None
#         self.right = None
        
# class ThreeNode:
#     def __init__(self, key1, value1, key2, value2):
#         self.key1 = key1
#         self.value1 = value1
#         self.key2 = key2

# class FourNode:
#     def __init__(self, key1, value1, key2, value2, key3, value3):
#         self.key1 = key1

# class TwoThreeTree:

class Node:
    def __init__(self, key, value, color):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.color = color
    
class RedBlackTree:
    def __init__(self):
        self.root = None
        self.RED = True
        self.BLACK = False
        
    def is_red(self, node):
        if node is None:
            return False
        return node.color == self.RED
    
    def rotate_left(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = self.RED
        return x
    
    def rotate_right(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = self.RED
        return x
    
    def flip_colors(self, node):
        node.color = self.RED
        node.left.color = self.BLACK
        node.right.color = self.BLACK
        
    def put(self, key, value):
        self.root = self.put_node(self.root, key, value)
        self.root.color = self.BLACK
        
    def put_node(self, node, key, value):
        if node is None:
            return Node(key, value, self.RED)
        
        if key < node.key:
            node.left = self.put_node(node.left, key, value)
        elif key > node.key:
            node.right = self.put_node(node.right, key, value)
        else:
            node.value = value
            
        if self.is_red(node.right) and not self.is_red(node.left):
            node = self.rotate_left(node)
        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self.rotate_right(node)
        if self.is_red(node.left) and self.is_red(node.right):
            self.flip_colors(node)
            
        return node

    def get(self, key):
        node = self.root
        while node is not None:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node.value
        return None

    def inorder(self):
        self.inorder_node(self.root)
        
    def inorder_node(self, node):
        if node is None:
            return
        self.inorder_node(node.left)
        print(node.key, node.value)
        self.inorder_node(node.right)