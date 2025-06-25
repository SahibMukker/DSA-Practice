'''
You are given an m x n 2-D integer array matrix and an integer target.
Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?

Ex 1.
Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
Output: true

Ex 2.
Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15
Output: false

Expected Time Complexity: O(log(m * n))
Expected Auxiliary Space: O(1)

Completed in 36 mins 43 secs, acc had right logic but i wasnt checking the rows properly, 
(had matrix[mid][0] for both checks but should have been matrix[mid][-1] for top and matrix[mid][0] for bot)

RUN 2: June 24th 2025
Completed in 28 mins 55 secs, was doing wrong pointer change in first binary search (swapped top and bot), 
calculated rows/cols wrong (did len(matrix), len(matrix) - 1 instead of len(matrix), len (matrix[0]))
in second binary search did checked for mid > target instead of matrix[row][mid] > target

'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1

        # this binary search goes through matrix and looks for the row we gotta search
        while top <= bot:
            mid = (top + bot) // 2

            # if leftmost value is bigger than target, move to below
            if matrix[mid][0] > target:
                bot = mid - 1
            # if rightmost value is smaller than target, move to above row
            elif matrix[mid][-1] < target:
                top = mid + 1
            
            # found the row
            else:
                break
        
        row = (top + bot) // 2
        lo, hi = 0, cols - 1
        
        # this binary search goes through found row and looks for the target
        while lo <= hi:
            mid = (lo + hi) // 2

            if matrix[row][mid] < target:
                lo = mid + 1
            
            elif matrix[row][mid] > target:
                hi = mid - 1
            
            else:
                return True
        
        return False

# RUN 2: June 24th 2025
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1

        # binary search to find row
        while top <= bot:
            row = (top + bot) // 2

            if matrix[row][-1] < target:
                top = row + 1
            elif matrix[row][0] > target:
                bot = row - 1
            else:
                break
        
        # getting row
        row = (top + bot) // 2
        l, r = 0, cols - 1

        # binary searching the row target should be in
        while l <= r:
            mid = (l + r) // 2

            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                return True
        
        return False