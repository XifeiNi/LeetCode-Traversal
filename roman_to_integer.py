ROMAN = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
class Solution:
    
    def romanToInt(self, s: str) -> int:
        if len(s) == 0:
            return 0
        sum = 0
        for i in range(len(s)):
            if i + 1 < len(s) and ROMAN[s[i]] < ROMAN[s[i+1]]:
                sum -= ROMAN[s[i]]
            else:
                sum += ROMAN[s[i]]
        return sum
        
