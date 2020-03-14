from collections import deque
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        queue = deque([start])
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while queue:
            i, j = queue.pop()
            maze[i][j] = 2
            if i == destination[0] and j == destination[1]:
                return True
            for delta_x, delta_y in DIRECTIONS:
                row = delta_x + i
                col = delta_y + j
                while 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] != 1:
                    row += delta_x
                    col += delta_y
                row -= delta_x
                col -= delta_y
                if maze[row][col] == 0:
                    queue.append((row, col))
        return False
