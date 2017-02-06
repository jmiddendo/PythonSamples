##  Dice game race to 200

import random

class Player(object):

    def __init__(self, newName):
        self.playerName = newName
        self.playerScore = 0

class Dice(object):

    def __init__(self, newMin, newMax):
        self.minValue = newMin
        self.maxValue = newMax

    def rollDice(self):
        return random.randint(self.minValue, self.maxValue)

class Game(object):

    dice = Dice(1,6)
    validName, activeGame = False, False
    strPlayerOne, strPlayerTwo = 'Player One', 'Player Two'
    playerOne, playerTwo = Player(strPlayerOne), Player(strPlayerTwo)
    maxScore = 200

    def queryName(self, player):
        runAgain = True
        
        while (runAgain):
            playerName = input('Please enter a name for the {} player: '.format(player))
            if (len(playerName.strip()) == 0):
                print('Please enter a valid name!')
                print('')
            else:
                runAgain = False

        return playerName

    def checkNumber(self, testNumber):
        try:
            testNumber = int(testNumber)
        except:
            return False
        else:
            return True
        
    def registerUser(self):

        userResponse = ''

        if(self.activeGame):
            userResponse = input('Game already in progress.  Do you want to start a new game? (y or n) : ')
            
        if (userResponse.upper() == 'Y' or not self.activeGame):
            strPlayerOne = self.queryName('first')
            strPlayerTwo = self.queryName('second')
            playerOne = Player(strPlayerOne)
            playerTwo = Player(strPlayerTwo)
            newValue = input('Maximum score to win (<Enter> to use default 200) : ')
            if (newValue.strip() == 0):
                print('\nDefault value accepted!')
            elif (self.checkNumber(newValue)):
                self.maxScore = int(newValue)
            self.activeGame = True

    def determineWinner(self):
        if (self.playerOne.playerScore > self.playerTwo.playerScore):
            print('\n{}\'s current score is {} points  <--- WINNER!!'.format(self.playerOne.playerName, self.playerOne.playerScore))
            print('{}\'s current score is {} points.'.format(self.playerTwo.playerName, self.playerTwo.playerScore))
        elif (self.playerOne.playerScore < self.playerTwo.playerScore):
            print('\n{}\'s current score is {} points.'.format(self.playerOne.playerName, self.playerOne.playerScore))
            print('{}\'s current score is {} points  <--- WINNER!!'.format(self.playerTwo.playerName, self.playerTwo.playerScore))
        elif (self.playerOne.playerScore == self.playerTwo.playerScore):
            print('\nThe game ends in a tie!')
            print('{}\'s current score is {} points.'.format(self.playerOne.playerName, self.playerOne.playerScore))
            print('{}\'s current score is {} points.'.format(self.playerTwo.playerName, self.playerTwo.playerScore))
        else:
            print('\nI don\'t know what happened in this game!')
        self.activeGame = False
            
                
    def completeSingleRoll(self, player):
        firstRoll, secondRoll, roundScore = self.dice.rollDice(), self.dice.rollDice(), 0
        if (firstRoll == secondRoll):
            print('{} rolled a {} + {} and scored {} points (Bonus).'.format(player.playerName, firstRoll, secondRoll, (firstRoll + secondRoll)*2))
        else:
            print('{} rolled a {} + {} and scored {} points.'.format(player.playerName, firstRoll, secondRoll, (firstRoll + secondRoll)))
        player.playerScore += firstRoll
        player.playerScore += secondRoll

        

    def executeTurn(self):
        if (not self.activeGame):
            print('Error : Players have not been set up!')
        else:
            self.completeSingleRoll(self.playerOne)
            self.completeSingleRoll(self.playerTwo)

        if (self.playerOne.playerScore > self.maxScore or self.playerTwo.playerScore > self.maxScore):
            self.determineWinner()
            

    def checkScore(self):
        if (not self.activeGame):
            print('Error : Players have not been set up!')
        else:
            if (self.playerOne.playerScore == self.playerTwo.playerScore):
                print('The game is a tie!')
            elif (self.playerOne.playerScore > self.playerTwo.playerScore):
                print('{}\'s current score is {} points  <--- Current LEADER!'.format(self.playerOne.playerName, self.playerOne.playerScore))
                print('{}\'s current score is {} points.'.format(self.playerTwo.playerName, self.playerTwo.playerScore))
            elif (self.playerOne.playerScore < self.playerTwo.playerScore):
                print('{}\'s current score is {} points.'.format(self.playerOne.playerName, self.playerOne.playerScore))
                print('{}\'s current score is {} points  <--- Current LEADER!'.format(self.playerTwo.playerName, self.playerTwo.playerScore))
            else:
                print('I don\'t understand what is happening in the game')
        

    def displayHelp(self):
        print('Welcome to FIT9131 Dice Game!')
        print('-----------------------------')
        print('Please read the menu carefully!')
        print('Please chose option 1, FIRST!  You cannot take your turn or view scores without players!  This is also the option you will use to set the maximum score.\n')

        print('After you create the players, use option 2 to roll the dice and take you turns.  You can')
        print('repeat this option until you reach the max score.  The game will then display the winner.\n')

        print('You can chose option 3 any time after player creation to display who the current leader is\n')

        print('You can chose option 4 any time to display this help menu again.\n')

        print('Use option 5 to exit the game.')

    def exitGame(self):
        print('Thank you for playing.  Have a great day!\n')

    def playGame(self):

        runAgain = True
        userChoice = 0

        while(userChoice != 5):
            userChoice = 0
            print('\nWelcome to My Dice-and-Roll Game!')
            print('=================================')
            print('(1) Start New Game')
            print('(2) Play One Round')
            print('(3) Who is leading now?')
            print('(4) Display Game Help')
            print('(5) Exit Game\n')
            userChoice = input('Please select an option : ')

            if not self.checkNumber(userChoice):
                print('\nPlease enter a valid number!')
                continue

            userChoice = int(userChoice)

            if (userChoice < 1 or userChoice > 5):
                print('\nPlease make a choice from the menu!')
                continue

            print('\n')
            
            if (userChoice == 1):
                self.registerUser()
            elif (userChoice == 2):
                self.executeTurn()
            elif (userChoice == 3):
                self.checkScore()
            elif (userChoice == 4):
                self.displayHelp()
            elif (userChoice == 5):
                self.exitGame()
            else:
                print('I did not understand that request.  Please try again!')
                    
        
def main():
    currentGame = Game()
    currentGame.playGame()
    
    
if __name__ == '__main__':
    main()
        
