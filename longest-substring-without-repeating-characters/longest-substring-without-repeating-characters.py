class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end, longest, slidingWindow = 0, 0, 0, collections.defaultdict(int)
        while start < len(s):
            while end < len(s) and slidingWindow[s[end]] == 0:
                slidingWindow[s[end]] += 1
                end += 1
            longest = max(longest, end - start)
            slidingWindow[s[start]] -= 1
            start += 1
        return longest