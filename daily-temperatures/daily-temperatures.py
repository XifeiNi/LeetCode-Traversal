class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return [0]
        stack = []
        results = [0 for _ in range(len(temperatures))]
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                results[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return results