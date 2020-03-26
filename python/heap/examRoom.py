class ExamRoom:

    def __init__(self, N: int):
        self.numSeats = N
        self.heap = []
        self.availFirst = {}
        self.availLast = {}
        self.putSegment(0, self.numSeats - 1)

    def seat(self) -> int:
        while self.heap:
            _, first, last, valid = heapq.heappop(self.heap)
            if valid:
                del self.availFirst[first]
                del self.availLast[last]
                break
        if first == 0:
            if first != last:
                self.putSegment(first + 1, last)
            return 0
        elif last == self.numSeats - 1:
            if first != last:
                self.putSegment(first, last - 1)
            return last
        else:
            ret = first + (last - first) // 2
            if ret > first:
                self.putSegment(first, ret - 1)
            if ret < last:
                self.putSegment(ret + 1, last)
            return ret

    def leave(self, p: int) -> None:
        first, last, left, right = p, p, p - 1, p + 1
        if left >= 0 and left in self.availLast:
            segment_left = self.availLast.pop(left)
            segment_left[3] = False
            first = segment_left[1]

        if right < self.numSeats and right in self.availFirst:
            segment_right = self.availFirst.pop(right)
            segment_right[3] = False
            last = segment_right[2]

        self.putSegment(first, last)
    
    def putSegment(self, first, last):
        if first == 0 or last == self.numSeats - 1:
            priority = last - first
        else:
            priority = (last - first) // 2
        segment = [-priority, first, last, True]
        
        self.availFirst[first] = segment
        self.availLast[last] = segment
        
        heapq.heappush(self.heap, segment)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
