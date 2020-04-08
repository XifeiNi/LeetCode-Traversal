class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        rowcnt, colcnt = 0, [0 for _ in range(len(grid[0]))]
        ret = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 'W':
                    continue
                if col == 0 or grid[row][col - 1] == 'W':
                    rowcnt = 0
                    for c in range(col, len(grid[0])):
                        if grid[row][c] == 'W':
                            break
                        if grid[row][c] == 'E':
                            rowcnt += 1
                if row == 0 or grid[row - 1][col] == 'W':
                    colcnt[col] = 0
                    for r in range(row, len(grid)):
                        if grid[r][col] == 'W':
                            break
                        if grid[r][col] == 'E':
                            colcnt[col] += 1
                if grid[row][col] == '0':
                    ret = max(ret, rowcnt + colcnt[col])
        return ret
