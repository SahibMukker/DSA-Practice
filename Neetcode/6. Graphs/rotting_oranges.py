'''
You are given a 2-D matrix grid. Each cell can have one of three possible values:

0 representing an empty cell
1 representing a fresh fruit
2 representing a rotten fruit

Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then the fresh fruit also becomes rotten.
Return the minimum number of minutes that must elapse until there are zero fresh fruits remaining. If this state is impossible within the grid, return -1.

Ex 1.
Input: grid = [[1,1,0],[0,1,1],[0,1,2]]
Output: 4

Ex 2.
Input: grid = [[1,0,1],[0,2,0],[1,0,1]]
Output: -1

Expected Time Complexity: O(n * m)
Expected Auxiliary Space: O(n * m)

Completed in 40 mins 24 secs
this felt really similar to num islands, had most of the logic down but my implementation wasnt working because i wasnt keep track of fresh fruit,
i thought i could just look at number of rotten fruits in a queue and fresh fruit in a set but i wasnt properly keeping track so it wasnt working
after looking at a bit of the solution, i realized that i needed to keep track of fruits, other than that most of my logic was sound cause this quesiton
was so similar to num islands
'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # queue needed for BFS, initializing fresh fruit count and time count 
        # using queue to keep track of rotten fruits
        q = deque()
        fresh = 0
        time = 0

        # getting rows and columns
        rows, cols = len(grid), len(grid[0])
        
        # for grid at coordinate [r][c], if it == 1 then its a fresh fruit add to it
        # if it is 2, then its a rotten fruit, add it to the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        # directions right, left, down, up
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # run while loop as long as there are fresh fruit and items in the queue (rotten fruit)
        while fresh > 0 and q:
            # need to run this for as long as there are items in the queue
            for i in range(len(q)):
                # unpack tuple (so coordinate of current rotten fruit)
                r, c = q.popleft()

                # apply the different direction changes to the coordinate
                # if (after the direction change) it is in bounds, and there is an adjacent fresh fruit
                # update it to be a rotten fruit, add the now new rotten fruits coordinates to the queue,
                # decrement fresh fruit by 1
                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    if (row in range(rows) and col in range(cols) and grid[row][col] == 1):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1

            # increment time by 1 for each iteration
            time += 1
            
        # if there are no more fresh fruit, return time
        # if there are fresh fruit but they cant be converted, return -1 (as per question)
        if fresh == 0:
            return time
        else:
            return -1