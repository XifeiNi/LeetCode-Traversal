class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        res, upper, digit, lower = 0, 1, 1, 1
        v = [0 for _ in range(len(s))]
        
        i = 0
        while i < len(s):
            if 'A' <= s[i] <= 'Z':
                upper = 0
            if 'a' <= s[i] <= 'z':
                lower = 0
            if '0' <= s[i] <= '9':
                digit = 0
            j = i
            while i < len(s) and s[i] == s[j]:
                i += 1
            v[j] = i - j
        missing = upper + digit + lower
        if len(s) < 6:
            return 6 - len(s) + max(0, missing - 6 + len(s))
        else:
            over = max(len(s) - 20, 0)
            print(over)
            res += over
            print(v)
            for k in range(1,3):	
                for i in range(len(s)) :
                    if over <= 0:
                        break
                    if v[i] < 3 or v[i] % 3 != (k - 1) :	
                        continue
                    if over - k < 0:
                        v[i] = v[i] - k + over
                        over = 0
                        
                    else:
                        v[i] -= k
                        over -=k
            left = 0
            for i in range(len(s)):
            
                if v[i] >= 3 and over > 0:
                    need = v[i] - 2
                    v[i] -= over
                    over -= need
                if v[i] >= 3:
                    left += v[i] // 3
            res += max(missing, left)
            return res
            
        
                
