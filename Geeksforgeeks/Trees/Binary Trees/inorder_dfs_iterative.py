'''
Given a binary tree. Find the inorder traversal of the tree without using recursion.

Ex 1.
Input:  
       1
     /   \
    2     3
   /  \    
  4    5  
 
Output: 4 2 5 1 3
Explanation:
Inorder traversal (Left->Root->Right) of 
the tree is 4 2 5 1 3.

Ex 2.
Input:

        1
     /      \
    1         5
    \        / \
     7      10  6
      \     /
       10  6
Output: 1 7 10 8 6 10 5 6
Explanation:
Inorder traversal (Left->Root->Right) 
of the tree is 1 7 10 8 6 10 5 6.

Completed in 57 mins 42 secs

- Forgot to account for going back up and keeping the loop running till both curr and stack are empty and not just curr.
- Also my original implementation was wrong since it was only going left or right if they .left or .right are none, but this asks for in order
 (so all the way left, then node, and then right) and it was missing backtracking to the parent.
- Also I was using stack to store data values and not nodes and cause of that traversal wasnt happening properly
'''
#User function Template for python3

'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

# Return a list containing the inorder traversal of the given tree
class Solution:
    def inOrder(self, root):
        # using a stack to keep track of the nodes to be added in correct order,
        # and a list that is the going to contain the final order
        stack = []
        result = []
        curr = root

        # curr checks going down the left side of the tree, stack checks going back up
        # so running loop while the algo can go down and back up (so while either curr or stack is not empty)
        while curr or stack:
            # keeping going down to the left till there is no more left and adding nodes to the stack on the way
            if curr:
                stack.append(curr)
                curr = curr.left
            
            # if not curr, then pop from the stack (bringing the code back to the previous, the parent node) 
            # and append that data point to the result stack
            # then go to the right child of the parent whose left was just popped
            else:
                curr = stack.pop()
                result.append(curr.data)
                curr = curr.right
            
        return result


