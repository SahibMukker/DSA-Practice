'''
The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree. 
The path does not necessarily have to pass through the root.
The length of a path between two nodes in a binary tree is the number of edges between the nodes.
Given the root of a binary tree root, return the diameter of the tree.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(h)

Completed in 27 mins 36 secs
didnt know how to make diameter a global variable and my logic was also kinda off, i knew dfs was needed. i thought i should count the distance
between each node but that was wrong and i also wasnt even able to figure it out so looked at solution
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diameter = 0
        
        def dfs(curr):
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            # need to set it nonlocal so that it can be used and called upon by this function
            # otherwise wihtout it you get error
            # another way to do this is in initial creation of diameter, make it self.diameter = 0
            # and therefore no need for nonlocal
            nonlocal diameter
            
            # updating the diameter but not returning it since need to go through all the nodes
            # current diameter is length of left and right subtrees added so this is
            # updating diameter to be the biggest value between old diameter and current diameter
            diameter = max(diameter, left + right)
            
            return 1 + max(left, right)

        dfs(root)

        return diameter 
