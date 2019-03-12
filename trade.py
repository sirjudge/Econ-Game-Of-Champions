# TRADE CLASS


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

    def __init__(self, player_num_to, player_num_from, money_to_trade):
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
