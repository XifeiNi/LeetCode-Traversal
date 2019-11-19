class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        results, i = [], 0
        while i < len(nums):
            j = i+1
            while j < len(nums) and (nums[j] - nums[j-1]) == 1:
                j+=1
            if j - i > 1:
                results.append(str(nums[i]) + '->' + str(nums[j-1]))
            else:
                results.append(str(nums[i]))
            i = j
        return results
                
    
