class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) == 0:
            return ""
        for i in range(len(s) - 1, -1, -1):
            substr = s[:i + 1]
            if substr == substr[::-1]:
                if i == len(s) - 1:
                    return s
                else:
                    return s[i+1:][::-1] + s
