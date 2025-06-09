'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
write a function to check whether these edges make up a valid tree.

Ex 1.
Input:
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

Output:
true

Expected Time Complexity: O(V + E)
Expected Auxiliary Space: O(V)

Completed in 42 mins 14 secs
had right approach but wasnt intializing queue properly (didnt realize i had to include parent node)
and i also didnt implement the neighours == parent check because i thought i was already checking for cycles
but forgot to realize i need to consider backtracking since its an undirected graph
'''

from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A GRAPH IS A VALID TREE IF IT IS ACYCLIC, CONNECTED, EDGES = N-1 (N = NUM NODES)
        
        # edges should = n-1, so if they dont return false
        if len(edges) > (n-1):
            return False
        
        # creating adjacency list
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # creating seen hashset to keep track of nodes that have already been seen
        # initializing queue with a tuple where 0 is curr node and -1 is placeholder for parent node
        # need to initialize as tuple to distinguish between valid backtracking and actual cycles
        seen = set()
        q = deque([(0, -1)])
        seen.add(0)

        while q:
            # unpacking tuple where first value is curr and second value is parent
            curr, parent = q.popleft()

            for neighbours in adj[curr]:
                # dont go back to the node just came from (since undirected graph)
                # its okay to see the neighbour again, but then the next if statement checks
                # if the value is already in seen and if it is, it is a cycle
                if neighbours == parent:
                    continue

                if neighbours in seen:
                    return False
                
                # if not in seen, add the current neighbour to hashset
                # and add to queue where neighbours is now curr and curr is the parent of the neighbours
                seen.add(neighbours)
                q.append((neighbours, curr))

        # if while loop ends and we chillin, finally check if the number of nodes in the hashset
        # is the same as the number of nodes that should be in the tree
        # if thats true itll return true, if its not then itll return false
        return len(seen) == n