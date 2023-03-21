# Package to verify Valid Move and to check Win or Loose Tic Tac Toe.

class VerifyMod:

    def __init__(self,board):
        self.board = board
        
    def validMove(self,num,size = 3):
        count = 0
        if (num >  (size ** 2) or num < 1):
            print("Invalid input")
            return [0,0,0]
        for i in range(size):
            for j in range(size):
                count += 1
                if (count == num and self.board[i][j] == '_'):
                    return [1,i,j]
        return [0,0,0]
    
    def winCheck(self,player,size = 3):
        res = None

        if player == 1:
            strPlayer = 'X'
        else:
            strPlayer = 'O'

        # Validating Rows
        for i in range(size):
            res = True
            for j in range(size):
                if (self.board[i][j] != strPlayer):
                    res = False
                    break
            if (res):
                return res
        
        # Validating Cols
        for i in range(size):
            res = True
            for j in range(size):
                if (self.board[j][i] != strPlayer):
                    res = False
                    break
            if (res):
                return res
            
        # Validaing Diaginoals
        res = True
        for i in range(size):
            if (self.board[i][i] != strPlayer):
                res = False
                break
        if (res):
            return res
        
        res = True
        for i in range(size):
            if (self.board[i][size - i - 1] != strPlayer):
                res = False
                break
        if (res):
            return res
        
        return False
        
