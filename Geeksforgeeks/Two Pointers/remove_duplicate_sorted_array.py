'''
Given a sorted array arr. Return the size of the modified array which contains only distinct elements.
Note:
1. Don't use set or HashMap to solve the problem.
2. You must return the modified array size only where distinct elements are present and modify the original array such that all the distinct elements come at the beginning of the original array.

Ex 1.
Input: arr = [2, 2, 2, 2, 2]
Output: [2]
Explanation: After removing all the duplicates only one instance of 2 will remain 
i.e. [2] so modified array will contains 2 at first position and you should return 1 after modifying the array, 
the driver code will print the modified array elements.

Ex 2.
Input: arr = [1, 2, 4]
Output: [1, 2, 4]
Explation:  As the array does not contain any duplicates so you should return 3.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Completed in 14 mins 41 secs
'''
#User function template for Python
class Solution:
    def removeDuplicates(self, arr):
        
        if len(arr) == 0:
            return []
        
        # two pointers i and j, if array at i is not equal to array at j, move j pointer up and move the value of array at i to array at j    
        j = 0
        for i in range(1, len(arr)):
            if arr[i] != arr[j]:
                j += 1
                arr[j] = arr[i]
        
        return j + 1