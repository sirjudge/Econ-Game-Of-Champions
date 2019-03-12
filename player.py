# PLAYER CLASS


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
