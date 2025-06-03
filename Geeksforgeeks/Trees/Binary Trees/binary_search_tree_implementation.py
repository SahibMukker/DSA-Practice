'''
creating a binary search tree from scratch for practice
creating insert, delete, find min, preorder dfs, inorder dfs, postorder dfs, isbst check, and max depth
will be doing the dfs searches via recursion, not iteratively in this prac question

Completed in 1 hour 47 mins, delete and is_BST gave me most trouble. i had a lil trouble with max_depth.

i was stuck on delete cause i couldnt figure out how to make the successor the new node until i looked at notes and saw that
i can replace the nodes value with the successors and then delete the successor

was stuck on is_BST cause i was messing up my logic. i was checking if current nodes left is smaller and current nodes right is bigger,
but that isnt the right thing in most cases cause there can be a case where thats true but the left child is smaller than the main root and
that wont be caught, so i needed help of chatgpt to figure out what to do with that

the little trouble i had with max_dpeth is mainly a recursion diff. like i did it and its corerct but i spent some time tryna figure out
why exactly it works. in my mind i was like how tf is it incrementing if theres no counter but realized the '1' in the return reps current height
and when you go down, its 'saved' so for ex. start at root 1 + 0, then next level if theres a node its 1 + 1, etc.
'''

class TreeNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def preorder_dfs(node):
    # if node is none, just return
    if node is None:
        return 
    
    # preorder = processing node first, then moving all the way left, then all the way right
    print(node.data)
    preorder_dfs(node.left)
    preorder_dfs(node.right)
def inorder_dfs(node):
    if node is None:
        return 
    
    # inorder = going all the way left, then processing the node, then all the way right
    inorder_dfs(node.left)
    print(node.data)
    inorder_dfs(node.right)

def postorder_dfs(node):
    if node is None:
        return
    
    # postorder = going all the way left, then all the way right, and then processing node at the end
    postorder_dfs(node.left)
    postorder_dfs(node.right)
    print(node.data)

def insert(root, key):
    # if there is no root, create a new node and return it
    if root is None:
        return TreeNode(key)
    
    # creating the new node, using curr to traverse
    new_node = TreeNode(key)
    curr = root
    
    # this while loop runs and finds the node that will be the parent of the new node taht is being added
    while curr:
        parent = curr
        # move left if node we wanna add is less than current node
        if curr.data > key:
            curr = curr.left
        # move right if node we wanna add is bigger than cureent node
        elif curr.data < key:
            curr = curr.right
        # if the node already exists, return since cant have duplicates in BSTs
        else:
            return
    
    # are now at the node that will be new nodes parent
    # if parents val is bigger than the node to be added, the new node is the parents left child
    # else its the right child    
    if parent.data > key:
        parent.left = new_node
    else:
        parent.right = new_node
        
    return root

# function that finds smallest node, keeps going down left and returns the smallest node
def find_min(node):
    while node.left is not None:
        node = node.left
    return node

def delete(root, key):
    if root is None:
        return root

    # recursively check which subtree the node to be deleted is in    
    if root.data > key:
        root.left = delete(root.left, key)
    
    elif root.data < key:
        root.right = delete(root.right, key)
    # this is when we have found it    
    else:
        # if node to be deleted has only a right child
        if root.left is None:
            return root.right
        # if node to be deleted has only a left child
        elif root.right is None:
            return root.left
        
        # if node to be deleted has both children
        # get successor, setting find min to root.right since the successor has to be the next biggest value
        # then, set the value of the node to be deleted to the value of the successor
        # then deleting the successor (since we cant have duplicates)
        # so this is not the same as deleting the node, its changing the node to be deleted's value and then deleting the successor
        successor = find_min(root.right)
        root.data = successor.data
        root.right = delete(root.right, successor.data)

    return root

def is_BST(root, min_val = float('-inf'), max_val = float('inf')):
    # if theres no root, this is still considered a binary search tree therefore return true
    if root is None:
        return True
    
    # checks if current node biolates the min/max constraint
    # min/max constraint is used so there isnt a case where ex. this is not a valid BST since 6 less than 10 but is in right tree
    #    10
    #   /  \
    #  5   15
    #      /
    #     6
    # so min/max constraint is used, itll check if in left subtree all values are smaller than root, and if in right subtree all values are greater
    if not (min_val < root.data < max_val):
        return False
    
    # will check recursively check if all values in left subtree are smaller than curr root, and if all values in right subtree are greater than curr root
    # if both are true, then this will return true, if one of these is false then it will return false
    return (is_BST(root.left, min_val, root.data)) and is_BST(root.right, max_val, root.data)

def max_depth(root):
    # empty tree retuns 0
    if root is None:
        return 0
    
    # getting biggest value between left and right subtrees
    # adding 1 for 1 based height instead of 0 (forgot actual term)
    return 1 + max(max_depth(root.left), max_depth(root.right))