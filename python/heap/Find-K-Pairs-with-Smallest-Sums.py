import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        heap = [[nums1[0] + nums2[0], 0, 0]]
        seen = {(0, 0)}
        result = []
        for i in range(min(k, len(nums1) * len(nums2))):
            _, id1, id2 = heapq.heappop(heap)
            result.append((nums1[id1], nums2[id2]))
            if id1 + 1 < len(nums1) and (id1 + 1, id2) not in seen:
                heapq.heappush(heap, [nums1[id1 + 1] + nums2[id2], id1 + 1, id2])
                seen.add((id1 + 1, id2))
            if id2 + 1 < len(nums2) and (id1, id2 + 1) not in seen:
                heapq.heappush(heap, [nums1[id1] + nums2[id2 + 1], id1, id2 + 1])
                seen.add((id1, id2 + 1))
        return result
    
