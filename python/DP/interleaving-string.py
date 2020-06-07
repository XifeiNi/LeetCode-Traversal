class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if s1 == None or s2 == None or s3 == None:
            return False
        if len(s1) + len(s2) != len(s3):
            return False
        interleave = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        interleave[0][0] = True
        
        for i in range(len(s1)):
            interleave[i + 1][0] = s1[:i+1] == s3[:i+1]
        for i in range(len(s2)):
            interleave[0][i + 1] = s2[:i + 1] == s3[:i + 1]
        for i in range(len(s1)):
            for j in range(len(s2)):
                interleave[i + 1][j + 1] = False
                if s1[i] == s3[i + j + 1]:
                    interleave[i + 1][j + 1] = interleave[i][j + 1]
                if s2[j] == s3[i + j + 1]:
                    interleave[i + 1][j + 1] |= interleave[i + 1][j]
        return interleave[len(s1)][len(s2)]
