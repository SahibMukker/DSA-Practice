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

RUN 2 ITERATIVE DFS IMPLEMENTATION:
completed in 32 mins 54 secs, was orignally making 2 stacks and making copies of trees but when i tried running it and saw it wasnt working
i realized that i dont need to make copies i needa just iterate through both and compare as i go. but i didnt know i could/should add both
trees to 1 stack as a tuple, once i saw that, the rest of the code i fixed myself
'''
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
    
# RUN 2 ITERATIVE DFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # since comparing two trees, adding both of them to the stack as a tuple
        stack = [(p, q)]
        
        while stack:
            # unpacking current node tuple
            node1, node2 = stack.pop()

            # if in both trees current node is null, keep going
            if not node1 and not node2:
                continue
            
            # if one of the nodes is null and the other is not or if both exist but values dont match up,
            # not same tree so return false
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            # if those checks are passed, add the next set of nodes to stack to check them
            # adding to stack as a tuple since stack is initialized as tuple
            stack.append((node1.left, node2.left))
            stack.append((node1.right, node2.right))
        
        # default return true since all false checks have been passed
        return True