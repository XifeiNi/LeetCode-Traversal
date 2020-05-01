from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges):
            return False
        neighbors = defaultdict(list)
        for node1, node2 in edges:
            neighbors[node1].append(node2)
            neighbors[node2].append(node1)
        
        visited, queue = set(), deque([])
        queue.append(0)
        visited.add(0)
        
        while queue:
            current = queue.popleft()
            visited.add(current)
            for neighbor in neighbors[current]:
                if neighbor not in visited:
                    queue.append(neighbor)
        return len(visited) == n        
