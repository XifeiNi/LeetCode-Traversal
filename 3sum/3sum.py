class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        if not nums or len(nums) < 3:
            return results
        
        nums.sort()
        
        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i -  1]:
                continue
            left, right = i + 1, len(nums) - 1
            target = -nums[i]
            self.twoSum(nums, left, right, target, results)
        return results
    def twoSum(self, nums, left, right, target, results):
        lastPair = None
        while left < right:
            if nums[left] + nums[right] == target:
                if (nums[left], nums[right]) != lastPair:
                    results.append([-target, nums[left], nums[right]])
                lastPair = (nums[left], nums[right])
                left += 1
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
                
            
        