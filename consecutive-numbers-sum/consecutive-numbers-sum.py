class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        if n <= 0:
            return 0
        count, i = 0, 1
        while (i * (i + 1)) // 2 <= n:
            if ((n - (i * (i + 1)) // 2)) % i == 0:
                count += 1
            i += 1
        return count