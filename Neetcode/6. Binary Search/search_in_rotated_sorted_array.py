'''
You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. 
For example, the array nums = [1,2,3,4,5,6] might become:
    [3,4,5,6,1,2] if it was rotated 4 times.
    [1,2,3,4,5,6] if it was rotated 6 times.
Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.
You may assume all elements in the sorted rotated array nums are unique,
A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

Ex 1.
Input: nums = [3,4,5,6,1,2], target = 1
Output: 4

Ex 2.
Input: nums = [3,5,6,0,1,2], target = 4
Output: -1

Expected Time Complexity: O(logn)
Expected Auxiliary Space: O(1)

Completed in 58 mins 49 secs, was not considering all the different comparison scenarios
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        result = -1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                result = mid
                break
            
            # in left portion
            if nums[mid] >= nums[l]:
                
                # search right side
                if nums[l] > target or nums[mid] < target:
                    l = mid + 1
                # target is less than middle, middle of left so search left
                else:
                    r = mid - 1

            # in right portion
            else:
                # search left side
                if nums[mid] > target or nums[r] < target:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return result            