class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        MAX = 10000
        ans = [MAX for _ in range(amount + 1)]
        ans[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    ans[i] = min(ans[i], ans[i - coin] + 1)
        if ans[amount] == MAX:
            return -1
        return ans[amount]
        
