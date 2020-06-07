class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(grid))] for _ in range(len(grid[0]))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j > 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0 and i > 0:
                    grid[i][j] += grid[i - 1][j]
                elif i > 0 and j > 0:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[len(grid) - 1][len(grid[0]) - 1]
