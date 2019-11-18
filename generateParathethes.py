class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        results = []
        self.dfs(n, n, "", results)
        return results
    
    def dfs(self, left, right, item, results):
        if left == 0 and right == 0:
            results.append(item)
            return
        if right < left:
            return
        if left > 0:
            self.dfs(left - 1, right, item + '(', results)
        if right > 0:
            self.dfs(left, right - 1, item + ')', results)
