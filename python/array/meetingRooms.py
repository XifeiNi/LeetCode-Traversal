class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        prev = - 1
        for interval in sorted(intervals):
            if interval[0] < prev:
                return False
            prev = interval[1]
        return True
