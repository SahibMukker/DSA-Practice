'''
Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without duplicate characters.
A substring is a contiguous sequence of characters within a string.

Ex 1.
Input: s = "zxyzxyz"
Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.

Ex 1.
Input: s = "xxxx"
Output: 1

Expected Time Complexity: O(n), n is length of string
Expected Auxiliary Space: O(m), m is number of unique characters

Completed in 32 mins 59 secs, used this question to learn sliding window concepts, so i had the right idea
of what to do but couldnt figure out how to do it myself so needed to look up solution
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        longest = 0
        seen = set()
        
        # run loop while r is in range of the length of s
        for r in range(len(s)):
            
            # while string at right pointer is in the hashset,
            # remove left pointer value from hashset (cause thats only way it can be in seen)
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            # find longest between current longest and sliding window and add right pointer to seen
            window_length = (r - 1) + 1
            longest = max(longest, window_length)
            seen.add(s[r])
        
        return longest