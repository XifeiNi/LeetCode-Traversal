class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        results = [0 for _ in range(length)]
        operations = results + [0]
        
        for start, end, increment in updates:
            operations[start] += increment
            operations[end + 1] -= increment
        
        results[0] = operations[0]
        for index in range(1, length):
            results[index] = results[index - 1] + operations[index]
        return results
