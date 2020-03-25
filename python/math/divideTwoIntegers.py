class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative = False
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            negative = True
        ans, count, abDividend, abDivisor = 0, 1, abs(dividend), abs(divisor)
        while abDividend >= abDivisor:
            abDivisor = abDivisor << 1
            
            if abDividend >= abDivisor:
                count = count << 1
            
            else:
                abDivisor = abDivisor >> 1
                abDividend = abDividend - abDivisor
                abDivisor = abs(divisor)
                ans += count
                count = 1
        if negative:
            ans = -ans
        if ans > 2147483647:
            return 2147483647
        return ans
