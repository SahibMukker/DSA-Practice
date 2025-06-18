'''
Given the root of a binary tree, return its depth.
The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Completed in 25 mins 3 secs
did BFS implementation, had everything right except i wasnt accounting for processing all nodes of current level with the for loop,
instead i was processing one node at a time and increasing depth per node which is obvi wrong
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        q = deque()
        q.append(root)
        
        depth = 0

        while q:
            # need for loop to make sure all nodes of current level are processed
            # without it, depth is increased per node processed (which is wrong)
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            depth += 1
            
        return depth