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

Completed in 26 mins 43 secs, acc had right logic but i wasnt checking the rows properly, 
(had matrix[mid][0] for both checks but should have been matrix[mid][-1] for top and matrix[mid][0] for bot)
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