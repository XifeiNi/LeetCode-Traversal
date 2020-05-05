import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        visited = {1}
        for i in range(n):
            val = heapq.heappop(heap)
            for factor in [2, 3, 5]:
                if factor * val not in visited:
                    heapq.heappush(heap, factor * val)
                    visited.add(factor * val)
        return val
