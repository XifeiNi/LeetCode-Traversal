class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total = 0
        high, low = 0, sys.maxint
        for i in range(len(prices)):
            if prices[i] - low > total:
                total = prices[i] - low
            low = min(prices[i], low)
        return total
        
