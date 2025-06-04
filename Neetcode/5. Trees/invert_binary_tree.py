'''
You are given the root of a binary tree root. Invert the binary tree and return its root.

Example 1:
Input: root = [1,2,3,4,5,6,7]

         1
       /   \
      2     3
     / \   / \
    4   5 6   7

Output: [1,3,2,7,6,5,4]

         1
       /   \
      3     2
     / \   / \  
    7   6 5   4
    
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Completed in 25 mins 46 secs

tried to do (what i know know is) iterative implementation cause that was making sense to me but i couldnt figure it out
then i saw that there is a recusrive way to do it and remembered that 'oh shit i can do recursion if i need to iterate through tree for anything'
and so this is a preorder dfs (i think) recursive solution
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # base case, if no root return None
        if root is None:
            return None

        # swap the two values
        root.left, root.right = root.right, root.left

        # recursively swap the roots and return the root
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root