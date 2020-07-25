class Solution:
    def knightDialer(self, N: int) -> int:
        neighbors = {
            0: (4, 6),
            1: (6, 8),
            2: (7, 9),
            3: (4, 8),
            4: (0, 3, 9),
            5: (), 
            6: (0, 1, 7),
            7: (2, 6),
            8: (1, 3),
            9: (2, 4)
        }
        
        currCount = [1] * 10
        for _ in range(N - 1):
            nextCount = [0] * 10
            for src in range(len(currCount)):
                for dst in neighbors[src]:
                    nextCount[dst] = (nextCount[dst] + currCount[src]) %  (10**9 + 7)
            currCount = nextCount
        return sum(currCount) %  (10**9 + 7) 
