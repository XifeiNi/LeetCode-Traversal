from collections import defaultdict
import sys
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        charFreqA = defaultdict(int)
        charFreqB = defaultdict(int)
        charSameAB = defaultdict(int)
        for i in range(len(A)):
            if A[i] == B[i]:
                charSameAB[A[i]]+=1
            charFreqA[A[i]]+=1
            charFreqB[B[i]]+=1
        allKeys = list(charFreqA.keys()) + (list(charFreqB.keys()))
        flip = sys.maxsize
        for key in allKeys:
            if charFreqA[key] + charFreqB[key] - charSameAB[key] == len(A):
                flip = min([charFreqA[key] - charSameAB[key], charFreqB[key] - charSameAB[key], flip])
        if flip == sys.maxsize:
            return -1
        else:
            return flip
            
            
