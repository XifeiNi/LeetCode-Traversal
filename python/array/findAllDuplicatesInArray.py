class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ret = []
        for i in range(len(nums)):
            index = nums[i]
            if index < 0:
                index = -index
            if nums[index - 1] < 0:
                ret.append(index)
            else:
                nums[index - 1] = -nums[index - 1]
        return ret
