'''
Completed in 51 mins 52 secs, used same code for rotations from my insertion implementaiton, but in deleteNode
i was messing up the logic in the actual rotations. i should prob start writing down the logic before coding cause
towards last week i did that and it helped but today i havent and its been hella hard logicing everythig out
'''

''' structure of tree node:

class Node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
        self.height=1

'''

def deleteNode(root, key):
    # base case, if no root then return
    if not root:
        return root
    
    # if current key is less than the root value go left and recursion till node to be deleted is found
    if key < root.data:
        root.left = deleteNode(root.left, key)
    # if current key is greater than root vlaue go right and recursion till node to be deleted is found
    elif key > root.data:
        root.right = deleteNode(root.right, key)
    # if node to be deleted is found,
    else:
        # node with 1 or no child, if theres 1 child this will return that child (replaces deleted node with child)
        # if no child, replaces node with None
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        
        # if node has 2 children, find smallest node (the correct successor) and replace current nodes value with that
        # then go down recursively and delete the successor from the bottom so theres no duplicates
        temp = min_node(root.right)
        root.data = temp.data
        root.right = deleteNode(root.right, temp.data)
    
    # updating height
    root.height = 1 + max(height(root.left), height(root.right))
    
    # chekcing balance facotr
    balance = balance_factor(root)
    
    # left left
    if balance > 1 and balance_factor(root.left) >= 0:
        return rightrotate(root)
    # left right
    if balance > 1 and balance_factor(root.left) < 0:
        root.left = leftrotate(root.left)
        return rightrotate(root)
    # right right
    if balance < -1 and balance_factor(root.right) <= 0:
        return leftrotate(root)
    # right left
    if balance < -1 and balance_factor(root.right) > 0:
        root.right = rightrotate(root.right)
        return leftrotate(root)
    
    return root

# function to determine balancer factor for rebalancing tree if/when needed
# you get balance factor by subtracting height of node ur at by the height of left and right subtrees
def balance_factor(root):
    if not root:
        return 0
    return height(root.left) - height(root.right)

# function to find appropriate sucessor, will go as far left as possible (since left side = smaller values)
# and find the node that will replace the node that is going to be deleted
def min_node(node):
    # code similar to going down a linked list
    curr = node
    
    while curr.left:
        curr = curr.left
    return curr
    
# function to get height of node
def height(node):
    if node:
        return node.height
    return 0
    
# for when right subtree is heavier (right right/right left rotation)
def leftrotate(root):
    # new root is going to be right child, and are saving left subtree in temp
    new_root = root.right
    temp = new_root.left
        
    # old root now becomes left child, then reconnect the left subtree
    new_root.left = root
    root.right = temp
        
    # updating height after rotation
    # looks at height of left and right subtrees and chooses the bigger number
    # and then add 1 since the root itself is not counted
    root.height = 1 + max(height(root.left), height(root.right))
    new_root.height = 1 + max(height(new_root.left), height(new_root.right))
        
    return new_root
    
# when lefft subtree is heavier (left left/left right rotation)
def rightrotate(root):
    # new root going to be left child, save right subtree in temp
    new_root = root.left
    temp = new_root.right
        
    # old root is now left right subchild, reconnect right subtree
    new_root.right = root
    root.left = temp
        
    # updating heights after rotation
    # looks at height of left and right subtrees and chooses the bigger number
    # and then add 1 since the root itself is not counted
    root.height = 1 + max(height(root.left), height(root.right))
    new_root.height = 1 + max(height(new_root.left), height(new_root.right))
        
    return new_root  