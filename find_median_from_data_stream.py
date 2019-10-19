import heapq
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxHeap, self.minHeap = [], []
        
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.maxHeap) <= len(self.minHeap):
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)
            
        if len(self.maxHeap) == 0 or len(self.minHeap) == 0:
            return
        if -self.maxHeap[0] > self.minHeap[0]:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.minHeap) == len(self.maxHeap):
            
            return (self.minHeap[0] - self.maxHeap[0])/2.0
        return -self.maxHeap[0]
        
