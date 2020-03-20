class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0 for _ in range(n)]
        stack = []
        last_time = 0
        for string in logs:
            log = string.split(':')
            id, status, time = int(log[0]), log[1], int(log[2])
            if status == "start":
                if stack:
                    result[stack[-1]] += time - last_time
                stack.append(id)
            else:
                time += 1
                result[stack.pop()] += time - last_time
            last_time = time
        return result
