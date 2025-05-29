'''
Given a root of a Binary Tree. Your task is to check whether it is Symmetric or not, i.e. whether the binary tree is a Mirror image of itself.

Ex 1.
Input: root[] = [1, 2, 2, 3, 4, 4, 3]
        1
       / \
      2   2
     / \ / \
    3  4 4  3
Output: True
Explanation: Tree is mirror image of itself i.e. tree is symmetric.

Input: root[] = [1, 2, 2, N, 3, N, 3]
        1
       / \
      2   2
       \   \
        3   3
Output: False
Explanation: Tree is not mirror image of itself i.e. tree is not symmetric.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(h)

Completed in 30 mins 19 secs, couldnt figure out how to iterate down and check left node of one node with right node of other
'''

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def mirror_check(self, root1, root2):
        # if the children of the parent node are empty, there is symmetry
        if root1 == None and root2 == None:
            return True
        
        # if one of the children are empty or if the values dont match, there is no symmetry
        if root1 == None or root2 == None or root1.data != root2.data:
            return False
        
        # recursively check if left child of one node matches right of other 
        # and if both recursive calls are the same then True will be returned, else false
        return self.mirror_check(root1.left, root2.right) and self.mirror_check(root1.right, root2.left)
    
    def isSymmetric(self, root):
        # if there is no root then there is still symmetry
        if root == None:
            return True
        
        return self.mirror_check(root.left, root.right)