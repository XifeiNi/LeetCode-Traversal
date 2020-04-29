class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        subFreq = {}
        for i in range(len(s) - minSize + 1):
            for j in range(minSize, maxSize + 1):
                if i + j > len(s):
                    break
                word = s[i:i + j]
                if word in subFreq:
                    subFreq[word] += 1
                else:
                    count = collections.Counter(word)
                    if len(count) <= maxLetters:
                        subFreq[word] = 1
        return max(subFreq.values()) if subFreq else 0
