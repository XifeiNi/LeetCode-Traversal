class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        cols, rows = [], []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)
        rows.sort()
        cols.sort()
        mid = len(cols)//2
        x, y = rows[mid], cols[mid]
        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ret += abs(i - x) + abs(j - y)
        return ret
