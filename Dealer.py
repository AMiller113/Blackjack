import random
from Player import Player


class Dealer:
    deck_of_cards = \
        {'Ace': ({'Number in Deck': 4}, {'Value': [1, 11]}),
         'King': ({'Number in Deck': 4}, {'Value': 10}),
         'Jack': ({'Number in Deck': 4}, {'Value': 10}),
         'Queen': ({'Number in Deck': 4}, {'Value': 10}),
         'Two': ({'Number in Deck': 4}, {'Value': 2}),
         'Three': ({'Number in Deck': 4}, {'Value': 3}),
         'Four': ({'Number in Deck': 4}, {'Value': 4}),
         'Five': ({'Number in Deck': 4}, {'Value': 5}),
         'Six': ({'Number in Deck': 4}, {'Value': 6}),
         'Seven': ({'Number in Deck': 4}, {'Value': 7}),
         'Eight': ({'Number in Deck': 4}, {'Value': 8}),
         'Nine': ({'Number in Deck': 4}, {'Value': 9}),
         'Ten': ({'Number in Deck': 4}, {'Value': 10})}
    max_players = 6
    minimum_players = 2

    def __init__(self, players):
        self.num_players = len(players)
        self.players = players

    def deal_cards(self):
        for i in range(2):
            for player in self.players:
                card_key = random.choice(list(self.deck_of_cards))
                self.deck_of_cards[card_key][0]['Number in Deck'] -= 1
                card_value = self.deck_of_cards[card_key][1]['Value']
                card = {card_key: card_value}
                player.hit(card)
        for player in self.players:
            print('Player {} initial hand'.format(player.player_name))
            player.show_hand()
        pass

    def hit_player(self, player):
        card_key = random.choice(list(self.deck_of_cards))
        while self.deck_of_cards[card_key][0]['Number in Deck'] == 0:
            card_key = random.choice(list(self.deck_of_cards))
        self.deck_of_cards[card_key][0]['Number in Deck'] -= 1
        card_value = self.deck_of_cards[card_key][1]['Value']
        card = {card_key: card_value}
        player.hit(card)

    def all_stayed(self):
        _all_stayed = False
        for player in self.players:
            if player.has_stayed is False:
                return _all_stayed
        _all_stayed = True
        return _all_stayed

    def game_status(self):
        has_winner = False
        winners = []
        if self.all_stayed():
            max_hand = 0
            for player in self.players:
                if max_hand < player.current_total <= 21:
                    winners.clear()
                    winners.append(player)
                    max_hand = player.current_total
                elif player.current_total == max_hand:
                    winners.append(player)
            has_winner = True
        elif len(self.players) is 1:
            winners.append(self.players[0])
            has_winner = True
        else:
            for player in self.players:
                if player.current_total == 21:
                    has_winner = True
                    winners.append(player)
        if has_winner is True:
            if len(winners) == 1:
                player = winners[0]
                print(player.show_hand())
                print('Player {} has won the game! Thank you for playing.'.format(player.player_name))
            else:
                print('The game is a draw between players...')
                for player in winners:
                    print(player.player_name)
                    player.show_hand()
                print('Thank you for playing!')
        return has_winner

    def disqualify_player(self, player):
        print('Player {} is eliminated, better luck next time.'.format(player.player_name))
        self.players.remove(player)

pass
