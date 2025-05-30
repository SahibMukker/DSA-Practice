'''
Given a Binary Tree, check whether the given Binary Tree is Complete Binary Tree or not. 
A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, 
and all nodes should be as much close to left as possible.

Ex 1.
Input: root = [1, 2, 3]
Output: true
Explanation: The given tree is complete binary tree.

Ex 2.
Input: root = [1, 2, 3, 4, N, 5, 6]
Output: false
Explanation: The given tree is not complete binary tree because in last level all nodes are not at left.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Completed in 31 mins mins 43 secs, haven't done much BFS so didnt know that was needed, tried doing dfs but i got stir fried
'''

from collections import deque

class Solution():
    def isCompleteBT(self, root):
        
        # if root is empty, that means no tree but no tree is still considered a complete binary tree
        if not root:
            return True
        
        # initializing queue for BFS (level order traversal)
        # and initializing a boolean that will indicate if a node has a missing child
        queue = deque([root])
        no_child = False
        
        while queue:
            node = queue.popleft()
            
            # if the node doesnt have a child then update boolean
            if node is None:
                no_child = True
                
            # if a child is found, update no_child boolean to false since a child has been found
            # and then add next set of children to the queue
            else:
                if no_child:
                    return False
                
                queue.append(node.left)
                queue.append(node.right)
        
        return True