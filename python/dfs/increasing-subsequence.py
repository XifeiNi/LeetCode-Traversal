class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ret = []
        self.dfs(ret, 0, [], nums)
        return ret
    
    def dfs(self, ret, index, current, nums):
        if len(nums) >= index and len(current) >= 2:
            ret.append(current[:])
        used = set()
        for i in range(index, len(nums)):
            if len(current) > 0 and current[-1] > nums[i]:
                continue
            if nums[i] in used:
                continue
            current.append(nums[i])
            used.add(nums[i])
            self.dfs(ret, i + 1, current, nums)
            current.pop()

