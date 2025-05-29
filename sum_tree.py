'''
Given a Binary Tree. Check for the Sum Tree for every node except the leaf node. Return true if it is a Sum Tree otherwise, return false.
    A SumTree is a Binary Tree where the value of a node is equal to the sum of the nodes present in its left subtree and right subtree.
    An empty tree is also a Sum Tree as the sum of an empty tree can be considered to be 0. A leaf node is also considered a Sum Tree.

Ex.
Input:
    3
  /   \    
 1     2
Output: true
Explanation: The sum of left subtree and right subtree is 1 + 2 = 3, which is the value of the root node. Therefore,the given binary tree is a sum tree.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(log n)

Completed in 55 mins 54 secs
'''

class Solution:
    def is_sum_tree(self, node):
        # function that does postorder dfs to check if the subtree of a certain node is a sum tree
        # and returns the total sum of nodes in that sub tree (so can check the parent)
        # doing post order cause need to know left and right sub trees before verifying current node
        # the function returns boolean (true or false) and total sum value
        def check_sum(node):
            if node is None:
                return True, 0
            
            # checking if the current node is a leaf node, if it is, its a valid sum tree
            if node.left is None and node.right is None:
                return True, node.data
            
            # recursively check left and right subtrees
            # the 'is sum' variables are boolean, the '_sum' variables hold the actual numbers
            left_is_sum, left_sum = check_sum(node.left)
            right_is_sum, right_sum = check_sum(node.right)
            
            # current_is_sum checks if current node value equals sum of left and right subtree sums 
                # (will be either true or false)
            # total_sum stores the total sum so can check later
            current_is_sum = node.data == left_sum + right_sum
            total_sum = node.data + left_sum + right_sum
            
            # return whether current subtree is a sum tree and the sum
            # so it checks if left_is_sum, right_is_sum, and current_is_sum are all true.
            # if they are, then the line of code returns true and the sum
            # if any of those 3 are false, then it returns false
            return left_is_sum and right_is_sum and current_is_sum, total_sum
        
        # doing [0] cause this question only asks for true and false and [0] is the boolean, [1] is the total sum
        return check_sum(node)[0]