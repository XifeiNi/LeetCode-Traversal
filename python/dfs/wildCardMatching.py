class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self._isMatch(s, 0, p, 0, {})
    def _isMatch(self, source, i, pattern, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        if len(source) == i:
            return self.isEmpty(j, pattern)
        if len(pattern) == j:
            return False
        if pattern[j] != '*':
            matched = self.equal(source[i], pattern[j]) and self._isMatch(source, i+1, pattern, j+1, memo)
        else:
            matched = self._isMatch(source, i + 1, pattern, j, memo) or self._isMatch(source, i, pattern, j+1, memo)
        memo[(i, j)] = matched
        return matched
        
    def isEmpty(self, j, pattern):
        for index in range(j, len(pattern)):
            if pattern[index] != '*':
                return False
        return True
    def equal(self, source, pattern):
        return source == pattern or pattern == '?'
