class Solution:
    def partition(self, s: str) -> List[List[str]]:
        results = []
        self.dfs(results, s, [])
        return results
    
    def dfs(self, results, string, stringList):
        if len(string) == 0:
            results.append(list(stringList))
            return
        for i in range(1, len(string) + 1):
            prefix = string[:i]
            if self.isPal(prefix):
                stringList.append(prefix)
                self.dfs(results, string[i:], stringList)
                stringList.pop()
    
    def isPal(self, string):
        return string == string[::-1]
