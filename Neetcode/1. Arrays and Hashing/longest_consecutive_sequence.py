'''
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.
The elements do not have to be consecutive in the original array.
You must write an algorithm that runs in O(n) time.

Ex 1.
Input: nums = [2,20,4,10,3,4,5]
Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Completed in 44 mins 27 secs
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # converting array into a set, also variable to keep track of what longest sequence is
        numset = set(nums)
        longest = 0

        # running a loop that goes through the set, and are checking if the previous number exists
        # if it doesn't, the length is 1
        # ex. num = 100, checking if 99 exists. if it doesnt then length of the sequence is 1
        # therefore this num is the start of a sequence
        for num in numset:
            if (num - 1) not in numset:
                length = 1

                # keep increasing length by 1 as long as num + length exists in the set
                # ex. num = 100, this is checking if 101 exists. if it doesnt the code moves to the next num
                while (num + length) in numset:
                    length += 1
                
                # updating longest by seeing whats bigger 
                # (current sequence length or previous longest val)
                longest = max(longest, length)
        
        return longest