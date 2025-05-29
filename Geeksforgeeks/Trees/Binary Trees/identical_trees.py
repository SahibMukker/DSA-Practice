'''
Given two binary trees with their root nodes r1 and r2, return true if both of them are identical, otherwise, false.

Ex.
Input:
    1          1
   /   \     /   \
  2     3    2    3
Output: true
Explanation: There are two trees both having 3 nodes and 2 edges, both trees are identical having the root as 1, left child of 1 is 2 and right child of 1 is 3.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Completed in 24 mins 50 secs

Was making mistake of initializng empty list in preorder_dfs and not adding the left and right nodes
Also, if node is None, I originally had it to return None but that was wrong cause then tree structure is lost, so instead i used placeholder
'''

'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    
    def preorder_dfs(self, node):
        # if there is no node, have placeholder (so tree structure is kept)
        if node is None:
            return ["#"]
        
        # creating new list with current nodes data and then traversing down its left and right nodes
        result = [node.data]
        result += self.preorder_dfs(node.left)
        result += self.preorder_dfs(node.right)
        
        return result
        
    def isIdentical(self,r1, r2):
        return True if self.preorder_dfs(r1) == self.preorder_dfs(r2) else False