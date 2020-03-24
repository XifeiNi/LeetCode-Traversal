class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if len(grid) <= 2 or len(grid[0]) <= 2:
            return 0
        for i in range(len(grid)):
            if grid[i][0] == 0:
                grid[i][0] = 3
            if grid[i][len(grid[0]) - 1] == 0:
                grid[i][len(grid[0]) - 1] = 3
        for i in range(len(grid[0])):
            if grid[0][i] == 0:
                grid[0][i] = 3
            if grid[len(grid) - 1][i] == 0:
                grid[len(grid) - 1][i] = 3
        island = 0
        print(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:

                    if self.bfs(grid, i, j):
                        #print("(" + str(i) + " " + str(j) + ")")
                        island += 1
        return island
    def bfs(self, grid, x, y):
        queue = collections.deque([(x, y)])
        grid[x][y] = 2
        ret = True
        while queue:
            x, y = queue.popleft()
            for deltaX, deltaY in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if self.bounded(grid, x + deltaX, y + deltaY):
                    grid[x + deltaX][y + deltaY] = 2
                    ret = False
                if self.isValid(grid, x + deltaX, y + deltaY):
                    queue.append((x + deltaX, y + deltaY))
                    grid[x + deltaX][y + deltaY] = 2
        return ret
    def isValid(self, grid, x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0
    def bounded(self, grid, x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 3 
