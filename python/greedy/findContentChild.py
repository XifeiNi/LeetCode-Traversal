class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        
        cookie, children, ans = 0, 0, 0
        while cookie < len(s) and children < len(g):
            if s[cookie] >= g[children]:
                cookie += 1
                children += 1
                ans += 1
            else:
                cookie += 1
        return ans
