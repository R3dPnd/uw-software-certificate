'''
    BST can obviously store items more complex than primitives. The values are likely to be objects with indices related to their keys.
    For example, a person object can be stored in a BST with the key being the person's ID.
'''
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)
        
    def delete(self, key):
        self.root = self._delete(self.root, key)
    
    def change_key(self, old_key, new_key):
        """ Changes the key of a node in the BST.

        :param old_key: The old key to change.
        :param new_key: The new key to change to.
        """
        # Find the node with the old key
        node = self.node_search(old_key)
        if node is None:
            raise ValueError(f"Key {old_key} not found in the BST.")
        # Remove the node with the old key
        self.delete(old_key)
        # Insert the node with the new key
        self.insert(new_key, node.value)

class TwoThreeTree:
    