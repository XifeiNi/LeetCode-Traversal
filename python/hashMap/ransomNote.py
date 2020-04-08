from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineCharFreq = defaultdict(int)
        for char in magazine:
            magazineCharFreq[char] += 1
        for char in ransomNote:
            magazineCharFreq[char] -= 1
            if magazineCharFreq[char] < 0:
                return False
        return True
            
