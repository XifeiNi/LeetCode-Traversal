class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n <= 2:
            return n
        results = [1, 2]
        for i in range(2, n):
            results.append(results[i-1]+results[i-2])
        return results[-1]
