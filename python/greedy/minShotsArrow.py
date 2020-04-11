class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if points == None or not points:
            return 0
        points.sort(key = lambda x : x[1])
        ans, lastEnd = 1, points[0][1]
        for i in range(1, len(points)):
            if points[i][0] > lastEnd:
                ans += 1
                lastEnd = points[i][1]
        return ans
