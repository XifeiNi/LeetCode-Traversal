class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.board = [['E' for _ in range(n)] for _ in range(n)]
        self.winning = n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.makeMove(row, col, player)
        #print(self.board)
        winning = self.winningMark(player)
        if self.isHorizontalWin(row, col, winning) or self.isVerticalWin(row, col, winning) or self.isDiagonalWin(row, col, winning):
            return player
        else:
            return 0
        
    def makeMove(self, row, col, player):
        if player == 1:
            self.board[row][col] = 'X'
        else:
            self.board[row][col] = 'O'
    def winningMark(self, player):
        if player == 1:
            return 'X'
        else:
            return 'O'
    def isVerticalWin(self, row, col, winningMark):
        left = 0
        starting_row = row 
        while starting_row < self.winning and self.board[starting_row][col] == winningMark:
            starting_row += 1
            left += 1
        right = 0
        starting_row = row
    
        while starting_row >= 0 and self.board[starting_row][col] == winningMark:
            starting_row -= 1
            right += 1
        #print(left, right)
        if left + right - 1  >= self.winning:
            return True
        else:
            return False
    def isHorizontalWin(self, row, col, winningMark):
        left = 0
        starting_col = col 
        while starting_col < self.winning and self.board[row][starting_col] == winningMark:
            #print( self.board[row][starting_col])
            starting_col += 1
            left += 1
        right = 0
        starting_col = col
        while starting_col >= 0 and self.board[row][starting_col] == winningMark:
            #print( self.board[row][starting_col])
            starting_col -= 1
            right += 1
        #print(left, right)
        if left + right - 1  >= self.winning:
            return True
        else:
            return False
    def isDiagonalWin(self, row, col, winningMark):
        # ++ / -- 
        comp = []
        for delta in [[1, 1], [-1, -1], [1, -1], [-1, 1]]:
            left_up = 0
            starting_row, starting_col = row, col
            while self.inBound(starting_row, starting_col) and self.board[starting_row][starting_col] == winningMark:
                starting_row += delta[0]
                starting_col += delta[1]
                left_up += 1
            comp.append(left_up)
        if comp[0] + comp[1] - 1 >= self.winning or comp[2] + comp[3] - 1 >= self.winning:
            return True
        else:
            return False
            
    def inBound(self, row, col):
        if row < self.winning and row >= 0 and col < self.winning and col >= 0:
            return True
        else:
            return False
    
        
            
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
