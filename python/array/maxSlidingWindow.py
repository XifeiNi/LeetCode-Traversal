class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue, output = deque([]), []
        for i in range(len(nums)):
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            if i + 1 >= k:
                output.append(nums[queue[0]])
            if i + 1 - k == queue[0]:
                queue.popleft()
        return output
