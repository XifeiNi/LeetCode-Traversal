class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        answer = []
        self.dfs(s, [], answer)
        return answer
    def dfs(self, s, path, answer):
        if not s and len(path) == 4:
            answer.append('.'.join(path))
            return
        n = min(4, len(s)+1)
        for i in range(1, n):
            if int(s[:i]) <= 255:
                if i > 1 and s[0] == '0' or len(path) == 5:
                    break
                self.dfs(s[i:], path+[s[:i]], answer)
