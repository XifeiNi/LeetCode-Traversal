from collections import deque
UNSEEN = 0
RED = 1
BLUE = -1

class Solution:
    """
    @param graph: the given undirected graph
    @return:  return true if and only if it is bipartite
    """
    def isBipartite(self, graph):
        q = deque([])
        coloring = [0]*len(graph)
        for i in range(len(graph)):
            if coloring[i] != UNSEEN:
                continue
            q.append(i)
            coloring[i] = RED
            while q:
                cur_vertice = q.popleft()
                for element in graph[cur_vertice]:
                    if coloring[element] == UNSEEN:
                        coloring[element] = -coloring[cur_vertice]
                        q.append(element)
                    elif coloring[element] != -coloring[cur_vertice]:
                        return False
        return True
