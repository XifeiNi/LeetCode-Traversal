class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        sortedA = sorted(A)
        sortedB = sorted(B)
        
        bMap = {b : [] for b in B}
        unUsed = []
        index = 0
        for a in sortedA:
            if a > sortedB[index]:
                bMap[sortedB[index]].append(a)
                index += 1
            else:
                unUsed.append(a)
        return [bMap[b].pop() if bMap[b] else unUsed.pop() for b in B]
        
