from collections import defaultdict
class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hitMap = defaultdict(int)
        

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        self.hitMap[timestamp]+=1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        ret = 0
        for key in self.hitMap.keys():
            if key >= timestamp - 300 + 1:
                ret+=self.hitMap[key]
        return ret
