class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key = lambda x: x[1])
        dp = [0 for _ in range(len(endTime) + 1)]
        dp[1] = jobs[0][2]
        for i in range(1, len(endTime)):
            if jobs[i][0] < jobs[i - 1][1]:
                start, end = 0, i + 1
                while start < end:
                    mid = start + (end - start)//2
                    if jobs[mid][1] > jobs[i][0]:
                        end = mid
                    else:
                        start = mid + 1
                dp[i + 1] = max(dp[start - 1 + 1] + jobs[i][2], dp[i])
            else:
                dp[i + 1] = dp[i] + jobs[i][2]
        return dp[-1]