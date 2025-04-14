# Summary of the Lecture

The lecture discusses the implementation of a binary tree using an array-based representation. Key points include:

## Child and Parent Index Calculation

Left Child: For a node at index i, the left child is at 2 *i + 1.
Right Child: For a node at index i, the right child is at 2* i + 2.
Parent: For a node at index i, the parent is at (i - 1) // 2 if i is odd, and (i - 2) // 2 if i is even.

## Properties of Nodes

The right child index is always even.
The tree alternates between odd and even indices for children.

## Helper Functions

Functions to get the index of the left child, right child, and parent are used to navigate the tree.

## Memory Allocation

Arrays require contiguous memory allocation.
The initial tree size is set to 64 nodes.
When the tree outgrows its size, the array is expanded by copying existing data to a new array with double the size, filled with None values.

## Efficiency

Doubling the array size minimizes the overhead of frequent resizing.
This approach ensures logarithmic execution time for insertions as the tree grows.
The lecture emphasizes the importance of efficient memory management and index calculations in implementing a binary tree using an array.
