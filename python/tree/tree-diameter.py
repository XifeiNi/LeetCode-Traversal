from collections import defaultdict, deque
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        queue = deque([edges[0][0]])
        visited = set()
        while queue:
            node = queue.popleft()
            for vertex in graph[node]:
                if vertex in visited:
                    continue
                queue.append(vertex)
                visited.add(vertex)
        queue = deque([node])
        visited = set()
        dis = 0
        while queue:
            length = len(queue)
            for i in range(length):
                v = queue.popleft()
                for nodes in graph[v]:
                    if nodes  in visited:
                        continue
                    visited.add(nodes)
                    queue.append(nodes)
            dis += 1
        return dis  - 1
