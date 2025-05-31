'''
Given a matrix mat[][] of size n*n, where each row and column is sorted in non-decreasing order. Find the kth smallest element in the matrix.

Ex 1.
Input: n = 4, mat[][] = [[16, 28, 60, 64], [22, 41, 63, 91], [27, 50, 87, 93], [36, 78, 87, 94]], k = 3
Output: 27
Explanation: 27 is the 3rd smallest element.

Ex 2.
Input: n = 4, mat[][] = [[10, 20, 30, 40], [15, 25, 35, 45], [24, 29, 37, 48], [32, 33, 39, 50]], k = 7
Output: 30
Explanation: 30 is the 7th smallest element.

Completed in 52 mins 17 secs

thought maybe i could do dfs and then map values to a hashmap in a sorted way and then check k smalled by looking for the kth key, but couldnt figure it out
then i looked at the comments and they all were doing binary search and i havent touched that since like march or something so i got the structure of the
binary search right for the most part, but couldnt figure out the countLessEqual function (knew i needed a helper function but not how to write it) so had
to look at a solution in the comments and then have chat gpt explain whats going on
'''
class Solution:
    def kthSmallest(self, matrix, k):
        
        # getting size of the nxn matrix
        n = len(matrix)
    
        # function to count how many elements in the matrix are <= a given value x
        # can do this efficiently since the matrix is sorted in both rows and columns
        def countLessEqual(x):
            
            # count is number of variables, 
            # setting row so binary search starts from last row,
            # setting column to start from first column
            count = 0 
            row = n - 1  
            col = 0      
    
            # moving through the matrix in a stair-case fashion
            # if current element is <= x, then all elements above it in the same column are also <= x
            # if current element is > x, move up to find smaller values
            while row >= 0 and col < n:
                if matrix[row][col] <= x:
                    # all elements in this column up to the current row are <= x
                    count += row + 1
                    # move right (so to the next column)
                    col += 1
                else:
                    # current element is > x, so move up to find smaller values
                    row -= 1
            return count  # return the total count of elements <= x
    
        # initializing the binary search range
        # the smallest possible value is top left element
        # the largest possible value is bottom right element
        low = matrix[0][0]
        high = matrix[n - 1][n - 1]
    
        # binary search
        while low < high:
            # find mid
            mid = (low + high) // 2
    
            # count how many elements are <= mid
            counter = countLessEqual(mid)
            
            # if k is bigger than counter, that means check top half
            if counter < k:
                low = mid + 1
                
            # if k smaller than counter, that means check bottom half
            else:
                high = mid
    
        # when low == high, found the smallest number with at least k numbers less than or equal to it
        return low
        
        
        
        
        
        
        
        