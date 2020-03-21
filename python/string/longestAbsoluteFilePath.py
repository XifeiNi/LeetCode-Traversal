class Solution:
    def lengthLongestPath(self, input: str) -> int:
        if not input:
            return 0
        ans = 0
        levelSum = [0 for _ in range(len(input))]
        for string in input.split("\n"):
            level = string.count("\t")
            if "." in string:
                length = len(string.strip("\t"))
                ans = max(ans, length + levelSum[level - 1])
            else:
                length = len(string.strip("\t")) + 1
                if level > 0:
                    levelSum[level] = length + levelSum[level - 1]
                else:
                    levelSum[level] = length
        return ans
