from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        start, end = 0, 10
        freq = defaultdict(int)
        while end <= len(s):
            freq[s[start:end]] += 1
            start += 1
            end += 1
        ret = []
        for key in freq:
            if freq[key] > 1:
                ret.append(key)
        return ret
            
