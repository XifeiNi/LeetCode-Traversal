class Solution:
    """
    @param A: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def totalOccurrence(self, A, target):
        # write your code here
        if len(A) == 0:
            return 0
        
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end)//2
            if A[mid] < target:
                start = mid
            else:
                end = mid
        if A[start] == target:
            leftBound = start
        elif A[end] == target:
            leftBound = end
        else:
            return 0
            
        start, end = 0, len(A) -1
        while start + 1 < end:
            mid = (start + end)//2
            if A[mid] <= target:
                start = mid
            else:
                end = mid
        if A[end] == target:
            rightBound = end
        else:
            rightBound = start
        return rightBound - leftBound + 1
