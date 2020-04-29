class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        max_gold = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    max_gold = max(max_gold, self.dfs(grid, i, j))
        return max_gold
    def dfs(self, grid, row, col):
        max_gold = 0
        grid[row][col] = -grid[row][col]
        
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0 <= row + dx < len(grid) and 0 <= col + dy < len(grid[0]) and grid[row + dx][col + dy] > 0:
                max_gold = max(max_gold, self.dfs(grid, row + dx, col + dy))
        grid[row][col] = abs(grid[row][col])
        return max_gold + grid[row][col]
