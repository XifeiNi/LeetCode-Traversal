class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        ret = [0 for _ in range(len(nums))]
        start, end = 0, len(nums) - 1
        if a >= 0:
            count = end
        else:
            count = start
        while start  <= end:
            startNum = a * nums[start] * nums[start] + b * nums[start] + c
            endNum = a * nums[end] * nums[end] + b * nums[end] + c

            if a >= 0:
                if startNum > endNum:
                    ret[count] = startNum
                    count -= 1
                    start += 1
                else:
                    ret[count] = endNum
                    count -= 1
                    end -= 1
            else:
                
                if startNum > endNum:
                    ret[count] = endNum
                    count += 1
                    end -= 1
                else:
                    ret[count] = startNum
                    count += 1
                    start += 1
        return ret
                    
