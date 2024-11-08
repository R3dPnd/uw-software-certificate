# Lecture 5

Zoom Link: <https://washington.zoom.us/rec/play/rz78P0tutO6dorRWSe0PreCGasOMHOYMgZg3_qFDvH3GB5V2Bdq97nx1sgcC72owB8o1Jl4wgFusDO6j.vLfYe3EjA30wNTzN>

## Summary

    Graphs: Graphs are a data structure implemented from a Linked-List that consists of Nodes and Edges between nodes. These edges can be directional or undirected. The typical traversal algorithms are Breadth First Search and Depth First search.

    Depth First Search: Traversing a graph from left to right and processing the nodes using a Stack. 

    Breadth First Search: Traversing a graph from left to right and processing the nodes using a Queue. 

    Trees: Trees are a data structure similar to graphs but are always unidirectional with a specified root node. One such implementation would be a binary tree and further a binary search tree in which all nodes have at most  children nodes. These are typically used for creating a sorted data structure with log(n) search times, though this gets complicated when keeping a tree balanced.

    Tree Traversal: Trees can be traversed in three main ways. Pre-order in which you traverse left until you can't move left further, taking each node as you traverse. Post-order where do the same but only take the nodes when they have no children. In order where you move left most, then take that parent and move to the right node. I n a balanced tree this will give you the items in order.

    Tree Node Deletion: Deleting a tree node is trivial when the node hs no children or only one child, but when they have two children, you must replace this node with the node most left from they right node.
