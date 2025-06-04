'''
Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.
Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

Ex 1.
Input: p = [1,2,3], q = [1,2,3]
Output: true

Ex 2.
Input: p = [4,7], q = [4,null,7]
Output: false

Completed in 30 mins 27 secs, forgot to account for the case where one of the trees is empty,
original implementation i did not properly account for missing tree values, i corrected that implementation as well
and added it
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if both trees are empty, return true since empty trees are the same
        if not p and not q:
            return True
        
        # if one of the trees are empty, return false since they are not the same
        if not p or not q:
            return False

        # if the vals do not match return false
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
# orignal implementation that was corrected
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # preorder dfs
        def dfs(root):
            # if theres no root then add a placeholder to keep tree structure
            if root is None:
                return ['#']

            # return the current roots value and add on the left and right subtree values
            return [root.val] + dfs(root.left) + dfs(root.right)
        
        # returns true if the two dfs results match
        return dfs(p) == dfs(q)