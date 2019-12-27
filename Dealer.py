import random

class Dealer:
    deck_of_cards = \
        {'Ace': ({'Number in Deck': 4}, {'Value': [1, 11]}),
         'King': ({'Number in Deck': 4}, {'Value': 10}),
         'Jack': ({'Number in Deck': 4}, {'Value': 10}),
         'Queen': ({'Number in Deck': 4}, {'Value': 10}),
         'One': ({'Number in Deck': 4}, {'Value': 1}),
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

    def __init__(self, players):
        if len(players) > self.max_players:
            print('Max num of players exceeded, only {} allowed.'.format(self.max_players))
            self.num_players = self.max_players
            self.players = players[:self.max_players]
        else:
            self.num_players = len(players)

    def deal_cards(self):
        for i in range(2):
            for player in self.players:
                card_key = random.choice(list(self.deck_of_cards))
                self.deck_of_cards[card_key][0]['Number in Deck'] -= 1
                card_value = self.deck_of_cards[card_key][1]['Value']
                player.hit(self, {card_key: card_value})
        pass

    def hit_player(self, player):
        card_key = random.choice(list(self.deck_of_cards))
        while self.deck_of_cards[card_key][0]['Number in Deck'] == 0:
            card_key = random.choice(list(self.deck_of_cards))
        self.deck_of_cards[card_key][0]['Number in Deck'] -= 1
        card_value = self.deck_of_cards[card_key][1]['Value']
        player.hit(self, {card_key: card_value})

        
pass
