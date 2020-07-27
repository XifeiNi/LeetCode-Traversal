# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:
ARRAY_MAX_SIZE = 10000
class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        start, end = 0, ARRAY_MAX_SIZE
        while start + 1 < end:
            
            mid = (start + end)//2
            if reader.get(mid) < target:
                start = mid
            elif reader.get(mid) > target:
                end = mid
            else:
                return mid
        if reader.get(start) == target:
            return start
        elif reader.get(end) == target:
            return end
        else:
            return -1
