class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 0:
            return 0
        count = 0
        for i in range(1, int(math.sqrt(N*2)) + 1):
            if (N - (i + 1)*i/2)%i == 0:
                count += 1
        return count
