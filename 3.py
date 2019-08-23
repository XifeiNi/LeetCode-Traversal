class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        j = 0
        uniqueChars = set([])
        for i in range(len(s)):
            
            while j < len(s) and s[j] not in uniqueChars:
                uniqueChars.add(s[j])
                j += 1
            longest = max(longest, j -i)
            uniqueChars.remove(s[i])
        return longest
        
