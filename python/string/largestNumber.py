from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(key=cmp_to_key(lambda x, y: 1 if str(x)+str(y) < str(y)+str(x) else -1))
        if nums[0] == 0:
            return "0"
        return ''.join(map(str, nums))
