class Graph:
    """ A Python Implementation of a Basic Directed Graph.
    """
    class Vertex:
        """A basic Vertex or graph node that can store a color, and has an adjacency list.
        """
        def __init__(self, key, color=None):
            """Returns a newly created `Vertex` object.
            :param key: The unique value by which to retrieve the desired value.
            :param color: The optional color of the vertex.
            """
            self.key = key
            self.color = color
            self.adj = []

        def edge_list(self):
            """Prints basic list of edges."""
            pass

        def get_edges(self):
            """ Returns a list of out edges from the existing vertex."""
            pass

        def out_degree(self):
            """Returns the Out Degree of the Vertex"""
            pass

        def add_edge(self, edge):
            pass

        def __str__(self):
            """Returns a string representation of a node, including the ids and colors of its left and right links.
            The pattern used is: `(left.key)<-[Red|Black]--(node.key)--[Red|Black]->(right.key)
            If either left or right nodes are blank, the key is `None` and the link color defaults to `Black`.

            :return: String representation of the desired node.
            """
            pass

    class Edge:
        """Simple Edge class that stores a source and target and a weight."""

        def __init__(self, source, target, weight=None):
            self.source = source
            self.target = target
            self.weight = weight

        def __str__(self):
            weight_str = "" if self.weight is None else f"[{self.weight}]"
            return f"{self.source}-{weight_str}->{self.target}"

    def __init__(self):
        """Creates an empty graph with no Vertices and no Edges."""
        self.V = 0
        self.E = 0
        self.vertices = {}

    def __str__(self):
        """Prints basic information about the graph."""
        return f"Vertices:{self.V}, Edges:{self.E}, Degree:{self.degree()}"

    def degree(self):
        """Returns the total degree from all nodes in graph G"""
        pass

    def add_vertex(self, key, color=None):
        """ Adds new vertex of optional color to the Graph. Throws a Key error if he vertex key is already used."""
        pass

    def add_edge(self, source, target, weight=None, bi=False):
        """ Add a new edge to the Graph.  If ether the source or target vertex is not yet in the Graph it will be
        automatically added without a color.
        :param source: The key of the vertex to be used as the "from" vertex.
        :param target: The key of the vertex to be used as the "to" vertex.
        :param weight: The optional weight of the edge.
        :param bi: Boolean indicating whether or not to create a bi-directional edge.  This is implemented as creating
        a second edge to the graph from the target to the source.
        :return: None
        """

        pass

    def depth_first_search(self, start):
        pass



    def is_acyclic(self):
        """Performs a complete search of the graph, halting when a cycle is found or when all vertices in
         the graph have been traversed.
         :returns: True if no cycle is detected, false otherwise. An empty graph will return True"""
        pass



if __name__ == "__main__":
    g = Graph()
    g.add_edge('a','b')
    g.add_edge('a','c')
    g.add_edge('b','d')
    g.add_edge('b','c')
    g.add_edge('d','c')
    g.add_edge('c','b')
    g.add_edge('b','a')

    for v in g.depth_first_search('a'):
        print(v)

    cycle = Graph()
    cycle.add_edge('a','b')
    cycle.add_edge('a','c')
    cycle.add_edge('c','d')
    cycle.add_edge('e','f')
    cycle.add_edge('f','g')

    print("Should be acyclic")
    print(cycle.is_acyclic())

    cycle.add_edge('g','e')
    print("Should no longer be acyclic")
    print(cycle.is_acyclic())

    g2 = Graph()

    g2.add_edge('a', 'b')
    g2.add_edge('b', 'c')
    g2.add_edge('c', 'd')
    g2.add_edge('b', 'd')
    g2.add_edge('d', 'e')
    g2.add_edge('e', 'g')

    g2.is_acyclic()

    g3 = Graph()
    g3.add_edge('a','a')
    print(f"Self loop graph is_acyclic?:{g3.is_acyclic()}")

    # SAME GRAPH AS SLIDES FOR CYCLE DETECTION
    g4 = Graph()
    baked_order = ['d','c','b','a','e','f']
    for v in baked_order:
        g4.add_vertex(v)

    g4.add_edge('a','b')
    g4.add_edge('b', 'c')
    g4.add_edge('b', 'd')
    g4.add_edge('b', 'e')
    g4.add_edge('c', 'd')
    g4.add_edge('d', 'e')
    g4.add_edge('e', 'f')


    print(f"Is there a cycle, there shouldn't be, this should be True... and it is {g4.is_acyclic()}")

    g4.add_edge('c', 'a')

    print(f" Is there a cycle, there is now... so this should be False...? {g4.is_acyclic()}")

