'''
Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.
An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. 
You may assume water is surrounding the grid (i.e., all the edges are water).

Ex 1.
Input: grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
Output: 1

Ex 2.
Input: grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
Output: 4

Expected Time Complexity: O(n * m)
Expected Auxiliary Space: O(n * m)

Completed in 58 mins 15 secs
had right logic of solving question (go through cols and rows, if grid at current position is 1 and the coordinate is not in seen, run bfs and increment islands by 1)
but i had no idea how to properly look at neighbours in the grid, so most of the time was spent on figuring that out, couldnt do it so looked up solution
and spent like 20 mins trying to understand why it works and the logic behind it
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return  0
        # len(grid) checks num of items in list, len(grid[0]) checks num items in sublist
        # ex: len(grid) = 3 since there are 3 different items in list, len(grid[0]) = 2 since the there are 2 items in sublist
        # grid = [
        # [0, 1]
        # [1, 1]
        # [1, 0]  
        #]
        rows, cols = len(grid), len(grid[0])
        seen = set()

        islands = 0

        def bfs (r, c):
            # intializing queue and adding to set the current node (tuple since given r,c)
            q = deque()
            seen.add((r, c))
            q.append((r, c))
            
            # while queue not empty, 'expanding island'
            while q:
                row, col = q.popleft()
                # checking adjacent positions (down, up, right, left)
                directions = [[1, 0], [-1, 0], [0,1], [0,-1]]
                
                # dr = direction of row (or change in row going up or down)
                # dc = direction of column (or change in column going left or right)
                # so for current cell, look at all directions up down left and right
                for dr, dc in directions:
                    # this makes the change in the row and column to visit neighbour cell and see
                    # if there is a 1 that has not already been seen
                    r, c = row + dr, col + dc
                    # check if directions in bound (so we not in position that doesnt exist) 
                    # for each of these directions and position is land and hasnt already been seen, 
                    # append to seen and queue
                    # checking (r, c) in hashset because grid[r][c] = '1' is value and not acc coordinate
                    # need to add the acc coordinate to the hashset
                    if (r in range(rows) and c in range(cols) and grid[r][c] == '1' and (r, c) not in seen):
                        q.append((r, c))
                        seen.add((r,c))

        # go through rows and columns, if the current grid value is 1 and current coordinate is not in seen
        # run bfs to find all the coordinates belonging to the current island and increment island by 1
        # after all land for current island has been found
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in seen:
                    # BFS
                    bfs(r, c)
                    islands += 1
        
        return islands