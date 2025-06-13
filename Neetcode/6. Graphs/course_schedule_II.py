'''
You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

Return a valid ordering of courses you can take to finish all courses. If there are many valid answers, return any of them. 
If it's not possible to finish all courses, return an empty array.

Ex 1.
Input: numCourses = 3, prerequisites = [[1,0]]
Output: [0,1,2]
Explanation: We must ensure that course 0 is taken before course 1.

Ex 2.
Input: numCourses = 3, prerequisites = [[0,1],[1,2],[2,0]]
Output: []
Explanation: It's impossible to finish all courses.

Expected Time Complexity: O(V + E)
Expected Auxiliary Space: O(V)

Completed in 58 mins 7 secs
kind of knew what was going on cause of course schedule 1 but needed to look at neetcode cause my implementation was wrong 
(didnt think of using a separate set for cycle dection, was using seen set and forgot to append output course to list)
'''
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        prereq = {course: [] for course in range(numCourses)}

        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        # course has 3 possible states: been seen, currently being seen, unseen
        output = []
        seen, cycle = set(), set()

        def dfs(crs):
            # detected cycle
            if crs in cycle:
                return False
            
            if crs in seen:
                return True
            
            # keeping track of course in path before recursion
            cycle.add(crs)
            for pre in prereq[crs]:
                # if cycle detected
                if dfs(pre) == False:
                    return True
            # atp were done recursion and can remove from cycle and add to seen and final output list
            cycle.remove(crs)
            seen.add(crs)
            output.append(crs)
            
            return True

        for course in range(numCourses):
            # if cycle detected by dfs return empty array
            if dfs(course) == False:
                return []
            
        return output
            





