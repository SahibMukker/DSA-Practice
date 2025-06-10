'''
You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.
The pair [0, 1], indicates that must take course 1 before taking course 0.
There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.
Return true if it is possible to finish all courses, otherwise return false.

Ex 1.
Input: numCourses = 2, prerequisites = [[0,1]]
Output: true
Explanation: First take course 1 (no prerequisites) and then take course 0.

Ex 2.
Input: numCourses = 2, prerequisites = [[0,1],[1,0]]
Output: false
Explanation: In order to take course 1 you must take course 0, and to take course 0 you must take course 1. So it is impossible.

Completed in 58 mins 47 secs
ngl this question was hard asf. i had some of the logic down like
i knew i need to check for cycles using a set keeping track of prereqs of current course we are on.
but i thought maybe i could do it with BFS but with both BFS and cycle detection, i couldnt figure out how to implement it. 
for cycle detection i used the seen set (same as below solution),but i thought maybe i need to unpack the prerequistes list as a tuple or something (which is wrong).
i just dont know how i couldve thought of this the 'correct way' or how to logic it out properly on my own
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # for every course, initially map it to an empty list
        # mapping course to pre-req list
        reqmap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            reqmap[crs].append(pre)
        
        # seen courses for cycle detection
        seen = set()

        def dfs(crs):
            # this course cant be completed cause of loop
            if crs in seen:
                return False
            
            if reqmap[crs] == []:
                # no prereqs so course can be completed
                return True
            
            # if neither, then add it to the seen set and recursively check its prereq
            seen.add(crs)

            for pre in reqmap[crs]:
                # if dfs returns false, return false
                if not dfs(pre):
                    return False

            # the course can be taken, remove it from the seen set
            seen.remove(crs)
            # set it to empty list since this course can be taken, makes it easier for dfs
            # since we have empty list condition in dfs, no need to run the for loop again
            reqmap[crs] = []
            
            return True

        # call dfs for every course for number of courses we have
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True
