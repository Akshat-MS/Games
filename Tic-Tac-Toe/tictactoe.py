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
print("Welcome to Play Tic Tac Toe")
print("Choose one options as shown below - ")
print("1. Single Player.")
print("2. Two player Game. ")
print()

while True:
    try :
        bSingleFlag = int(input("Choose playing Option "))
    except:
        print("Not a proper integer1! Try it again")
        continue
    break

while True:

    if bSingleFlag == 1 and player == 1:
        tic_ui.playerChance(1)
    elif bSingleFlag == 1 and player == 2:
        tic_ui.computerChance(1)
    else:
        tic_ui.playerChance(2)

    # Win Check    
    if player == 1:
        if tic_verify.winCheck(1):
            print("Player One Won")
            break
        else:
            print("\nPlayer Two Chance")
            player = 2
    else:
        if tic_verify.winCheck(2):
            print("Player Two Won")
            break
        else:
            print("\nPlayer One Chance")
            player = 1

    # Board Full Check
    if tic_ui.isBoardFull():
        print("Game Over and Match Draw!!")
        break

