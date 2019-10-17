from collections import defaultdict
class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashMap = defaultdict(list)
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.hashMap[key].append([value, timestamp])
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if len(self.hashMap[key]) == 0:
            return ""
        return self.findClosest(timestamp, self.hashMap[key])
    def findClosest(self, timestamp, mapList):
        diff = sys.maxsize
        ret = ""
        start, end = 0, len(mapList) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if mapList[mid][1] < timestamp:
                start = mid
            else:
                end = mid
        if mapList[end][1] <= timestamp:
            return mapList[end][0]
        if mapList[start][1] <= timestamp:
            return mapList[start][0]
        
        return ""
            


