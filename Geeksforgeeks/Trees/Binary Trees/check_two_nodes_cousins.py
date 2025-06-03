'''
Given a binary tree (having distinct node values)root and two node values. Check whether or not the two nodes with values a and b are cousins.
Note: Two nodes of a binary tree are cousins if they have the same depth with different parents.

Ex 1.
Input:
      1
    /   \
   2     3
a = 2, b = 3
Output: false
Explanation: Here, nodes 2 and 3 are at the same level but have same parent nodes.

Ex 2.
Input:
       1
     /   \ 
    2     3
   /       \
  5         4 
a = 5, b = 4
Output: True
Explanation: Here, nodes 5 and 4 are at the same level and have different parent nodes. Hence, they both are cousins. 

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(h)

Completed in 56 mins 40 secs, had implemented dfs to find depth and parent but messed up on parameters of dfs function cause i only had node and depth
found out after thatt needed 4 paramters cause need to track parent since the cousins cant have the same parents, and need target because need to actually
find the nodes (a or b). i also wouldve never thought of using tuples and unpacking them i did not coime up with that myself
'''

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''
class Solution:
# Returns true if the nodes with values 'a' and 'b' are cousins. Else returns false
    def isCousins(self, root, a, b):
        # helper dfs to find depth and parent
        def dfs(node, parent, depth, target):
            if node is None:
                return None
            
            # if current node is the node thats being looked for, return tuple of its depth and the parent
            if node.data == target:
                return (depth, parent)
            
            # going down left subtree, parent is current node and increasing depth by 1
            # if target is found, return
            left = dfs(node.left, node, depth + 1, target)
            if left:
                return left
            # if left not found, then go down right subtree and do the same
            return dfs(node.right, node, depth + 1, target)
            
        # finding depth and parent of a and b
        a_data = dfs(root, None, 0, a)
        b_data = dfs(root, None, 0, b)
        
        # if both nodes are found, set new variables to the data 
        # since a_data and b_data are tuples, the way the code is written 'unpacks' the code
        if a_data and b_data:
            a_depth, a_parent = a_data
            b_depth, b_parent = b_data
            
            # if the depth of a and b is the same and they dont have the same parents, this returns True
            return a_depth == b_depth and a_parent != b_parent
        
        # default returns false in the case a or b doesnt exist
        return False