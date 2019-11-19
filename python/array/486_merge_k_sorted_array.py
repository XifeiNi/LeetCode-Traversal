import heapq
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        result = []
        heap = []
        for index, array in enumerate(arrays):
            if len(array) == 0:
                continue
            heapq.heappush(heap, (array[0], index, 0))
        while len(heap):
            val, x, y = heap[0]
            result.append(val)
            heapq.heappop(heap)
            if y + 1 < len(arrays[x]):
                heapq.heappush(heap, (arrays[x][y+1], x, y+1))
        return result

