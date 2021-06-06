import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            distance = - (x*x + y*y)
            if len(heap) == k:
                
                heapq.heappush(heap, (distance, x, y))
                heapq.heappop(heap)
            else:
                heapq.heappush(heap, (distance, x, y))
        return [(x, y) for _, x, y in heap]