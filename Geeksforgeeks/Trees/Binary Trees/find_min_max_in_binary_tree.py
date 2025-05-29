'''
Given a Binary Tree, find maximum and minimum elements in it.

Ex.
Input:   6
        / \
       5   8
      /
     2  
Output: 8 2
Explanation: The maximum and minimum element in this binary tree is 8 and 2 respectively.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Completed in 21 mins 48 secs
'''

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''

class Solution:
    # bfs implementaiton that adds every node to a list called result
    def bfs(self, root):
        
        if root is None:
            return
        queue = [root]
        result = []
        
        while queue:
            node = queue.pop()
            result.append(node.data)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result
        
    def findMax(self,root):
        
        # go through the tree and return the max value
        maximum = self.bfs(root)
        return max(maximum)
        
    def findMin(self,root):
        
        # go through the tree and return the min value
        minimum = self.bfs(root)
        return min(minimum)