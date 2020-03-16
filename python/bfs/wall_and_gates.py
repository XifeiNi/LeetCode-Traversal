from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        for row in range(len(rooms)):
            for col in range(len(rooms[0])):
                if rooms[row][col] != 0:
                    continue
                self.bfs(rooms, row, col)
    def bfs(self, rooms, row, col):
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set([(row, col)])
        
        queue = deque([(row, col, 0)])
        while queue:
            cur_row, cur_col, step = queue.popleft()
            if rooms[cur_row][cur_col] < step:
                continue
            rooms[cur_row][cur_col] = step
            next_step = step + 1
            for delX, delY in DIRECTIONS:
                next_row, next_col = cur_row + delX, cur_col + delY
                
                if self.isValid(rooms, next_row, next_col) and (next_row, next_col) not in visited:
                    queue.append((next_row, next_col, next_step))
                    visited.add((next_row, next_col))
    def isValid(self, rooms, row, col):
        if 0 <= row < len(rooms) and 0 <= col < len(rooms[0]):
            if rooms[row][col] != -1 and rooms[row][col] != 0:
                return True;
        return False
