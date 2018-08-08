# Global Variables
__numPlayers = 2
__turnNum = 0
__player = []
__teams = []

def startGame():
    # keeps track of which player is currently doing their turn
    playerTurn = 0
    # Keeps track of which turn the game is on
    gameTurn = 0
    # In order to stop playing set stillPlaying to false
    stillPlaying = True
    while stillPlaying:
        currPlayer = __player[playerTurn]
        readCommands(currPlayer)
        if playerTurn == __numPlayers:
            playerTurn = 0
            gameTurn += 1
        else:
            playerTurn += 1
        print('your turn is over ' + currPlayer.getName() + '\n')

# processes commands. Takes in the current player as a variable
def readCommands(player):
    turnInProgress = True
    while turnInProgress:
        # temporarily store the current players stats
        playerName = player.getName()
        playerMoney = player.getMoney()
        playerTeamName = player.getTeam()

        # Read Command line input
        commandInput = input('What do you want to do?\n')

        # finish the turn not the game, confirm on exit
        if commandInput == 'finish':
            print('are you sure you want to finish your turn?')
            commandInput = input('yes or no?\n')
            if commandInput.lower() == 'yes' or commandInput.lower() == 'y':
                turnInProgress = False
            else:
                print('continuing turn')

        # Exit the game with this command, confirm on exit
        elif commandInput == 'exit':
            print('are you sure you want to finish your turn?')
            commandInput = input('yes or no\n')
            if commandInput.lower() == 'yes' or commandInput.lower() == 'y':
                exit()
            else:
                print('continuing turn')

        # lists player name and player team
        elif commandInput == 'whoami':
            print('you are ' + player.getName() + ' on the team ' + player.getTeam())

        # List the name of each player with the team they are on
        elif commandInput == 'listPlayers':
            for x in range(0, len(__player)):
                print(str(x) + ':' + __player[x].getName())
                print('\t' + __player[x].getTeam())

        # Team Related Commands
        elif commandInput == 'listTeams':
            for x in range(0,len(__teams)):
                print(str(x) + ':'  + __teams[x])
        elif commandInput == 'myTeam':
            print(player.getTeam())
        elif commandInput == 'changeTeam':
            for x in range(0,len(__teams)):
                print(str(x) + ':' + __teams[x])
            teamNum = input('select a team number to change to')
            if teamNum == '':
                print('you have not selected any team, remaining on the same team')
            elif teamNum > len(__teams):
                print('that team number does not exist, remaining on the same team')
            else:
                player.setTeam(__teams[teamNum])

        elif commandInput == 'createTeam':
            teamName = input("what's your new team name?")
            player.setTeam(teamName)

        # Get current player's balance
        elif commandInput == 'balance':
            print(str(player.getMoney()))

        # Trade with another player
        elif commandInput == 'trade':
            print('players to trade:\n')
            for x in range(0, len(__player)):
                print(str(x) + ':' + __player[x].getName())
            playerToTrade = input('What player do you want to trade with? (choose a number)\n')
            amountToTrade = input('How much do you want to trade?\n')
            player.tradeMoney(__player[int(playerToTrade)], int(amountToTrade))

        # TODO add descriptions of each command
        elif commandInput == 'help':
            print('please use the following commands')

        else:
            print('command not recognized')


"""
DAVID'S CODE
           # List each command and a description
           playerToTrade = lookUpPlayer(input('What player do you want to trade with?'))
           amountToTrade = int(input('How much do you want to trade?'))
           player.tradeMoney(playerToTrade,amountToTrade)
"""


def lookUpPlayer(playerName):
    for player in __player:
        if player.getName() == playerName:
            return player


class Player():
    # Global class variables
    _name = ''
    _team = ''
    _money = 0
    _playerNumber = -1

    def __init__(self, playerName, currMoney, team, playerNum):
        self._name = playerName
        self._money = currMoney
        self._team = team
        self._playerNumber = playerNum

    # Getters and setters
    def getTeam(self):
        return self._team
    def setTeam(self, teamName):
        self._team = teamName

    def getMoney(self):
        return self._money
    def setMoney(self, moneyVal):
        self._money = moneyVal

    def getName(self):
        return self._name
    def setName(self, name):
        self._name = name

    def getPlayerNum(self):
        return self._playerNum
    def setPlayerNum(self, playerNum):
        self._playerNum = playerNum

    # Trading with other players
    def subtractMoney(self, value):
        self.setMoney(self.getMoney() - value)

    def addMoney(self, value):
        self.setMoney(self.getMoney() + value)

    def tradeMoney(self, playerToTrade, amountToTrade):
        if self.getMoney() > amountToTrade:
            self.subtractMoney(amountToTrade)
            playerToTrade.addMoney(amountToTrade)
            print(str(amountToTrade) + ' has been traded to ' + playerToTrade.getName())
        else:
            print('you do not have enough money in the bank to finish the transaction')


if __name__ == "__main__":
    # set number of players and check to see if user input a real number
    numPlayersInput = input("How many players are there? press enter to default to two players\n")

    # while intCheck is true, no valid input has been given
    intCheck = True
    while intCheck:
        # Make sure user input is valid
        try:
            if numPlayersInput == '':
                __numPlayers = 2
            else:
                numPlayers = int(numPlayersInput)
            intCheck = False
        except ValueError:
            print("That's not an int!")
            numPlayers = input('please enter a real number between 1 and 4\n')
    # set global variables accordingly
    if numPlayersInput == '':
        __numPlayers = 2
    elif int(numPlayersInput) > 4:
        print('too high of a number, reducing to 4 players\n')
        __numPlayers = 4

    else:
        __numPlayers = numPlayersInput

    # initialize player array
    for playerNumber in range(0, __numPlayers):
        # Set the player and team name
        playerName = input('what is your name, player ' + str(playerNumber) + '?\n')

        if len(__teams) < 1:
            teamName = input('what would you like to call your team?\n')
            __teams.append(teamName)
        else:
            answer = input('do you want to create a team or join a team?\n')
            if answer == 'create':
                teamName = input('what is your team name?\n')
                __teams.append(teamName)
            elif answer == 'join':
                for x in range(0,len(__teams)):
                    print(str(x) + ':' + __teams[x])
                teamNum = input('select your team number\n')
                teamName = __teams[int(teamNum)]

        # add new player object to the player array
        newPlayer = Player(playerName, 100, teamName, playerNumber)
        __player.append(newPlayer)
        print("welcome to the game " + playerName + '. You are with team ' + teamName)
    startGame()
