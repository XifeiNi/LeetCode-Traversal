from collections import defaultdict
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        mostLeft = defaultdict(int)
        for i, char in enumerate(S):
            mostLeft[char] = i
        ans = []
        right, left = 0, 0
        for i in range(len(S)):
            right = max(right, mostLeft[S[i]])
            if i == right:
                ans.append(i - left + 1)
                left = i + 1
        return ans
