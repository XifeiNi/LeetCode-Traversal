class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        results = []
        self.dfs(s, [], results)
        return results
    def dfs(self, s, path, results):
        if s == "":
            results.append(path[:])
            return
        for i in range(2):
            if i + 1 <= len(s):
                path.append(s[:i+1])
                self.dfs(s[i+1:], path, results)
                path.pop()
