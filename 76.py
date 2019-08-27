from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        targetMap = self.getTargetMap(t)
        matchedUniqueChar = 0
        sourcedMap = defaultdict(int)
        targetUniqueChar = len(targetMap)
        minLength = len(s) + 1
        minimumWindow = ""
        j = 0
        for i in range(len(s)):
            while j < len(s) and matchedUniqueChar < targetUniqueChar:
                if s[j] in targetMap:
                    sourcedMap[s[j]] += 1
                if s[j] in targetMap and targetMap[s[j]] == sourcedMap[s[j]]:
                    matchedUniqueChar+=1
                j+=1

            if j - i < minLength and matchedUniqueChar == targetUniqueChar:
                minLength = j - i
                minimumWindow = s[i:j]
            if s[i] in targetMap:
                if targetMap[s[i]] == sourcedMap[s[i]]:
                    matchedUniqueChar-=1
                sourcedMap[s[i]]-=1
            
        return minimumWindow
        
    
    def getTargetMap(self, t):
        targetMap = {}
        for char in t:
            if char not in targetMap:
                targetMap[char] = 1
            else:
                targetMap[char]+=1
        return targetMap
