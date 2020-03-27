class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        if not self.checkNum(board):
            return False
        
        return self.checkCol(board) and self.checkRow(board) and self.checkDiagonal(board)
        
    
    def checkNum(self, board):
        numX, num0 = 0, 0
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == 'X':
                    numX += 1
                if board[i][j] == 'O':
                    num0 += 1
        self.numX = numX
        self.num0 = num0
        if not (numX == num0 + 1 or numX == num0):
            return False
        else:
            return True
    def checkCol(self, board):
        for j in range(0, 3):
            if board[0][j] == board[1][j] == board[2][j]:
                if board[0][j] == 'X':
                    return self.numX == self.num0 + 1
                elif  board[0][j] == 'O':
                    return self.numX == self.num0
        return True
    def checkRow(self, board):
        for i in range(0, 3):
            if board[i][0] == board[i][1] == board[i][2]:
                if board[i][0] == 'X':
                    return self.numX == self.num0 + 1
                elif  board[i][0] == 'O':
                    return self.numX == self.num0
        return True
    def checkDiagonal(self, board):
        if board[0][0] == board[1][1] == board[2][2]:
            if board[0][0] == 'X':
                return self.numX == self.num0 + 1
            if board[0][0] == 'O':
                return self.numX == self.num0
        if board[0][2] == board[1][1] == board[2][0]:
            if board[2][0] == 'X':
                return self.numX == self.num0 + 1
            if board[2][0] == 'O':
                return self.numX == self.num0
        return True
                    
        
