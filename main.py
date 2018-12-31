# Global Variables
__numPlayers = 2
__turnNum = 0
__player = []
__teams = []
__playerInboxes = []
__playerNotifications = []
__playerTradeList = []


def start_game():
    # keeps track of which player is currently doing their turn
    player_turn = 0
    # Keeps track of which turn the game is on
    game_turn = 0
    # In order to stop playing set still_playing to false
    still_playing = True
    print('playerNotification list:')
    for x in __playerNotifications:
        print(x)
    while still_playing:
        curr_player = __player[player_turn]
        read_commands(curr_player)
        if player_turn == __numPlayers:
            player_turn = 0
            game_turn += 1
        else:
            player_turn += 1
        print('your turn is over ' + curr_player.get_name() + '\n')


# function takes in an amount and gives it to all the players
def increase_economy(amount_to_raise):
    for player in __player:
        player.add_money(amount_to_raise)


def create_notification(msg, player_num):
    __playerInboxes[player_num].append(msg)
    __playerNotifications[player_num] += 1


# returns a list of trades involving the current player
def check_my_trades(curr_player_num):
    out = []
    for trade in __playerTradeList:
        if (trade.get_player_num_from() == curr_player_num) or (trade.get_player_to_num() == curr_player_num):
            out.append(trade)
    return out


# processes commands. Takes in the current player as a variable
def read_commands(player):
    # set turn_in_progress to end the turn
    turn_in_progress = True

    # store the current players stats
    player_name = player.get_name()
    player_num = player.get_player_num()

    # continue asking for a command until player is done with their turn
    while turn_in_progress:
        # these player attributes can change so we need to make sure they are updated
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
            print('are you sure you want to exit the game?')
            command_input = input('yes or no\n')
            if command_input.lower() == 'yes' or command_input.lower() == 'y':
                exit()
            else:
                print('continuing turn')

        # command for testing incrementation of player notifications
        elif command_input == 'incNot':
            __playerNotifications[player_num] += 1
            print(__playerNotifications[player_num])

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
            elif team_num_to_change > int(len(__teams)):
                print('that team number does not exist, remaining on the same team')
            else:
                player.set_team(__teams[team_num_to_change])

        # check your inbox
        elif command_input == 'checkMessages':
            for message in __playerInboxes:
                print(message)

        # send another player a message to their inbox
        elif command_input == 'message':
            print_players()
            player_to_send = int(input('Who do you want to message?'))
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
            # TODO finish trade
            # have user select what they want to do
            p_input = input('1. Check my trades \n 2. Start a new trade  \n 3. Accept or reject a trade')
            # Get a list of all trades either from or to the current player
            my_trades = check_my_trades(player_num)

            # list all the trades player currently has
            if p_input == '1':
                for open_trade in my_trades:
                    print(open_trade)

            # create a new trade
            elif p_input == '2':
                print_players()
                player_to_trade_to = int(input('enter the player number of who you want to trade with'))
                money_amount = int(input('how much money do you want to trade?'))
                newTrade = Trade(player_to_trade_to, player_num, money_amount)
                __playerTradeList.append(newTrade)

            # Confirm or deny each trade you have
            elif p_input == '3':
                print('accept or deny a trade')
                for open_trade in my_trades:
                    response = input('press [A] to accept the trade or [R] to reject the trade')
                    print('')
                    if response.lower() == 'a':
                        if open_trade._playerToStatus == 'a' or open_trade._playerToStatus == 'w':
                            player.trade_money()
            else:
                'command not recognized, please enter a valid command'
            # if there are trades available
            if len(__playerTradeList) > 0:
                print('you have a trade list')
            # If the player has no trades, the command won't run
            else:
                print('You have no trades, please enter a new command')
        # prints the list of commands found in commandList.txt
        elif command_input == 'help':
            help_file = open("commandList.txt", 'r')
            for line in help_file:
                print(line[:-1])
        else:
            print('command not recognized')


def print_players():
    for y in range(0, len(__player)):
        print(str(y) + ':' + __player[y].get_name())


def look_up_player(player_name):
    for player in __player:
        if player.get_name() == player_name:
            return player


class Trade:
    # the player number of who is recieving the trade
    _playerNumTo = ''
    # player number of who is sending the trade
    _playerNumFrom = ''
    _moneyToTrade = -1

    # Check to see if player has accepted, rejected, or sent new trade, or waiting response.
    # All new trades start as follows
    # n = new trade || a = accepted trade || r = rejected trade || w = waiting response
    # playerFrom = 'n' playerTo = 'w'
    _playerToStatus = 'w'
    _playerFromStatus = 'n'

    def __init(self, player_num_to, player_num_from, money_to_trade):
        self._playerNumTo = player_num_to
        self._playerNumFrom = player_num_from
        self._moneyToTrade_moneyToTrade = money_to_trade

    ####################
    # Getters + setters#
    ####################
    def get_player_to_num(self):
        return self._playerNumTo

    def get_player_num_from(self):
        return self._playerNumFrom

    def get_money_to_trade(self):
        return self._moneyToTrade

    def set_player_to_num(self, p_num):
        self._playerNumTo = p_num

    def set_player_num_from(self, p_num):
        self._playerNumFrom = p_num

    def set_money_to_trade(self, money_amount):
        self._moneyToTrade = money_amount


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

        '''
        #=============================
        # Defining and creating lists
        #=============================
        '''
        # create the list of player inboxes  to send messages to
        __playerInboxes = [[] for x in range(0, __numPlayers)]
        __playerNotifications = [0 for x in range(0, __numPlayers)]

        # add new player object to the player array
        newPlayer = Player(playerName, 100, teamName, playerNumber)
        __player.append(newPlayer)
        print("welcome to the game " + playerName + '. You are with team ' + teamName)
    start_game()
