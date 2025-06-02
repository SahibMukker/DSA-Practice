'''
Completed AVL tree insertion in 1 hour 9 mins, can do this on paper but couldnt figure out the code
and how to balance properly in code, so looked at solution in comments + help from chatgpt to understand
'''

''' structure of tree node:

class Node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
        self.height=1

'''

class Solution:
    def insertToAVL(self, node, key):
        if not node:
            return Node(key)
    
        # insert (like a normal BST)
        if key < node.data:
            node.left = self.insertToAVL(node.left, key)
        else:
            node.right = self.insertToAVL(node.right, key)
        
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        
        diff = self.height(node.left) - self.height(node.right)
        
        # imbalnce case 1 (right right)
        if diff < -1 and key > node.right.data:
            return self.leftrotate(node)
        
        # imbalance case 2 (left left)
        if diff > 1 and key < node.left.data:
            return self.rightrotate(node)
            
        # imbalance case 3 (right left)
        if diff < -1 and key < node.right.data:
            node.right = self.rightrotate(node.right)
            return self.leftrotate(node)
        
        # imbalance case 4 (left right)
        if diff > 1 and key > node.left.data:
            node.left = self.leftrotate(node.left)
            return self.rightrotate(node)
        
        return node
        
    def height(self, node):
        # if a node exists return its height, else the function default returns 0
        if node:
            return node.height
        
        return 0
    
    # for when right subtree is heavier (right right/right left rotation)
    def leftrotate(self, root):
        # new root is going to be right child, and are saving left subtree in temp
        new_root = root.right
        temp = new_root.left
        
        # old root now becomes left child, then reconnect the left subtree
        new_root.left = root
        root.right = temp
        
        # updating height after rotation
        # looks at height of left and right subtrees and chooses the bigger number
        # and then add 1 since the root itself is not counted
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        new_root.height = 1 + max(self.height(new_root.left), self.height(new_root.right))
        
        return new_root
    
    # when lefft subtree is heavier (left left/left right rotation)
    def rightrotate(self, root):
        # new root going to be left child, save right subtree in temp
        new_root = root.left
        temp = new_root.right
        
        # old root is now left right subchild, reconnect right subtree
        new_root.right = root
        root.left = temp
        
        # updating heights after rotation
        # looks at height of left and right subtrees and chooses the bigger number
        # and then add 1 since the root itself is not counted
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        new_root.height = 1 + max(self.height(new_root.left), self.height(new_root.right))
        
        return new_root