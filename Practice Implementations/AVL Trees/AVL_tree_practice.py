'''
creating avl tree from scratch, implementing left rotation, right rotation, and insertion

Completed in 1 hour 52 misn

still needed to use my notes but i think i understand the logic behind implementing rotations in code better but,
i need to remember to check key value as well otherwise after rotations and stuff values will be at the wrong spot

ex. i bricked this in practice cause i forgot to account for this
insert 4 in following:

		     13 
       		/  \
	      10    15 
         /  \    \ 
        5   11   16 
       /
      2
      
i did this for insert 4 which is wrong since right values need to be bigger not smaller:
		     13 
       		/  \
	      10    15 
         /  \    \ 
        5   11   16 
       / \
      2	  4   
      
i was forgetting to account for this when implementing insertion in code as well so i needa remember to do this when implementing insertion in code as well
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

# function that will find the height of whatever node looking for
def height(node):
    if node is None:
        return 0
    
    return node.height

# runction that gets balance factor of a specific node by going down both leftt and right subtrees and subtracting the heights
def balance_factor(node):
    if node is None:
        return 0
    
    return height(node.left) - height(node.right)

def leftrotate(node):
    # new_root will be the new root after the rotation happens
    # new_left_subtree is going to be the subtree that gets moved (has not been moved yet)
    new_root = node.right
    new_left_subtree = new_root.left
    
    # move the unbalanced node to the left of the new root and add the subtree to the right of the unbalanced node
    new_root.left = node
    node.right = new_left_subtree
    
    # updating heights of the new and old nodes by getting max value of left and right subtrees of each
    node.height = 1 + max(height(node.left), height(node.right))
    new_root.height = 1 + max(height(new_root.left), height(new_root.right))
    
    return new_root

def rightrotate(node):
    
    # new root will be the new root after the right rotation occurs
    # new_right_subtree will be the subtree that is moved to the rightt of the new node
    new_root = node.left
    new_right_subtree = new_root.right
    
    # the new roots right node is going to be the old node 
    # and the right subtree that needs to be moved is now moved to the left of the old node
    new_root.right = node
    node.left = new_right_subtree
    
    # updating heights and returning the new root after the rotations
    node.height = 1 + max(height(node.left), height(node.right))
    new_root.height = 1 + max(height(new_root.left), height(new_root.right))
    
    return new_root

def insert(node, key):
    if node is None:
        return Node(key)
    
    # go right if key is bigger than current node
    if node.data < key:
        node.right = insert(node, key)   
    # go left if key is smaller than current node
    elif node.data > key:
        node.left = insert(node, key)   
    # if node exists, return since cant have duplicates
    else:
        return node
    
    # update height of the node
    node.height = 1 + max(height(node.left), height(node.right))
    
    # balance factor checks
    bf = balance_factor(node)
    
    # if bf is greater than 1 and the key that is being inserted is smaller than the left nodes value, LL imbalance need right rotation
    if bf > 1 and key < node.left.data:
        return rightrotate(node)
    
    # if bf less than -1 and current value being added is bigger than the right nodes value, RR imbalance need left rotation
    if bf < -1 and key > node.right.data:
        return leftrotate(node)
        
    # if need LR rotation
    if bf > 1 and key > node.left.data:
        node.left = leftrotate(node)
        return rightrotate(node)
    
    # if need RL rotation
    if bf < -1 and key < node.right.data:
        node.right = rightrotate(node)
        return leftrotate(node)