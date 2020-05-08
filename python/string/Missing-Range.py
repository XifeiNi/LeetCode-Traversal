class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if len(nums) == 0:
            return [self.getRange(lower, upper)]
        prev = lower - 1
        ret = []
        for i in range(len(nums)):
            if prev != nums[i] and prev + 1 != nums[i]:
                ret.append(self.getRange(prev + 1, nums[i] - 1))
            prev = nums[i]
        if nums[-1] < upper:
            ret.append(self.getRange(nums[-1] + 1, upper))
        return ret
    def getRange(self, left, right):
        if left == right:
            return str(left)
        else:
            return str(left) + "->" + str(right)
