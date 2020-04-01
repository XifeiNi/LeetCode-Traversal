class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dict={}
        
        for x in nums:
            dict[x] = 1
            
        ans = 0
        
        for x in nums:
            if x in dict:
                len = 1
                del dict[x]
                l = x - 1
                r = x + 1
                while l in dict:
                    del dict[l]
                    l -= 1 
                    len += 1
                while r in dict:
                    del dict[r]
                    r += 1
                    len += 1
                if ans < len:
                    ans = len
                    
        return ans
