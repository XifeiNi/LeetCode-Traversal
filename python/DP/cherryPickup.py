class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[float('-inf')] * n for _ in range(n)]
        dp[0][0] = grid[0][0]
        for i in range(1, 2 * n - 1):
            for x1 in reversed(range(max(0, i - n + 1), min(i, n - 1) + 1)):
                y1 = i - x1
                g1 = grid[x1][y1]
                for x2 in reversed(range(max(0, i - n + 1), min(i, n -1) + 1)):
                    y2 = i - x2
                    g2 = grid[x2][y2]
                    if g1 < 0 or g2 < 0:
                        dp[x1][x2] = -1
                        continue
                    cur_grid = max(g1, g2) if x1==x2 else g1 + g2
                    left = dp[x1 - 1][x2] if x1 > 0 and y2 > 0 else -1
                    right = dp[x1][x2 - 1] if x2 > 0 and y1 > 0 else -1
                    up = dp[x1 - 1][x2 - 1] if x1 > 0 and x2 > 0 else - 1
                    down = dp[x1][x2] if y1 > 0 and y2 > 0 else -1
                    prev = max(left, up, right, down)
                    dp[x1][x2] = -1 if prev < 0 else prev + cur_grid
        return dp[n-1][n-1] if dp[n-1][n-1] > 0 else 0
