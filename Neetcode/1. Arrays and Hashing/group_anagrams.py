'''
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Ex.
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Expected Time Complexity: O(m*n), m is number of strings, n is length of longest string
Expected Auxiliary Space: O(n)

Completed in 37 mins 3 secs
honestly had no idea what to do had to look up neetcode solution

Completed 22 mins 19 secs, redid again and wrote more concise comment code to make understanding more clear
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # mapping character count to list of anagrams
        # defaultdict with empty list key doesnt exist
        result = defaultdict(list)

        for s in strs:
            # size 26 array that goes from a...z
            count = [0]*26
            for c in s:
            # mapping a to index 0, z to index 25
            # can do this by getting ascii value with ord() function
            # so get ascii value of character we at and subtract by ascii value
            # of a and thatll give the index
            # ex. a = 80, c = 82, 82-80 = 2 therefore index 2 = c
            # incrementing by 1 so num occurances is acc counted
                count[ord(c) - ord("a")] += 1
            
            # so at the key of the specific letters (ex. lets say key is 1e, 1a, 1t)
            # all words that have that exact lettering are mapped to that key
            # but cant do result[count] because count is a list and lists cant be keys (since mutable)
            # therefore need to convert to a tuple
            result[tuple(count)].append(s)
        
        # this only returns the grouped anagrams and not the keys, if dont do .values()
        # get error
        return result.values()
    
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        
        # iterate through list of words
        for s in strs:
            # making array of length 26, default val 0
            # will increment it by index of different letters by 1 as they come up
            count = [0]*26

            # go through the characters in the word currently iterating through
            for c in s:
                # this array will increase occurance of whatever letter currently on
                count[ord(c) - ord('a')] += 1

            # map count to the current word, need to make count a tuple
            # since cant put an array in a hashmap
            result[tuple(count)].append(s)
        
        # return result.values since we only want the sorted list and not the keys
        # (which is the count of the different letters)
        return result.values()