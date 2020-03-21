class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        if X > Y:
            return X - Y
        else:
            res = 0
            while X < Y:
                if Y % 2 == 1:
                    Y += 1
                    res += 1
                Y //= 2
                res += 1
            return res + X - Y
