DIRECTIONS = [(1,0),(0,1),(-1,0),(0,-1),(-1,-1),(1,1),(1,-1),(-1,1)]
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board or len(board) == 0:
            return board
        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        self.dfs(x, y, board)
        return board
    
    def dfs(self, x, y, board):
        mines = self.getMines(x, y, board)
        if mines > 0:
            board[x][y] = str(mines)
        else:
            board[x][y] = 'B'
            for deltaX, deltaY in DIRECTIONS:
                newX, newY = x + deltaX, y + deltaY
                if 0 <= newX < len(board) and 0 <= newY < len(board[0]) and board[newX][newY] == 'E':
                    self.dfs(newX, newY, board)

    
    def getMines(self, x, y, board):
        mine = 0
        for deltaX, deltaY in DIRECTIONS:
            newX, newY = x + deltaX, y + deltaY
            if 0 <= newX < len(board) and 0 <= newY < len(board[0]):
                if board[newX][newY] == 'M':
                    mine += 1
        return mine
