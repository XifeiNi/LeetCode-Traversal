from collections import deque
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = deque([(start[0], start[1], 0)])
        minDist = -1
        while queue:
            i, j, front = queue.popleft()
            maze[i][j] = 2
            if i == destination[0] and j == destination[1]:
                minDist = front if minDist == -1 else min(minDist, front)
            for deltaX, deltaY in DIRECTIONS:
                row, col = i + deltaX, j + deltaY
                count = 0
                while 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] != 1:
                    row += deltaX
                    col += deltaY
                    count += 1
                row -= deltaX
                col -= deltaY
                if maze[row][col] == 0:
                    queue.append((row, col, front + count))
        return minDist
