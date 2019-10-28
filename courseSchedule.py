from collections import defaultdict
from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        edge = defaultdict(list)
        degree = [0 for i in range(numCourses)]
        for i, j in prerequisites:
            edge[j].append(i)
            degree[i]+=1
        queue = deque([])
        count = 0
        for i in range(len(degree)):
            if degree[i] == 0:
                queue.append(i)
        while queue:
            node = queue.popleft()
            count+=1
            for neighbor in edge[node]:
                degree[neighbor]-=1
                if degree[neighbor] == 0:
                    queue.append(neighbor)
        return count==numCourses
                
