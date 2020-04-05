class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        return self.bfs(x, y)
    def bfs(self, x, y):
        if (x, y) == (0, 0):
            return 0
        queue = deque([[0, 0, 0]])
        seen = set()
        while queue:
            i, j, distance = queue.popleft()
            seen.add((i, j))
            for deltaX, deltaY in [(1,2),(2,1),(1,-2),(2,-1),(-1,2),(-2,1), (-1,-2),(-2,-1)]:
                
                if (i + deltaX, j + deltaY) in seen:
                    continue
                if (i + deltaX, j + deltaY) == (x, y):
                    return distance + 1
                seen.add((i + deltaX, j + deltaY))
                queue.append([i + deltaX, j + deltaY, distance + 1])
