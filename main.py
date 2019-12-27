from Dealer import Dealer
from Player import Player


def setup():
    print('Welcome to Blackjack!')
    num_of_players = input('Please enter the number of players in this game '
                           '(maximum {}, minimum {})\n'.format(Dealer.max_players, Dealer.minimum_players))
    while not num_of_players.isdigit():
        num_of_players = input('That was not a valid number. '
                               'Please enter the number of '
                               'players in this game (maximum {})'.format(Dealer.max_players))
    num_of_players = int(num_of_players)
    players = []
    for i in range(num_of_players):
        players.append(Player())
    dealer = Dealer(players)
    dealer.deal_cards()
    return dealer


def main_loop(dealer):
    game_over = dealer.game_status()
    while game_over is False:
        for player in dealer.players:
            player.show_hand()
            while not player.has_stayed:
                move = input('Player {}, hit or stay?\n'.format(player.player_name))
                move.lower()
                while move != 'hit' and move != 'stay':
                    move = input('Please input a valid move, hit or stay?\n')
                    move.lower()
                if move == 'hit':
                    dealer.hit_player(player)
                    player.show_hand()
                    if player.current_total > 21:
                        break
                else:
                    player.stay()
            has_winner = dealer.game_status()
            if has_winner is True:
                game_over = True
                break
    print('The game has ended, please play again sometime!')


current_dealer = setup()
main_loop(current_dealer)
