class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        self.dfs(n, k, 1, [], results)
        return results
    
    def dfs(self, n, k, start, toBeAppend, results):
        if len(toBeAppend) == k:
            
            results.append(list(toBeAppend))
            return
        
        for i in range(start, n + 1):
            toBeAppend.append(i)
            self.dfs(n, k, i + 1, toBeAppend, results)
            toBeAppend.pop()
        
