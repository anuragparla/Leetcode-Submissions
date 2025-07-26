from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 0:
            return True 
        indegrees = [0] * numCourses
        prereqToCoursesMap = dict()
        for i in range(len(prerequisites)):
            to = prerequisites[i][0]
            fromm = prerequisites[i][1]
            indegrees[to] = indegrees[to] + 1
            if fromm not in prereqToCoursesMap:
                prereqToCoursesMap[fromm] = [to]
            else:
                prereqToCoursesMap[fromm].append(to)
        queue = deque()
        count = 0
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                queue.append(i)
                count += 1
        while queue:
            print('q')
            print(queue)
            curr = queue.popleft()
            print('c')
            print
            if curr in prereqToCoursesMap:
                edges = prereqToCoursesMap[curr]
                if edges is None:
                    continue
                for e in edges:
                    indegrees[e] -= 1
                    if indegrees[e] == 0:
                        queue.append(e)
                        count += 1 
        return count == numCourses
            
            

