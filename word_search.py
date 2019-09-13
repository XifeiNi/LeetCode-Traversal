class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word or len(word) == 0:
            return False
        if len(word) > len(board)*len(board[0]):
            return False
        visited = [[False for i in range(len(board[0]))] for j in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.dfs(board, word, 0, visited, i, j):
                    return True
        return False
    def dfs(self, board, word, start, visited, row, column):
        if start == len(word):
            return True
        if row < 0 or column < 0 or row >= len(board) or column >= len(board[0]):
            return False
        if board[row][column] == word[start] and not visited[row][column]:
            print(word[start])
            visited[row][column] = True
            if self.dfs(board, word, start + 1, visited, row, column + 1) or self.dfs(board, word, start + 1, visited, row + 1, column) or self.dfs(board, word, start + 1, visited, row, column - 1) or self.dfs(board, word, start + 1, visited, row - 1, column):
                return True
            else:
                visited[row][column] = False
        return False
        
