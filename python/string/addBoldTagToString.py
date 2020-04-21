class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        tag = [False for _ in range(len(s))]
        
        for i in range(len(s)):
            block = s[i:]
            for word in dict:
                if block.startswith(word):
                    tag[i:i + len(word)] = [True] * len(word)
        ans = []
        for i in range(len(s)):
            if tag[i] and (i == 0 or not tag[i - 1]):
                ans.append('<b>')
            ans.append(s[i])
            if tag[i] and (i == len(s) - 1 or not tag[i + 1]):
                ans.append('</b>')
        return ''.join(ans)
