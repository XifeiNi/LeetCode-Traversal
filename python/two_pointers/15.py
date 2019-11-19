class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        for i in range(len(nums)-1):

            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.findTwoSum(i+1, len(nums)-1, nums, -nums[i], results)
        return results
    def findTwoSum(self, left, right, nums, target, results):
        while left < right:
            if nums[left] + nums[right] == target:
                results.append([-target, nums[left], nums[right]])
                left+=1
                right-=1
                while left > 0 and left < right and nums[left] == nums[left-1]:
                    left+=1
                while right < len(nums) - 1 and left < right and nums[right] == nums[right + 1]:
                    right-=1
            elif nums[left] + nums[right] < target:
                left+=1
            else:
                right-=1
        
            
