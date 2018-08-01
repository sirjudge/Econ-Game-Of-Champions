__numPlayers = 2
__turnNum = 0

if __name__ == "__main__":
    # set number of players and check to see if user input a real number
    numPlayersInput  = input("How many players are there? press enter to default to two players\n")
    try:
        numPlayers = int(numPlayersInput)
    except ValueError:
       print("That's not an int!")
       numPlayers = input('please enter a real number between 1 and 4\n')
    if numPlayers == '':
        __numPlayers=2
    elif numPlayers > 4:
       print('too high of a number, reducing to 4 players\n')
       __numPlayers=4
    else:
        __numPlayers = numPlayers
    print("welcome to the show\n")

def startGame():
    playerTurn = 1 
    # In order to stop playing set stillPlaying to false
    stillPlaying = True
    while stillPlaying:
        

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

