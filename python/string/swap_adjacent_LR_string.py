class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        l = 0
        r = 0
        for i in range(len(start)):
            if start[i] == 'R':
                r += 1
            if end[i] == "L":
                l += 1
            if start[i] == 'L':
                l -= 1
            if end[i] == 'R':
                r -= 1
            if (l < 0 or r != 0) and (l != 0 or r < 0):
                return False
        if l == 0 and r == 0:
            return True
        else:
            return False
