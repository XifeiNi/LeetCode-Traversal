class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        boards = []
        self.dfs(n, [], boards)
        return boards
    def dfs(self, n, permutation, boards):
        if n == len(permutation):
            boards.append(self.draw(permutation))
            return
        
        row_index = len(permutation)
        for col_index in range(n):
            if not self.is_valid(permutation, col_index):
                continue
            permutation.append(col_index)
            self.dfs(n, permutation, boards)
            permutation.pop()
        
    def draw(self, permutation):
        board = []
        for col in permutation:
            row_string = ''.join(['Q' if c == col else '.' for c in range(len(permutation))])
            board.append(row_string)
        return board
        
    def is_valid(self, permutation, col):
        row = len(permutation)
        for r, c in enumerate(permutation):
            if c == col:
                return False
            if r + c == col + row:
                return False
            if r - c == row - col:
                return False
        return True
    
        
