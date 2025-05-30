'''
Given a Binary Tree and a target key, you need to find the level of the target key in the given Binary Tree.
Note: The level of the root node is 1. If no such key exists then return 0.

Ex 1.
Input: root = [1, 2, 3], target = 4
        1
      /   \
     2     3
Output: 0

Ex. 2
Input: root = [3, 2, 5, 1, 4], target = 4
         3
       /   \
      2     5
    /   \
   1     4
Output: 3

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(h)

Completed in 49 mins 8 secs, need more recursion practice tbh cause in most of these tree problems, thats what stumps me the most i dont understand it fr
'''
class Solution:
    def getLevel(self, root, target):
        '''
        :param root: root of given tree.
        :param target: target to find level
        :return: LEVEL NO
        '''
        
        # using preorder dfs to go through tree
        def find_level(node, target, level):
            # return if there is no node
            if node is None:
                return
            
            # if we find target we are looking for, update result variable
            if node.data == target:
                self.result = level
                return
            
            # recursively going through tree to look for the target
            # increase level by one while iterating down the tree
            find_level(node.left, target, level + 1)
            find_level(node.right, target, level + 1)
        
        # default result is 0 in the event key is not found, default level is 1 (so root of tree is at level 1)
        self.result = 0
        find_level(root, target, 1)
        return self.result