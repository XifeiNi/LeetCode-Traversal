class Solution:
    def expand(self, S: str) -> List[str]:
        
        inBrace = False
        options = []
        graph = []
        for char in S:
            if char == '{':
                inBrace = True
                options = []
                continue
            if char == '}':
                inBrace = False
                graph.append(list(options))
                continue
            if char == ',':
                continue
            if inBrace:
                options.append(char)
            else:
                graph.append([char])
        results = []
        self.dfs(graph, 0, [], results)
        return sorted(results)
    
    def dfs(self, graph, start, path, results):
        if len(path) == len(graph):
            results.append(''.join(path))
            return
        for option in graph[start]:
            path.append(option)
            self.dfs(graph, start + 1, path, results)
            path.pop()
