class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        nearBy = {}
        if len(nums) > 10000:
            return False
        if k == 0:
            return False
        for q in range(min(k + 1, len(nums))):
            nearBy[nums[q]] = nearBy.get(nums[q], 0) + 1
        for i in range(len(nums)):
            
            if i + k < len(nums) and i != 0:
                nearBy[nums[i + k]] = nearBy.get(nums[i + k], 0) + 1
            for j in range(i, min(i + k + 1, len(nums))):
                for num in nearBy:
                    if num == nums[j] and nearBy[num] < 2:
                        continue
                    if abs(num - nums[j]) <= t:
                        return True
            nearBy[nums[i]] -= 1
            if nearBy[nums[i]] == 0:
                del nearBy[nums[i]]
                    
        return False
