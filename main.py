import re

__numPlayers = 2
__turnNum = 0
__player = []

if __name__ == "__main__":
    # set number of players and check to see if user input a real number
    numPlayersInput  = input("How many players are there? press enter to default to two players\n")

    # Make sure user input is valid
    try:
        numPlayers = int(numPlayersInput)
    except ValueError:
       print("That's not an int!")
       numPlayers = input('please enter a real number between 1 and 4\n')

    # set global variables accordingly
    if numPlayers == '':
        __numPlayers=2
    elif numPlayers > 4:
       print('too high of a number, reducing to 4 players\n')
       __numPlayers=4
    else:
        __numPlayers = numPlayers

    # initialize player array
    for x in __numPlayers:
        __player.additem('player' + x)
        print("welcome to the show\n")

def startGame():
    playerTurn = 1
    # In order to stop playing set stillPlaying to false
    stillPlaying = True
    while stillPlaying:
        currPlayer = player[playerTurn]
        readCommands(currPlayer)
        if playerTurn == __numPlayers:
            playerTurn = 1
        else:
            playerTurn += 1 


def readCommands(player):
    turnInProgress = True
    while(turnInProgress):
        command = raw_input('What do you want to do?')
        if command == 'exit': 
            print( 'are you sure you want to finish your turn?')
            input = raw_input("yes or no?")
            if input.lower() == 'yes' or input.lower() == 'y':
                turnInProgress = False
            else:
                print('continuing turn')
        elif command == 'trade':
            playerToTrade = raw_input('What player do you want to trade with?')
            amountToTrade = raw_input('How much do you want o trade?')
            player.tradeMoney(playerToTrade,amountToTrade)
        elif command == 'help':
            print('please use the following commands')
        else:
            print('command not recognized')

class player():
    def __init__(self, currMoney, team):
        self.currentMoney= currMoney
        self.team = team

    def getTeam(self):
        return self.team
    def setTeam(teamVal):
        self.team = teamVal

    def getMoney(self):
        return self.currentMoney
    def setMoney(self, moneyVal):
        self.currentMoney = moneyVal

    def subtractMoney(self, value):
        self.setMoney(self.getMoney() - value)

    def addMoney(self, value):
        self.setMoney(self.getMoney + value)

    def tradeMoney(self,playerToTrade, amountToTrade):
        if self.getMoney() > amountToTrade:
            self.subtractMoney(amountToTrade)
            playerToTrade.addMoney(amountToTrade)
            print(str(amountToTrade) + ' has been traded to ' + playerToTrade)
        else:
            print('you do not have enough money in the bank to finish the transaction')

