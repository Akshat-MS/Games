# Adding libraries used in the Project.
import ui
import validation_mod

# Starting the game

# Initializing the different Modules
tic_ui = ui.UserInterface()
tic_verify = validation_mod.VerifyMod(tic_ui.board)

# Create the Tic Tac Toe Board.
tic_ui.createBoard()
tic_ui.displayBoard()

# Decalaring global variables
turn = 1
player = 1
while True:

    try :
        num = int(input("Enter any number between 1 & 9 and fix the position : "))
    except ValueError:
        print("Not a proper integer! Try it again")
        continue

    print()

    cords = tic_verify.validMove(num,3)
    if (cords[0] == 1 and player == 1):
        tic_ui.updateBoard(cords,drawXO = 'X')
    elif (cords[0] == 1):
        tic_ui.updateBoard(cords,drawXO = 'O')

    if player == 1:
        print("Player One Turn")
        tic_ui.displayBoard()
    else:
        print("Player Two Turn")
        tic_ui.displayBoard()
        
    if player == 1:
        if tic_verify.winCheck(1):
            print("Player One Won")
            break
    else:
        if tic_verify.winCheck(2):
            print("Player Two Won")
            break

    if cords[0] == 1 and player%2 == 1:
        player = 2
    else :
        player = 1

    if tic_ui.isBoardFull():
        print("Game Over and Match Draw!!")
        break

