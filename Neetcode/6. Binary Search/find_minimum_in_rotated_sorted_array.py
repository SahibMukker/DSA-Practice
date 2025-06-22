'''
You are given an array of length n which was originally sorted in ascending order. 
It has now been rotated between 1 and n times. 
For example, the array nums = [1,2,3,4,5,6] might become:
    [3,4,5,6,1,2] if it was rotated 4 times.
    [1,2,3,4,5,6] if it was rotated 6 times.
Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array.
Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.
A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

Ex 1.
Input: nums = [3,4,5,6,1,2]
Output: 1

Ex 2.
Input: nums = [4,5,0,1,2,3]
Output: 0

Ex 3.
Input: nums = [4,5,6,7]
Output: 4

Expected Time Complexity: O(logn)
Expected Auxiliary Space: O(1)

Completed in 57 mins 20 secs, tried to do some calculation for howmany rotations and then based on that see which side to search on
but i couldnt figure out how to do that so i looked at the neetcode solution
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # default setting ersult to be whatever the first index of nums is
        result = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # if at an array with no rotations (so sorted array), result will be
            # the smallest between itself and current left pointer and break out of loop
            if nums[l] < nums[r]:
                result = min(result, nums[l])
                break
            
            mid = (l + r) // 2
            result = min(result, nums[mid])

            # in left sorted portion and want to search right, else in right search left
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        
        return result