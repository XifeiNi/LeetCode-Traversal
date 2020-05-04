class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        sweepLine = []
        for num, start, end in trips:
            sweepLine.append((start, num))
            sweepLine.append((end, -num))
        sweepLine.sort()
        passenger = 0
        for line in sweepLine:
            passenger += line[1]
            if passenger > capacity:
                return False
        return True
