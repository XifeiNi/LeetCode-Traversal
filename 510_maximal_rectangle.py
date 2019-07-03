class Solution:
    """
    @param matrix: a boolean 2D matrix
    @return: an integer
    """
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        max_rectangle = 0
        heights = [0] * len(matrix[0])
        for row in matrix:
            for index, num in enumerate(row):
                heights[index] = heights[index] + 1 if num else 0
            max_rectangle = max(max_rectangle, self.findMaxRectangle(heights))
        return max_rectangle
    def findMaxRectangle(self, heights):
        indices_stack = []
        max_rectangle = 0
        for index, height in enumerate(heights + [-1]):
            while indices_stack and heights[indices_stack[-1]] >= height:
                popped = indices_stack.pop(-1)
                left_bound = indices_stack[-1] if indices_stack else -1
                max_rectangle = max(max_rectangle, (index - left_bound - 1)*heights[popped])
            indices_stack.append(index)
        return max_rectangle
                
