class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            while 0 < nums[i] <= len(nums) and nums[i] != i+1 and nums[nums[i] - 1] != nums[i]:
                j = nums[i] - 1
                nums[i], nums[j]  = nums[j], nums[i]
            i+=1
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        return len(nums) + 1
