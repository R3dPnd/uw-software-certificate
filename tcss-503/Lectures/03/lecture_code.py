class Node:
    def __init__(self, key, value, is_red=True):
        self.key = key
        self.value = value
        
class Edge:
    def __init__(self, source, target, weight=None):
        self.source = source
        self.target = target
        self.weight = weight
        
class ListGraph:
    def __init__(self):
        self._nodes = []
        self._edges = []
        self.vertices = {}