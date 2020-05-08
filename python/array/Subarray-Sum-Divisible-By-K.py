from collections import defaultdict
class Solution:
    def subarraysDivByK(self, A: List[int], k: int) -> int:
        modToFreq = defaultdict(int)
        modToFreq[0] = 1
        cur_sum_mod, count = 0, 0
        for num in A:
            cur_sum_mod = (cur_sum_mod + num) % k 
            if cur_sum_mod < 0:
                cur_sum_mod += k
            count += modToFreq[cur_sum_mod]
            modToFreq[cur_sum_mod] += 1
        return count 
