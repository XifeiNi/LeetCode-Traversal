class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        arr = [1]
        while len(arr) < N:
            arr = [2 * i - 1 for i in arr] + [2 * i for i in arr]
        return [i for i in arr if i <= N]
            
