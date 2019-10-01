class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        
        prefix_sum, ret = {0:1}, 0
        for i in range(len(nums)):
            if (nums[i] - k) in prefix_sum:
                ret += prefix_sum[nums[i] - k]
            if nums[i] not in prefix_sum:
                prefix_sum[nums[i]] = 1
            else:
                prefix_sum[nums[i]]+=1
        return ret
