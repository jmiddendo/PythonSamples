class Game(object):
    def __init__(self):
        self.gameBoard = [['-','-','-'],['-','-','-'],['-','-','-']]
        self.playerTurn = 1

    def printBoard(self):
        print('\n-----------')
        for row in self.gameBoard:
            printValue = '' 
            for cell in row:
                printValue += ' ' + cell + ' |'

            if (printValue[len(printValue) - 1]):
                printValue = printValue[:-1]
            print(printValue)
            print('-----------')

    def takeTurn(self):

        runAgain = True;
        validEntry = True;
        
        while(validEntry):
            while(runAgain):
                xInput = input('Please enter the X input: ')
                try:
                    xInput = int(xInput)
                except:
                    print('\nPlease enter a valid value!')
                    continue
                if (xInput < 0 or xInput > 2):
                    print('\nPlease enter either a 0, 1, or 2')
                    continue
                runAgain = False

            runAgain = True

            while(runAgain):
                yInput = input('Please enter the Y input: ')
                try:
                    yInput = int(yInput)
                except:
                    print('\nPlease enter a valid value!')
                    continue
                if (yInput < 0 or yInput > 2):
                    print('\nPlease enter either a 0, 1, or 2')
                    continue
                runAgain = False

            runAgain = True
            
            if (self.gameBoard[xInput][yInput] != '-'):
                print('\nPlease chose an empty square!')
                continue

            validEntry = False
            
        if (self.playerTurn == 1):
            self.gameBoard[xInput][yInput] = 'x'
            self.playerTurn = 2
        else:
            self.gameBoard[xInput][yInput] = 'o'
            self.playerTurn = 1

    def checkWin(self):
        retValue = False
        dashCount = 0
        if (self.gameBoard[0][0] == 'x' and self.gameBoard[0][1] == 'x' and self.gameBoard[0][2] == 'x') or \
           (self.gameBoard[1][0] == 'x' and self.gameBoard[1][1] == 'x' and self.gameBoard[1][2] == 'x') or \
           (self.gameBoard[2][0] == 'x' and self.gameBoard[2][1] == 'x' and self.gameBoard[2][2] == 'x') or \
           (self.gameBoard[0][0] == 'x' and self.gameBoard[1][0] == 'x' and self.gameBoard[2][0] == 'x') or \
           (self.gameBoard[0][1] == 'x' and self.gameBoard[1][1] == 'x' and self.gameBoard[2][1] == 'x') or \
           (self.gameBoard[0][2] == 'x' and self.gameBoard[1][2] == 'x' and self.gameBoard[2][2] == 'x') or \
           (self.gameBoard[0][0] == 'x' and self.gameBoard[1][1] == 'x' and self.gameBoard[2][2] == 'x') or \
           (self.gameBoard[2][2] == 'x' and self.gameBoard[1][1] == 'x' and self.gameBoard[0][0] == 'x'):
            retValue = True
            print('Player 1 wins the game!')
            self.printBoard()
        elif (self.gameBoard[0][0] == 'o' and self.gameBoard[0][1] == 'o' and self.gameBoard[0][2] == 'o') or \
           (self.gameBoard[1][0] == 'o' and self.gameBoard[1][1] == 'o' and self.gameBoard[1][2] == 'o') or \
           (self.gameBoard[2][0] == 'o' and self.gameBoard[2][1] == 'o' and self.gameBoard[2][2] == 'o') or \
           (self.gameBoard[0][0] == 'o' and self.gameBoard[1][0] == 'o' and self.gameBoard[2][0] == 'o') or \
           (self.gameBoard[0][1] == 'o' and self.gameBoard[1][1] == 'o' and self.gameBoard[2][1] == 'o') or \
           (self.gameBoard[0][2] == 'o' and self.gameBoard[1][2] == 'o' and self.gameBoard[2][2] == 'o') or \
           (self.gameBoard[0][0] == 'o' and self.gameBoard[1][1] == 'o' and self.gameBoard[2][2] == 'o') or \
           (self.gameBoard[2][2] == 'o' and self.gameBoard[1][1] == 'o' and self.gameBoard[0][0] == 'o'):
            retValue = True
            print('Player 2 wins the game!')
            self.printBoard()
        elif '-' in self.gameBoard:
            retValue = True

        return retValue
            

    def playGame(self):

        while(not self.checkWin()):
            self.printBoard()
            if (self.playerTurn == 1):
                print('\nPlayer 1\'s turn: ')
            else:
                print('\nPlayer 2\'s turn: ')
            self.takeTurn()
        
            

def main():
    currentGame = Game()
    currentGame.playGame();

if __name__ == '__main__':
    main()
