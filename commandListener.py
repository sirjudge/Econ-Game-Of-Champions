# Command Class
import player
import trade


class CommandListener:

    # list of all commands made
    commandHistory = list()
    g_playerNotifications = list()
    g_teamList = []
    g_playerList = []
    g_playerInboxes = []
    g_playerNotifications = []
    g_playerTradeList = []

    # Turn variables
    g_turnNumber = 0
    g_player = None # global player variable. used for the current player commands are being used for

    # constructor takes in player list
    def __init__(self, pList):
        self.g_playerList = pList

    # processes commands. Takes in the current player as a variable
    @staticmethod
    def read_commands(self):
        # set turn_in_progress to end the turn
        turn_in_progress = True

        # store the current players stats
        player_name = self.g_player.get_name()
        player_num = self.g_player.get_player_num()

        # continue asking for a command until player is done with their turn
        while turn_in_progress:
            # these player attributes can change so we need to make sure they are updated
            player_money = self.g_player.get_money()
            player_team_name = self.g_player.get_team()

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
                self.g_playerNotifications[player_num] += 1
                print(self.g_playerNotifications[player_num])

            # lists player name and player team
            elif command_input == 'whoami':
                print('you are ' + player_name + ' on the team ' + player_team_name)

            # List the name of each player with the team they are on
            elif command_input == 'listPlayers':
                for q in range(0, len(self.g_playerList)):
                    print(str(q) + ':' + self.g_playerList[q].get_name())
                    print('\t' + self.g_playerList[q].get_team())

            # Team Related Commands
            elif command_input == 'listTeams':
                for z in range(0, len(self.g_teamList)):
                    print(str(z) + ':' + self.g_teamList[z])

            # Prints the players current team
            elif command_input == 'myTeam':
                print(player_team_name)

            # Changes the players team from already existing teams
            elif command_input == 'changeTeam':
                for p in range(0, len(self.g_teamList)):
                    print(str(p) + ':' + self.g_teamList[p])
                team_num_to_change = int(input('select a team number to change to'))
                if team_num_to_change == '':
                    print('you have not selected any team, remaining on the same team')
                elif team_num_to_change > (len(self.g_teamList)):
                    print('that team number does not exist, remaining on the same team')
                else:
                    self.g_player.set_team(self.g_teamList[team_num_to_change])

            # check your inbox
            elif command_input == 'checkMessages':
                for message in self.g_playerInboxes:
                    print(message)

            # send another player a message to their inbox
            elif command_input == 'message':
                self.print_players()
                player_to_send = int(input('Who do you want to message?'))
                msg_to_send = input('what is the message to send?')
                self.g_playerInboxes[player_to_send].append(msg_to_send)
                self.g_playerNotifications[player_to_send] += 1

            # Creates a new team and sets the player to the new team
            elif command_input == 'createTeam':
                team_name = input("what's your new team name?")
                self.g_player.set_team(team_name)

            # Get current player's balance
            elif command_input == 'balance':
                print(str(player_money))

            # Trade with another player
            elif command_input == 'trade':
                # TODO finish trade
                # have user select what they want to dos
                p_input = input('1. Check my trades \n 2. Start a new trade  \n 3. Accept or reject a trade')
                # Get a list of all trades either from or to the current player
                my_trades = self.check_my_trades(player_num)

                # list all the trades player currently has
                if p_input == '1':
                    for open_trade in my_trades:
                        print(open_trade)

                # create a new trade
                elif p_input == '2':
                    self.print_players()
                    player_to_trade_to = int(input('enter the player number of who you want to trade with'))
                    money_amount = int(input('how much money do you want to trade?'))

                    # (self, player_num_to, player_num_from, money_to_trade):
                    newTrade = trade.Trade(player_to_trade_to, player_num, money_amount)
                    self.g_playerTradeList.append(newTrade)

                # Confirm or deny each trade you have
                elif p_input == '3':
                    print('accept or deny a trade')
                    for open_trade in my_trades:
                        response = input('press [A] to accept the trade or [R] to reject the trade')
                        print('')
                        if response.lower() == 'a':
                            if open_trade._playerToStatus == 'a' or open_trade._playerToStatus == 'w':
                                self.g_player.trade_money()
                else:
                    'command not recognized, please enter a valid command'
                # if there are trades available
                if len(self.g_playerTradeList) > 0:
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

    def print_players(self):
        for y in range(0, len(self.g_playerList)):
            print(str(y) + ':' + self.g_playerList[y].get_name())

    def look_up_player(self, player_name):
        for player in self.g_playerList:
            if player.get_name() == player_name:
                return player

    # function takes in an amount and gives it to all the players
    def increase_economy(self, amount_to_raise):
        for player in self.g_playerList:
            player.add_money(amount_to_raise)

    def create_notification(self, msg, player_num):
        self.g_playerInboxes[player_num].append(msg)
        self.g_playerNotifications[player_num] += 1

    # returns a list of trades involving the current player
    def check_my_trades(self, curr_player_num):
        out = []
        for trade in self.g_playerTradeList:
            if (trade.get_player_num_from() == curr_player_num) or (trade.get_player_to_num() == curr_player_num):
                out.append(trade)
        return out
