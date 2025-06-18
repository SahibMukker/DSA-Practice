'''
Given a binary tree, return true if it is height-balanced and false otherwise.

A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Ex 1.
Input: root = [1,2,3,null,null,4]
      1
     / \
    2   3
      /
     4
Output: true

Ex. 2
Input: root = [1,2,3,null,null,4,null,5]
      1
     / \
    2   3
      /
     4
    /
   5
Output: false

Completed in 35 mins 6 secs, needed to look at solution
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # dfs recursive, will return boolean and height of tree
        def dfs(root):
            if not root:
                return [True, 0]
            
            # checking if left and right subtrees are balanced
            left, right = dfs(root.left), dfs(root.right)

            # check if balanced from root, doing [1] since the first is boolean, second is height
            # and checks if left and right subtrees are balanced and if root is balanced
            # so this is also a boolean (if all conditions are true then balance = True else False)
            balance = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            
            return [balance, 1 + max(left[1], right[1])]
        
        # returning the first value (the boolean true/false)
        return dfs(root)[0]
        