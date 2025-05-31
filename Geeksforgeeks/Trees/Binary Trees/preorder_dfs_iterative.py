'''
Given a Binary tree. Find the preorder traversal of the tree without using recursion.

Ex 1.

Input:
           1
         /   \
        2     3
      /  \
     4    5
Output: 1 2 4 5 3
Explanation:
Preorder traversal (Root->Left->Right) of 
the tree is 1 2 4 5 3.


Completed in 22 mins 50 secs
'''

'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    # Return a list containing the preorder traversal of the given tree
    def preOrder(self, root):
        
        # if no root, return an empty list
        if not root:
            return []
        
        # stack that stores all the nodes we need to process, starts off at the root node
        # result which is gonna be list of final ordered nodes
        stack = [root]
        result = []
        
        while stack:
            # add current node to the result list first
            node = stack.pop()
            result.append(node.data)
            
            # gotta go right first so that it is added into the stack before the left nodes
            # this is so that the left nodes get popped and added to the result first 
            # (since stacks are LIFO and we want preorder, so root -> left -> right)
            if node.right:
                stack.append(node.right)
                
            if node.left:
                stack.append(node.left)
                
                
        return result