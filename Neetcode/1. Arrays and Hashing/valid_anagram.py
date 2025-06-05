'''
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Ex 1.
Input: s = "racecar", t = "carrace"
Output: true

Ex 2.
Input: s = "jar", t = "jam"
Output: false

Expected Time Complexity: O(n + m)
Expected Auxiliary Space: O(n)

Comleted in 33 mins 53 secs
couldnt figure out key error because i didnt know how to account for if one string has characters that dont exist in the other
(i.e. if one string has a letter that the other doesnt have) but then found out about .get and how i can set a default value of 0 of the character that doesnt exist

ALSO if interviewer asks how to get O(1) space, can use sorting algorithm but this would increase time complexity (ex. sorted(s) == sorted(t), or create my own sorting algo)

Completed in 30 mins, couldnt finish by myself, replaced old code comment code with new code that is more clear
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # mapping character : num occurances of that character
        hash1 = {}
        hash2 = {}

        # counting the frequency of letters
        for i in range(len(s)):
            # hash1[s[i]] counts occurance of characters in strings
            # therefore hash1[] is us getting count, s[i] is going through the string
            # and i is the index in the string (so the character we are looking at)
            # increment previous counts of that character by 1, if it doesnt exist
            # set it to 0 and add 1 since we just encountered it
            hash1[s[i]] = 1 + hash1.get(s[i], 0)
            hash2[t[i]] = 1 + hash2.get(t[i], 0)
        
        # iterate through the first hash and if the count is not the same in hash 1 as hash2
        # then return false (need to do hash2.get in the event the two hash's dont contain the same letters)
        for c in hash1:
            if hash1[c] != hash2.get(c, 0):
                return False
        
        return True