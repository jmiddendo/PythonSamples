import random

class Game(object):

    def __init__(self):
        self.wordList, self.solutionArray, self.responseArray, self.guessLetter = list(), list(), list(), list()
        self.gameBoard = [[' ','_','_','_','_'],[' ','|',' ',' ','|'],[' ',' ',' ',' ','|'],[' ',' ',' ',' ','|'],[' ',' ',' ',' ','|'],[' ',' ',' ',' ','|'],['-','-','-','-','-']]
        self.alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.wrongGuess = 0
        self.loadWordList()
        self.chooseWord()

    def loadWordList(self):
        listFile = open('enable1.txt','r')
        for line in listFile.readlines():
            self.wordList.append(line)
        listFile.close()

    def chooseWord(self):
        wordIndex = random.randint(0,len(self.wordList)-1)
        self.solutionArray = self.wordList[wordIndex]
        for x in range(0,len(self.solutionArray) - 1):
            self.responseArray.append('-')

    def printBoard(self):
        for row in self.gameBoard:
            displayValue = ''
            for cell in row:
                displayValue += cell
            print(displayValue)

        
        displayValue = '\n'
        for x in range(len(self.alphabet)):
            displayValue += self.alphabet[x]
        displayValue += '\n'
        print(displayValue)

        displayValue = ''
        for x in range(len(self.responseArray)):
            displayValue += self.responseArray[x]
        print(displayValue)

    def checkWin(self):
        retValue = False
        if ('-' not in self.responseArray):
            print('You won the game!!')
            retValue = True
            self.printBoard()
        elif (self.wrongGuess == 6):
            print('You lost the game!!')
            print(self.solutionArray)
            retValue = True
        return retValue

    def takeTurn(self):
        runAgain = True

        while(runAgain):
            letter = input('Please enter a letter: ')

            if (len(letter.strip()) == 0):
                print('Please make an entry!')
                continue
            elif (len(letter.strip()) > 1):
                print('Please enter a single letter!')
                continue
            elif (letter.strip().lower() in self.guessLetter):
                print('You have already guessed that letter!')
                continue
            else:
                letter = letter.strip().lower()
                self.guessLetter.append(letter)
                self.alphabet[self.alphabet.index(letter)] = '-'

            runAgain = False


        if letter not in self.solutionArray:
            print('There is no ' + letter + ' in the word!')
            if (self.wrongGuess == 0):
                self.gameBoard[2][1] = 'O'
            elif (self.wrongGuess == 1):
                self.gameBoard[3][1] = '|'
            elif (self.wrongGuess == 2):
                self.gameBoard[3][0] = '\\'
            elif (self.wrongGuess == 3):
                self.gameBoard[3][2] = '/'
            elif (self.wrongGuess == 4):
                self.gameBoard[4][1] = '/'
            elif (self.wrongGuess == 5):
                self.gameBoard[4][1] = self.gameBoard[5][1] + '\\'
            self.wrongGuess += 1
        for x in range(len(self.solutionArray)):
            if (self.solutionArray[x] == letter):
                self.responseArray[x] = letter
                
    def startGame(self):
        while (not self.checkWin()):
            self.printBoard()
            self.takeTurn()

def main():
    currentGame = Game()
    currentGame.startGame()

if __name__ == '__main__':
    main()
