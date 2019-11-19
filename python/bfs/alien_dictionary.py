from collections import defaultdict
import heapq
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        graph = self.buildGraph(words)
        return self.topologicalSorting(graph)
    def buildGraph(self, words):
        graph = {}
        for word in words:
            for c in word:
                graph[c] = set()
        
        for i in range(len(words) - 1):
            for j in range(min(len(words[i]), len(words[i+1]))):
                if words[i][j] != words[i+1][j]:
                    graph[words[i][j]].add(words[i+1][j])
                    break
        return graph
    
    def topologicalSorting(self, graph):
        indegree = defaultdict(int)
        
        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor]+=1
        
        queue = [node for node in graph if indegree[node] == 0]
        heapq.heapify(queue)
        
        order = ""
        while queue:
            node = heapq.heappop(queue)
            order += node
            for neighbor in graph[node]:
                indegree[neighbor]-=1
                if indegree[neighbor] == 0:
                    heapq.heappush(queue, neighbor)
        if len(order) == len(graph):
            return order
        else:
            return ""
