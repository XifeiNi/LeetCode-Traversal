class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        left, right = -1, -1
        start, end = 0, len(nums)-1
        while start + 1 < end: 
            mid = (start + end)//2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid
        if nums[start] == target:
            right = start
        if nums[end] == target:
            right = end
        
        start, end = 0, len(nums)-1
        while start + 1 < end: 
            mid = (start + end)//2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
        if nums[end] == target:
            left = end
        if nums[start] == target:
            left = start
        return [left, right ]
