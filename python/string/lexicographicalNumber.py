class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        cur, ret = 1, []
        for i in range(1, n + 1):
            ret.append(cur)
            if cur * 10 <= n:
                cur = cur * 10
            elif cur % 10 != 9 and cur + 1 <= n:
                cur += 1
            else:
                while (cur // 10) % 10 == 9:
                    cur = cur // 10
                cur = cur // 10 + 1
        return ret
