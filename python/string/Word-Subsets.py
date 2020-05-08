import collections
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        letter_required = {}
        
        for word in B:
            count = collections.Counter(word)
            for char in count:
                if char not in letter_required or count[char] > letter_required[char]:
                    letter_required[char] = count[char]
        ret = []
        for word in A:
            count = collections.Counter(word)
            if self.isSubset(count, letter_required):
                ret.append(word)
        return ret
    def isSubset(self, map1, map2):
        for char in map2:
            if map1[char] < map2[char]:
                return False
        return True
