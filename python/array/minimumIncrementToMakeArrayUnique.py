from collections import defaultdict
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        ret = 0
        print(A)
        for i in range(1, len(A)):
            if A[i] == A[i - 1]:
                A[i] += 1
                ret += 1
            if A[i] < A[i - 1]:
                absolute = abs(A[i - 1] - A[i])
                A[i] = A[i] + absolute + 1
                ret = ret + absolute + 1
        return ret
                
