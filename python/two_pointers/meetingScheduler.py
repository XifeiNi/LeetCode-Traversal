class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        index1, index2 = 0, 0
        while index1 < len(slots1) and index2 < len(slots2):
            if len(self.intersect(slots1[index1], slots2[index2], duration)) > 0:
                return self.intersect(slots1[index1], slots2[index2], duration)
            if slots1[index1][1] > slots2[index2][1]:
                index2+=1
            else:
                index1+=1
        return []
        
    def intersect(self, slot1, slot2, duration):

        start = max(slot1[0], slot2[0])
        end = min(slot1[1], slot2[1])
        if end < start or end - start < duration:
            return []
        else:
            return [start, start + duration]
