class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        up, left, down, right = 0, 0, len(matrix) - 1, len(matrix[0]) - 1
        results = []
        while left <= right and up <= down:
            for i in range(left, right+1):
                results.append(matrix[up][i])
            up+=1
            for i in range(up, down+1):
                results.append(matrix[i][right])
            right-=1
            if up <= down:
                for i in range(right, left-1, -1):
                    results.append(matrix[down][i])
                down-=1
            if left <= right:
                for i in range(down, up-1, -1):
                    results.append(matrix[i][left])
                left +=1
        
        return results
            
