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
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # mapping letter : num occurances
        hash1 = {}
        hash2 = {}

        # going through the two strings counting the frequency of the different letters
        # len(s) because both s and t are same length (so could do len(t) as well, its the same)
        for i in range(len(s)):
            # s[i] is the key (so everytime we encounter a letter)
            # if key does not exist, give it default value of 0
            hash1[s[i]] = 1 + hash1.get(s[i], 0)
            hash2[t[i]] = 1 + hash2.get(t[i], 0)
        
        # iterating through hashmap to make sure the num of letters is the same
        for c in hash1:
            # if both strings dont have same number of occurances, return false
            # need to do .get on hash2 in case a specific letter doesnt exist, give it
            # default value of 0
            # because strings can be same size but composed of different letters
            if hash1[c] != hash2.get(c, 0):
                return False
        
        return True