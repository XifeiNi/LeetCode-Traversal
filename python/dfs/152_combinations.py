class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # write your code here
        self.res = []
        tmp = []
        self.dfs(n, k, 1, 0, tmp)
        return self.res
    def dfs(self, n, k, m, p, tmp):
        if k==p:
            self.res.append(tmp[:])
            return
        for i in range(m, n+1):
            tmp.append(i)
            self.dfs(n,k,i+1,p+1,tmp)
            tmp.pop()
