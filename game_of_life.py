DIRECTION=[(0,1),(1,0),(1,1),(-1,-1),(-1,0),(0,-1),(1,-1),(-1,1)]

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                self.getLiveNeighbors(board, i, j)
        
        self.calculateNextState(board)
        return board
    def getLiveNeighbors(self, board, i, j):
        m = len(board)
        n = len(board[0])
        ret = 0
        for deltaX, deltaY in DIRECTION:
            newX, newY = i + deltaX, j + deltaY
            if 0 <= newX < m and 0 <= newY < n and board[newX][newY] > 0:
                ret+=1
        if board[i][j] > 0:
            if ret > 3 or ret < 2:
                board[i][j] = 2 # about to die
        else:
            if ret == 3:
                board[i][j] = -1
    def calculateNextState(self, board):
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == -1:
                    board[i][j] = 1
