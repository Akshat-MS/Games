
import validation_mod
import random

class UserInterface:

    # Initialize the user interface
    def __init__(self):
        self.board = []
        self.li = []
        self.size = 3

    # Description - Create the Board.
    # Parameters - Size of the Board [Square Matrix]
    def createBoard(self,size = 3):
        count = 1
        for i in range(size):
            row = []
            for j in range(size):
                row.append('_')
                self.li.append(count)
                count += 1
            self.board.append(row)
        

    # Description - Display the Board.
    # Parameters - None
    def displayBoard(self):
        for row in self.board:
            for item in row:
                print(item,end=" ")
            print("\n")

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
    
    # Description - Player Chance
    # Parameters - player number
    def playerChance(self,player):

        tic_verify = validation_mod.VerifyMod(self.board)

        while(True):
            try :
                num = int(input("Enter any number between 1 & 9 and fix the position : "))
            except ValueError:
                print("Not a proper integer! Try it again")
                continue
            print()
            cords = tic_verify.validMove(num,3)
            if cords[0] == 0:
                print("Not a valid Move!! Try it again")
                continue
            else:
                self.li.remove(num)
                break
        
        if (player == 1):
            self.updateBoard(cords,drawXO = 'X')
            self.displayBoard()
        else:
            self.updateBoard(cords,drawXO = 'O')
            self.displayBoard()

    # Description - Computer Chance
    # Parameters - player number
    def computerChance(self,player):
        tic_verify = validation_mod.VerifyMod(self.board)

        # Random Number generator using given list of numbers.
        random_num = random.choice(self.li)
    

        # Checking if its a valid Move.
        cords = tic_verify.validMove(random_num,self.size)

        # Update & display the Board.
        self.updateBoard(cords,drawXO = 'O')
        self.displayBoard() 

        self.li.remove(random_num)
