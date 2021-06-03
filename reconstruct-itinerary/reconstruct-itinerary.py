class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = self.buildGraph(tickets)
        results = []
        self.dfs(graph, "JFK", results)
        return reversed(results)
        
    def buildGraph(self, tickets):
        graph = collections.defaultdict(list)
        for start, end in tickets:
            graph[start].append(end)
        
        for key in graph:
            graph[key] = collections.deque(sorted(graph[key]))
        return graph
    def dfs(self, graph, current, results):
        while graph[current]:
            neighbor = graph[current].popleft()
            self.dfs(graph, neighbor, results)
        results.append(current)
        