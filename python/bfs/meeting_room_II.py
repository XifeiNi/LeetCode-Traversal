class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        points = []
        for interval in intervals:
            points.append((interval[0], 1))
            points.append((interval[1], -1))
        rooms = 0
        current = 0
        for time, delta in sorted(points):
            current += delta
            rooms = max(rooms, current)
        return rooms
    
