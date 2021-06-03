class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0 : 1}
        currentSum, result = 0, 0
        for num in nums:
            currentSum += num
            result += prefixSum.get(currentSum - k, 0)
            prefixSum[currentSum] = prefixSum.get(currentSum, 0) + 1
        return result