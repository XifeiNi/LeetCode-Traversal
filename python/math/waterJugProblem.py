class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z == 0:
            return True
        if z > x + y:
            return False
        return z % self.gcd(x,y) == 0
    def gcd(self, x, y):
        if y == 0:
            return x
        return self.gcd(y, x % y)
