'''
Write a recursive function count_leaves(node) that returns the number of leaf nodes in a binary tree. A leaf node is a node that has no left or right children.

Ex.
     1
    / \
   2   3
  / \
 4   5
The leaf nodes are: 3, 4, and 5
So count_leaves(root) should return 3

Completed in 7 mins 26 secs
'''

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def count_leaves(node):
    # if there is no node return 0
    if node is None:
        return 0
    
    # if there is no left or right node, return 1 since we have found a leaf node
    if node.left is None and node.right is None:
        return 1
    
    # if there is a left or right node, recursively call the function and add the leaf nodes together
    return count_leaves(node.left) + count_leaves(node.right)