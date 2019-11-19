from collections import defaultdict, deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        edges = defaultdict(list)
        degree = [0 for i in range(numCourses)]
        for i , j in prerequisites:
            edges[j].append(i)
            degree[i]+=1
        queue, ret = deque([]), []
        for i in range(numCourses):
            if degree[i] == 0:
                queue.append(i)
        while queue:
            node = queue.popleft()
            ret.append(node)
            for neighbor in edges[node]:
                degree[neighbor]-=1
                if degree[neighbor] == 0:
                    queue.append(neighbor)
        if len(ret) == numCourses:
            return ret
        else:
            return []
