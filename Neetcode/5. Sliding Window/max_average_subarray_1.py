'''
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
Any answer with a calculation error less than 10-5 will be accepted.

Ex 1.
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Ex 2.
Input: nums = [5], k = 1
Output: 5.00000

Completed in 47 mins 1 sec, wasnt getting first sum properly, forgot to subtract the currsum when moving over, and was doing nums[k-i] instead of [i-k]
'''
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = 0
        
        # go through first k elements and add them to get first sum and get average
        for i in range(k):
            curr_sum += nums[i]
        
        max_avg = curr_sum / k
        
        # for length of nums, go over by 1, add integer at new val and subtract the removed, calculate the avg and compare max avg and return
        for i in range(len(nums)):
            curr_sum += nums[i]
            curr_sum -= nums[i-k]
            
            avg = curr_sum / k
            max_avg = max(max_avg, avg)
        
        return max_avg