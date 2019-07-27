import heapq
class Solution:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        self.heap = []
        self.k = k

    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num):
        heapq.heappush(self.heap, num)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
    """
    @return: Top k element
    """
    def topk(self):
        # write your code here
        return sorted(self.heap, reverse=True)

