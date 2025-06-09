'''
Given a node in a connected undirected graph, return a deep copy of the graph.

Each node in the graph contains an integer value and a list of its neighbors.
The graph is shown in the test cases as an adjacency list. 
An adjacency list is a mapping of nodes to lists, used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.
For simplicity, nodes values are numbered from 1 to n, where n is the total number of nodes in the graph. 
The index of each node within the adjacency list is the same as the node's value (1-indexed).

The input node will always be the first node in the graph and have 1 as the value.

Example 1:

Input: adjList = [[2],[1,3],[2]]
        1 - 2
           /
          3
Output: [[2],[1,3],[2]]
Explanation: There are 3 nodes in the graph.
Node 1: val = 1 and neighbors = [2].
Node 2: val = 2 and neighbors = [1, 3].
Node 3: val = 3 and neighbors = [2].

Expected Time Complexity: O(V + E), where V = vertices (or nodes n) and E = edges
Expected Auxiliary Space: O(V)

Completed in 38 mins 25 secs
i acc had most of the logic down which im surprised and my approach was right but i was messing up properly adding neighbours to the copy
and wasnt properly making a copy of the node (i was just copying node values which doesnt work since the copied value wasnt going anywhere)
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # if no node then return none
        if not node:
            return None

        # using hashmap, mapping old : copy and then making copy of node
        oldToCopy = {}
        oldToCopy[node] = Node(node.val)

        # since bfs, using queue
        q = deque()
        q.append(node)

        # while there are items in the queue, have a curr variable that is the current popped value
        # then, for the current neighbour of current, if the neighbour isnt in the hashmap
        # then create a node for the neighbour and map the current to the original copy
        # and add the neighbour to the queue
        while q:
            curr = q.popleft()
            for neighbour in curr.neighbors:
                if neighbour not in oldToCopy:
                    oldToCopy[neighbour] = Node(neighbour.val)
                    q.append(neighbour)
                
                # link clone of current node to clone of its neighbour
                # to the copied version of curr, add the copied neighbour to its neighbour list
                # so to current's (which is copy) neighbours, append the neighbour
                oldToCopy[curr].neighbors.append(oldToCopy[neighbour])
        
        # returning the copy
        return oldToCopy[node]