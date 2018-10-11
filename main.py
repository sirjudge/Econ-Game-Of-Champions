from appJar import gui

# Global Variables
__numPlayers = 2
__turnNum = 0
__player = []
__teams = []
__app = gui('EconGame')
__playerInboxes = []
__playerNotifications = []


# function to print out the name of the button pressed
# followed by the contents of the two entry boxes
def press(btn_name):
    print('buttonName:' + btn_name)
    print(__app.getEntry('commandEntry'))
    __app.setLabel('prevCommand', __app.getEntry('commandEntry'))


def create_gui():
    __app.addTextArea("t1", 0, 1)
    __app.addLabel('previousCommand', 'previous command', 2, 0)
    __app.addEmptyLabel('prevCommand', 2, 1)

    __app.addLabel("commandLabel", "Command Input", 3, 0)
    __app.addEntry("commandEntry", 3, 1)

    __app.addButtons(["Submit", "Finish"], press, colspan=2)
    __app.setFocus("commandEntry")
    #    __app.enableEnter(press)
    # Start the gui
    __app.go()


def start_game():
    # keeps track of which player is currently doing their turn
    player_turn = 0
    # Keeps track of which turn the game is on
    game_turn = 0
    # In order to stop playing set still_playing to false
    still_playing = True
    while still_playing:
        curr_player = __player[player_turn]
        read_commands(curr_player)
        if player_turn == __numPlayers:
            player_turn = 0
            game_turn += 1
        else:
            player_turn += 1
        print('your turn is over ' + curr_player.get_name() + '\n')


# processes commands. Takes in the current player as a variable
def read_commands(player):
    # set turn_in_progress to end the turn
    turn_in_progress = True

    # temporarily store the current players stats
    player_name = player.get_name()

    while turn_in_progress:
        player_money = player.get_money()
        player_team_name = player.get_team()

        # Read Command line input
        command_input = input('What do you want to do?\n')

        # finish the turn not the game, confirm on exit
        if command_input == 'finish':
            print('are you sure you want to finish your turn?')
            command_input = input('yes or no?\n')
            if command_input.lower() == 'yes' or command_input.lower() == 'y':
                turn_in_progress = False
            else:
                print('continuing turn')

        # Exit the game with this command, confirm on exit
        elif command_input == 'exit':
            print('are you sure you want to finish your turn?')
            command_input = input('yes or no\n')
            if command_input.lower() == 'yes' or command_input.lower() == 'y':
                exit()
            else:
                print('continuing turn')

        # lists player name and player team
        elif command_input == 'whoami':
            print('you are ' + player_name + ' on the team ' + player_team_name)

        # List the name of each player with the team they are on
        elif command_input == 'listPlayers':
            for q in range(0, len(__player)):
                print(str(q) + ':' + __player[q].get_name())
                print('\t' + __player[q].get_team())

        # Team Related Commands
        elif command_input == 'listTeams':
            for z in range(0, len(__teams)):
                print(str(z) + ':' + __teams[z])

        # Prints the players current team
        elif command_input == 'myTeam':
            print(player_team_name)

        # Changes the players team from already existing teams
        elif command_input == 'changeTeam':
            for p in range(0, len(__teams)):
                print(str(p) + ':' + __teams[x])
            team_num_to_change = input('select a team number to change to')
            if team_num_to_change == '':
                print('you have not selected any team, remaining on the same team')
            elif team_num_to_change > len(__teams):
                print('that team number does not exist, remaining on the same team')
            else:
                player.set_team(__teams[team_num_to_change])

        # send another player a message to their inbox
        elif command_input == 'message':
            print_players()
            player_to_send = input('Who do you want to message?')
            msg_to_send = input('what is the message to send?')
            __playerInboxes[player_to_send].append(msg_to_send)
            __playerNotifications[player_to_send] += 1

        # Creates a new team and sets the player to the new team
        elif command_input == 'createTeam':
            team_name = input("what's your new team name?")
            player.set_team(team_name)

        # Get current player's balance
        elif command_input == 'balance':
            print(str(player_money))

        # Trade with another player
        elif command_input == 'trade':
            print('players to trade:\n')
            print_players()
            player_to_trade = input('What player do you want to trade with? (choose a number)\n')
            amount_to_trade = input('How much do you want to trade?\n')
            player.trade_money(__player[int(player_to_trade)], int(amount_to_trade))

        # TODO add descriptions of each command
        elif command_input == 'help':
            print('please use the following commands')
        else:
            print('command not recognized')


def print_players():
    for y in range(0, len(__player)):
        print(str(y) + ':' + __player[x].get_name())


"""
DAVID'S CODE
           # List each command and a description
           playerToTrade = look_up_player(input('What player do you want to trade with?'))
           amountToTrade = int(input('How much do you want to trade?'))
           player.trade_money(playerToTrade,amountToTrade)
"""


def look_up_player(player_name):
    for player in __player:
        if player.get_name() == player_name:
            return player


class Player:
    # Global class variables
    _name = ''
    _team = ''
    _money = 0
    _playerNumber = -1

    def __init__(self, player_name, curr_money, team, player_num):
        self._name = player_name
        self._money = curr_money
        self._team = team
        self._playerNumber = player_num

    # Getters and setters
    def get_team(self):
        return self._team

    def set_team(self, team_name):
        self._team = team_name

    def get_money(self):
        return self._money

    def set_money(self, money_val):
        self._money = money_val

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_player_num(self):
        return self._playerNumber

    def set_player_num(self, player_num):
        self._playerNumber = player_num

    # Trading with other players
    def subtract_money(self, value):
        self.set_money(self.get_money() - value)

    def add_money(self, value):
        self.set_money(self.get_money() + value)

    def trade_money(self, player_to_trade, amount_to_trade):
        if self.get_money() > amount_to_trade:
            self.subtract_money(amount_to_trade)
            player_to_trade.add_money(amount_to_trade)
            print(str(amount_to_trade) + ' has been traded to ' + player_to_trade.get_name())
        else:
            print('you do not have enough money in the bank to finish the transaction')


if __name__ == "__main__":
    # createGUI()
    # set number of players and check to see if user input a real number
    numPlayersInput = input("How many players are there? press enter to default to two players\n")
    # while intCheck is true, no valid input has been given
    intCheck = True
    while intCheck:
        # Make sure user input is valid
        try:
            # if no input is given set to default
            if numPlayersInput == '':
                __numPlayers = 2
            # set numPlayers to be an int
            else:
                numPlayers = int(numPlayersInput)
            intCheck = False
        # if you get an error when converting to an int, have user enter a real int.
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
        __numPlayers = int(numPlayersInput)

    # initialize player array
    for playerNumber in range(0, int(__numPlayers)):
        # Set the player and team name
        playerName = input('what is your name, player ' + str(playerNumber) + '?\n')

        # Create the list of teams
        if len(__teams) < 1:
            teamName = input('what would you like to call your team?\n')

            # Make sure that the team name isn't already taken
            while teamName in __teams:
                teamName = input('that name is already taken, please choose another')
            __teams.append(teamName)
        else:
            answer = input('do you want to create a team or join a team?\n')
            if answer == 'create':
                teamName = input('What is your team name?')
                # Make sure that the team name isn't already taken
                while teamName in __teams:
                    teamName = input('that name is already taken, please choose another')
                __teams.append(teamName)
            elif answer == 'join':
                for x in range(0, len(__teams)):
                    print(str(x) + ':' + __teams[x])
                teamNum = input('select your team number\n')
                teamName = __teams[int(teamNum)]
            else:
                print('okay wise guy that is not an answer, please create a team')
                teamName = input('What is your team name?')
                # Make sure that the team name isn't already taken
                while teamName in __teams:
                    teamName = input('that name is already taken, please choose another')
                    __teams.append(teamName)

        # create the list of player inboxes to send messages to
        __playerInboxes = [[] for x in range(0, __numPlayers)]
        __playerNotifications = [0 for x in range(0, __numPlayers)]
        # add new player object to the player array
        newPlayer = Player(playerName, 100, teamName, playerNumber)
        __player.append(newPlayer)
        print("welcome to the game " + playerName + '. You are with team ' + teamName)
    start_game()
