class Solution:
    def countArrangement(self, N: int) -> int:
        nums = tuple([i+1 for i in range(N)]) # because tuple can be hashable
        memory = {} # key is nums left, value is the number of beautiful arrangment
        return self.dfs(nums,memory,N)
        
    def dfs(self,nums,memory,pos):
        if pos == 1:
            return 1
        if nums in memory:
            return memory[nums]
        res = 0
        for i in range(len(nums)):
            if nums[i] % pos ==0 or pos % nums[i] == 0:
                res += self.dfs(nums[:i]+nums[i+1:],memory,pos-1)
        memory[nums] = res
        return res
