class Solution:

    def __init__(self, w: List[int]):
        self.weight = w
        for i in range(1, len(w)):
            self.weight[i] = self.weight[i - 1] + self.weight[i]

    def pickIndex(self) -> int:
        target = random.randint(1, self.weight[-1])
        start, end = 0, len(self.weight)
        while start + 1 < end:
            mid = start + (end - start)//2
            if self.weight[mid] < target:
                start = mid
            elif self.weight[mid] > target:
                end = mid
            else:
                return mid
        if self.weight[start] >= target:
            return start
        return end
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()