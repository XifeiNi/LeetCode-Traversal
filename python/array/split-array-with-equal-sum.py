class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        sumArray = [0] * len(nums)
        sumArray[0] = nums[0]
        for i in range(1, len(nums)):
            sumArray[i] = sumArray[i - 1] + nums[i]
        n = len(nums)
        for i in range(3, n - 3):
            numSet = set()
            for j in range(1, i - 1):
                if (sumArray[j - 1] == sumArray[i - 1] - sumArray[j]):
                    numSet.add(sumArray[j - 1])
            for k in range(i + 2, n - 1):
                x , y = sumArray[k - 1] - sumArray[i], sumArray[n - 1] - sumArray[k]
                if x == y and x in numSet:
                    return True
        return False
