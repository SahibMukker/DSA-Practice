'''
Given a binary tree, you have to return the size of it. Size of binary tree is defined as number of nodes in it.
Ex.
Input:      
       1
     /  \
    2    3
Output: 3
Explanation: There are three nodes in given binary tree.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Completed in 21 mins 17 secs
'''
class Solution:
    def getSize(self, node : Optional['Node']) -> int:
        
        # if there is no node in the tree return 0
        if not node:
            return 0
        
        # set counter to 0 and increment by 1 for every node visited
        # return counter + 1
        counter = 0
        counter += self.getSize(node.left)
        counter += self.getSize(node.right)
        
        # have to add one to account for the node we are on
        return counter + 1