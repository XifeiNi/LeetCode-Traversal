from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_freq = defaultdict(int)
        for num in nums:
            num_to_freq[num] += 1
        num_sorted = sorted(num_to_freq.items(), key=lambda x: x[1], reverse=True)
        ret = []
        for i in range(k):
            ret.append(num_sorted[i][0])
        return ret
        
        
