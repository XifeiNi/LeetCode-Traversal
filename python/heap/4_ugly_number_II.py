import heapq

class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nthUglyNumber(self, n):
        heap = [1]
        visited = set()
        value = None
        for i in range(n):
            value = heapq.heappop(heap)
            for factor in [2, 3, 5]:
                if factor*value not in visited:
                    visited.add(factor*value)
                    heapq.heappush(heap, value*factor)
        return value

