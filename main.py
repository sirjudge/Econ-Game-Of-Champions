import commandListener
import player
import trade

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
        commandListener.read_commands(curr_player)
        if player_turn == __numPlayers:
            player_turn = 0
            game_turn += 1
        else:
            player_turn += 1
        print('your turn is over ' + curr_player.get_name() + '\n')


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
        newPlayer = player(playerName, 100, teamName, playerNumber)
        __player.append(newPlayer)
        print("welcome to the game " + playerName + '. You are with team ' + teamName)
    start_game()
