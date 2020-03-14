from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mapS1 = self.getStringMap(s1)
        mapS2 = self.getStringMap(s2[0:len(s1)])
        for index, char in enumerate(s2):
            if self.cmp(mapS1, mapS2):
                return True
            mapS2[char] -= 1
            if index + len(s1) < len(s2):
                mapS2[s2[index + len(s1)]] += 1
            else:
                return False
        return False
        
    def getStringMap(self, string):
        ret = defaultdict(int)
        for char in string:
            ret[char] += 1
        return ret
    
    def cmp(self, map1, map2):
        for key in map1.keys():
            if map1[key] != map2[key]:
                return False
        for key in map2.keys():
            if map2[key] != map1[key]:
                return False
        return True
