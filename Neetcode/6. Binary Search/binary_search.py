'''
You are given an array of distinct integers nums, sorted in ascending order, and an integer target.
Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.
Your solution must run in O(logn) time.

Ex 1.
Input: nums = [-1,0,2,4,6,8], target = 4
Output: 3

Ex 2.
Input: nums = [-1,0,2,4,6,8], target = 3
Output: -1

Expected Time Complexity: O(logn)
Expected Auxiliary Space: O(1)

Completed in 10 mins 47 secs, got it right but made mistake where i checked nums[mid] > target and l = mid + 1 instead of r = mid - 1
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] > target:
                r = mid - 1
            
            elif nums[mid] < target:
                l = mid + 1
            
            else:
                return mid
            
        return -1