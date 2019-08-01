class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        i, j = 0, 0
        results = []
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                results.append(A[i])
                i+=1
            else:
                results.append(B[j])
                j+=1
        while i < len(A):
            results.append(A[i])
            i+=1
        while j < len(B):
            results.append(B[j])
            j+=1
        return results
            

