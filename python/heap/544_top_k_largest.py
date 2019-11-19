import heapq
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        # write your code here
        heapq.heapify(nums)
        topK = heapq.nlargest(k, nums)
        topK.sort()
        topK.reverse()
        return topK
