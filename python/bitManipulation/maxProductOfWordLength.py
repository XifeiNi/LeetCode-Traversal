class Solution:
    def maxProduct(self, words: List[str]) -> int:
        sets = [0 for _ in range(len(words))]
        ret = 0
        for i in range(len(words)):
            for char in words[i]:
                sets[i] |= 1 << ord(char) - ord('a')
        
        for i in range(len(words)):
            for j in range(len(words)):
                if sets[i] & sets[j] == 0:
                    ret = max(ret, len(words[i]) * len(words[j]))
        return ret
