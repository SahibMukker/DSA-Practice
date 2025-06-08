'''
implementing graph (adjacency matrix, adjacency list, node class, recursive DFS, iterative DFS, and BFS) for practice, the graph i am using is the following:

        0 -> 1 -> 2
         \       ^ ^
          V     /   \
          3 -> 4 -> 5
         /  \
        V    V
        7    6
        
got array and n from Gregg Hog Graphs vid on youtube and code for implementing from him as well
trying my best to implement from memory/understanding/logicing it out

Completed in 1 hour 56 mins
was able to do most of it but when doing iterative DFS and BFS, i forgot to actually go through the adjacency list and its neighbours
and was instead just adding the current node to seen and not doing anything after that, had to look at notes for iterative DFS and then BFS is basically the same
but with queues instead of stacks so for that i did it right
'''
from collections import defaultdict, deque
# array for adjacency list/matrix
n = 8
A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]

# ADJACENCY MATRIX:
M = []

# setting size of matrix, this will make sure that there are the correct numbers of rows and columns (of size n x n)
for i in range(n):
    M.append([0]*n)

# going through the array and where there are connections, print them out
for u, v in A:
    M[u][v] = 1

print(f'Adjacency Matrix: \n{M}')

# ADJACENCY LIST:
adj_list = defaultdict(list)

for u, v in A:
    adj_list[u].append(v)

print(f'\nAdjacency List: \n{adj_list}')

# making class for node for practice
class Node:
    def __init__(self, data):
        self.data = data
        # setting self.neighbours to default empty list
        self.neighbours = []
    
    # simple function that displays neighbours of a certain node
    # first you find the connections by going through the node, finding its neighbours and setting connections to be that nodes data
    # then returning a string that shows the connections (neighbours) of the node in question
    def display(self):
        connections = [node.data for node in self.neighbours]
        return f'{self.data} is connected to: {connections}'

# recursive DFS
def recursive_dfs(node):
    # this line is processing the node, in other questions it can be whatever processing that needs to be done, in this implementation its just a simple print
    print(f'Visited: {node}')
    
    # going through the neighbours of the current node
    # if the neighbour is not in the seen hashset, add it and keep recursively going down
    for neighbour in adj_list[node]:
        if neighbour not in seen:
            seen.add(neighbour)
            recursive_dfs(neighbour)

# iterative DFS
def iterative_dfs(node):
    # create hashset to keep track of nodes that have been looked at already
    seen = set()
    seen.add(node)
    
    # using stack for iterative DFS
    stack = [node]
    
    # while there are values in the stack, delete the first value and process it (printing it in this implementation)
    # then go through its neighbours and if the neighbours are not in the set, add them to the hashset and the stack
    while stack:
        delete = stack.pop()
        print(f'Visited: {delete}')
        
        for neighbour in adj_list[delete]:
            if neighbour not in seen:
                seen.add(neighbour)
                stack.append(neighbour)   

# BFS
def bfs(node):
    # using a hashset to keep track of nodes already visited
    seen = set()
    seen.add(node)
    
    # using queue for BFS since we wanna visit all neighbours of a specific node before going next
    q = deque()
    q.append(node)
    
    # while there are elements in teh queue, delete the first element and process it (in this implementaion just printing it)
    # go through the adjacency list and find the current nodes neighbours
    # if the neighbours are not in the hashset (so they havent been seen), add them to the hashset and to the back of the queue
    while q:
        delete = q.popleft()
        print(f'Visisted: {delete}')
        
        for neighbour in adj_list[delete]:
            if neighbour not in seen:
                seen.add(neighbour)
                q.append(neighbour)

# Recursive DFS
print('\nRecursive DFS')
seen = set()
seen.add(0)
recursive_dfs(0)

# Iterative DFS
print('\nRecursive DFS')
iterative_dfs(0)

# BFS
print('\nRecursive DFS')
bfs(0)
