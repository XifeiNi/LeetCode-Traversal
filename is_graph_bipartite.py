from collections import deque
UNSEEN = 0
RED = 1
BLUE = -1
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        queue = deque([])
        coloring = [UNSEEN for _ in range(len(graph))]
        for i in range(len(graph)):
            if coloring[i] != UNSEEN:
                continue
            queue.append(i)
            coloring[i] = BLUE
            while queue:
                vertex = queue.popleft()
                for element in graph[vertex]:        
                    if coloring[element] == UNSEEN:
                        coloring[element] = -coloring[vertex]
                        queue.append(element)
                    elif coloring[element] != -coloring[vertex]:
                        return False
                    
        return True
            
