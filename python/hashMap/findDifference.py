from collections import defaultdict
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sfreq = defaultdict(int)
        for char in s:
            sfreq[char] += 1
        for char in t:
            sfreq[char] -= 1
            if sfreq[char] < 0:
                return char
        return ''
            
