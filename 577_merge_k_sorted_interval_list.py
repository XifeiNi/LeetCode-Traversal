"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """
    def mergeKSortedIntervalLists(self, intervals):
        result = []
        heap = []
        for index, array in enumerate(intervals):
            if len(array) == 0:
                continue
            heapq.heappush(heap, (array[0].start, array[0].end, index, 0))
             
        while len(heap):
            start, end, x, y = heap[0]
            heapq.heappop(heap)
            self.push_back(result, Interval(start, end))
            if y + 1 < len(intervals[x]):
                heapq.heappush(heap, (intervals[x][y + 1].start, intervals[x][y + 1].end, x, y + 1))
            
        return result
    def push_back(self, intervals, interval):
        if not intervals:
            intervals.append(interval)
        last_interval = intervals[-1]
        if last_interval.end < interval.start:
            intervals.append(interval)
            return
        last_interval.end = max(interval.end, last_interval.end)
