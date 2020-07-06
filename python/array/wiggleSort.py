class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        start = 0
        while start < len(nums) - 2:
            nums[start + 1], nums[start + 2] = nums[start + 2], nums[start + 1]
            start += 2
            
