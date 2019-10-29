from collections import defaultdict
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        first_map = self.getMap(nums1)
        second_map = self.getMap(nums2)
        ret = []
        for key in first_map.keys():
            if second_map[key] > 0:
                ret.append(key)
        return ret
    def getMap(self, nums):
        ret = defaultdict(int)
        for i in range(len(nums)):
            ret[nums[i]]+=1
        return ret
