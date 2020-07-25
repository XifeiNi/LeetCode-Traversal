class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        heap = []
        ret, perf = 0, 0
        for e, s in sorted(zip(efficiency, speed), reverse=1):
            heapq.heappush(heap, s)
            perf += s
            if len(heap) > k:
                perf -= heapq.heappop(heap)
            ret = max(ret, perf * e)
        return ret % (10**9 + 7)
