from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        index = defaultdict(list)
        for i in range(len(S)):
            index[S[i]].append(i)
        cache = {}
        ret = 0
        for word in words:
            if word in cache:
                ret += 1
                continue
            if self.isSubsequence(index, word):
                ret += 1
                cache[word] = True
        return ret
    
    def isSubsequence(self, pos, word):  
        l = -1
        for c in word:
            index = bisect.bisect_left(pos[c], l + 1)
            if index == len(pos[c]):
                return False
            l = pos[c][index]
        return True
            
