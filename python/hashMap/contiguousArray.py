class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        diff = 0
        ans = 0
        num_hash = {}
        for i in range(len(nums)):
            if nums[i] == 1:
                diff +=1
            else:
                diff-=1
            if diff == 0:
                ans = i+1
            elif diff in num_hash:
                ans = max(ans, i - num_hash[diff])
            else:
                num_hash[diff] = i
        return ans
            
