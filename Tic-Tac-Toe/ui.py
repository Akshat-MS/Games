
class UserInterface:

    # Initialize the user interface
    def __init__(self):
        self.board = []
        self.size = 3

    # Description - Create the Board.
    # Parameters - Size of the Board [Square Matrix]
    def createBoard(self,size = 3):
        for i in range(size):
            row = []
            for j in range(size):
                row.append('_')
            self.board.append(row)

    # Description - Display the Board.
    # Parameters - None
    def displayBoard(self):
        for row in self.board:
            for item in row:
                print(item,end=" ")
            print()

    # Description - Update the Board
    # Parameters - Position of the move
    #            - Draw with X or O
    def updateBoard(self,pos,drawXO = 'X'):
            self.board[pos[1]][pos[2]] = drawXO
    
    # Description - Check if the board is full
    # Parameters - None
    def isBoardFull(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == '_':
                    return False
        return True