class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        stack, res = [], [-1 for _ in range(len(nums))]
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                pop_index = stack.pop()
                res[pop_index] = nums[i]
            stack.append(i)
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                pop_index = stack.pop()
                res[pop_index] = nums[i]
            stack.append(i)
        return res
                
