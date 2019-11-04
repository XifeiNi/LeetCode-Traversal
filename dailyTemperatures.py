class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        if not T:
            return [0]
        results = [0 for _ in range(len(T))]
        stack = []
        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                results[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return results
