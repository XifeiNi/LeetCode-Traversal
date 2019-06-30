class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        row, column = len(matrix), len(matrix[0])
        i, j = row - 1, 0
        count = 0
        while i >= 0 and j < column:
            if matrix[i][j] == target:
                count+=1
                j+=1
                i-=1
            elif matrix[i][j] < target:
                j+=1
            else:
                i-=1
        return count
            
