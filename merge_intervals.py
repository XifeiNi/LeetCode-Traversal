class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        answer = []
        for i in range(len(intervals)):
            self.push_back(answer, intervals[i])
        return answer
    def push_back(self, answer, interval):
        if len(answer) == 0:
            answer.append(interval)
            return
        if len(answer) > 0 and answer[-1][1] >= interval[0]:
            answer[-1][1] = max(interval[1], answer[-1][1])
        else:
            answer.append(interval)
