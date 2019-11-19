class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ret = []
        if not matrix or len(matrix) == 0:
            return []
        up = False
        for dimeter in range(len(matrix) + len(matrix[0]) - 1):
            up = not up
            if up:
                for c in range(max(0, dimeter - len(matrix) + 1), min(dimeter, len(matrix[0]) - 1) + 1):
                    right = dimeter - c
                    ret.append(matrix[right][c])
            else:
                for right in range(max(0, dimeter - len(matrix[0]) + 1), min(dimeter, len(matrix) - 1) + 1):
                    c = dimeter - right
                    ret.append(matrix[right][c])
        return ret
                    
        
