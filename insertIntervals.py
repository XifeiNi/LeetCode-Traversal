class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        result = []
        position = 0
        for interval in intervals:
            if interval[1] < newInterval[0]:
                result.append(interval)
                position+=1
            elif interval[0] > newInterval[1]:
                result.append(interval)
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
        result.insert(position, newInterval)
        return result
