class Solution:
    """
    @param x: The vertexes of the edges
    @param y: The vertexes of the edges
    @return: Return the index of barycentre
    """
    ansNode = 0
    ansSize = 0
    def dfs(self, x, f, n, dp, g):
        dp[x] = 1
        maxSubtree = 0
        for i in g[x]:
            if i == f:
                continue
            dp[x] += dp[i]
            self.dfs(i, x, n, dp, g)
            maxSubtree = max(maxSubtree, dp[i])
        maxSubtree = max(maxSubtree, n - maxSubtree)
        if ((maxSubtree < self.ansSize) or (maxSubtree == self.ansSize and x < self.ansNode)):
            self.ansNode, self.ansSize = x, maxSubtree
        
    def getBarycentre(self, x, y):
        # Write your code here
        g = [[] for i in range(len(x)+2)]
        dp = [0 for i in range(len(x)+2)]
        for i in range(len(x)):
            g[x[i]].append(y[i])
            g[y[i]].append(x[i])
        self.ansNode = 0
        self.ansSize = len(x)+2
        self.dfs(1,0,len(x),dp,g)
        return self.ansNode

