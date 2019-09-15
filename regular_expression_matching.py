class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        return self._isMatch(0, 0, s, p, memo)
    
    def _isMatch(self, i, j,  string, pattern, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == len(string):
            return self.is_empty(pattern[j:])
        if j == len(pattern):
            return False
        if j + 1 < len(pattern) and pattern[j + 1] == '*':
            matched =  self._isMatch(i, j + 2, string, pattern, memo) or self._isMatch(i+1, j, string, pattern, memo) and self.isMatchedChar(string[i], pattern[j])
        else:
            matched = self.isMatchedChar(string[i], pattern[j]) and self._isMatch(i+1, j+1, string, pattern, memo)
        memo[(i, j)] = matched
        return matched
    def is_empty(self, pattern):
        if len(pattern) % 2 == 1:
            return False
        for i in range(len(pattern)//2):
            if pattern[i * 2 + 1] != '*':
                return False
        return True
        
    def isMatchedChar(self, s, p):
        return s == p or p == '.'
