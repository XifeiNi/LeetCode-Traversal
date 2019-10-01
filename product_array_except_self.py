class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = [1 for _ in range(len(nums))], [1 for _ in range(len(nums))]
        product = 1
        for i in range(len(nums)):
            product = product*nums[i]
            left[i] = product
        product = 1
        for i in range(len(nums)-1, -1, -1):
            product = product*nums[i]
            right[i] = product
        result = [0 for _ in range(len(nums))]
        if left[0] != 0:
            result[0] = right[0]//left[0]
        else:
            result[0] = right[0]
        if right[len(nums) -1] == 0:
            result[len(nums)-1] = left[len(nums) -2]
        else:
            result[len(nums)-1] = left[len(nums) -1]//right[len(nums) -1]
        for i in range(1, len(nums) - 1):
            result[i] = left[i-1]*right[i+1]
        return result
        
