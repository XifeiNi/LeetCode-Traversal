class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxHeap, minHeap = [], []
        ret = start = 0
        for index, num in enumerate(nums):
            heapq.heappush(maxHeap, (-num, index))
            heapq.heappush(minHeap, (num, index))
            while -maxHeap[0][0] - minHeap[0][0] > limit:
                start = min(maxHeap[0][1], minHeap[0][1]) + 1
                while maxHeap[0][1] < start: 
                    heapq.heappop(maxHeap)
                while minHeap[0][1] < start:
                    heapq.heappop(minHeap)
            ret = max(ret, index - start + 1)
        return ret
