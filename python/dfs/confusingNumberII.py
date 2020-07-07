CONFUSING_MAP = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
class Solution:
    def confusingNumberII(self, N: int) -> int:
        ret = []
        for d in CONFUSING_MAP:
            if d != 0:
                self.dfs(d, CONFUSING_MAP[d], 10, ret, N)
        return len(ret)
    
    def dfs(self, original, rotate, digit, ret, N):
        print(original, rotate)
        if original != rotate:
            
            ret.append(original)
        for key in CONFUSING_MAP:
            print(original, digit, key)
            new_num = original * digit + key
            if new_num > N:
                return
            
            self.dfs(new_num, CONFUSING_MAP[key] * digit + rotate, digit * 10, ret, N)
        return
        
            
