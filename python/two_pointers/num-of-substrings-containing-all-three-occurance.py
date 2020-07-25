class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        start, end = 0, 0
        ret = 0
        slidingMap = {'a': 0, 'b' : 0, 'c' : 0}
        while end < len(s):
            slidingMap[s[end]] += 1
            while slidingMap['a'] and slidingMap['b'] and slidingMap['c']:
                slidingMap[s[start]] -= 1
                start += 1
            ret += start
            end += 1
        return ret
