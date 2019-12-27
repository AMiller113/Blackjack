class Player:
    max_value = 21

    def __init__(self):
        self.hand = []
        self.current_total = 0
        self.player_name = input('Please enter a name for this player.')
        self.has_stayed = False
        pass

    def hit(self, new_card):
        self.hand.append(new_card)
        self.current_total = self.compute_total()

    def stay(self):
        self.has_stayed = True

    def compute_total(self):
        total = 0
        for card in self.hand:
            for card_name, card_value in self.card.items():
                if card_name != 'Ace':
                    total += card_value
                else:
                    total += self.choose_ace_value()
        return total

    def choose_ace_value(self):
        ace_value = input('{} Please enter a value for your Ace (1 or 11)\n'.format(self.player_name))
        while ace_value != '1' and ace_value != '11':
            ace_value = input('{} Please enter a value for your Ace (1 or 11)\n'.format(self.player_name))
            if ace_value != '1' and ace_value != '11':
                print('That is not a valid Ace value, please try again.')
                continue
        ace_value = int(ace_value)
        return ace_value

    def show_hand(self):
        print('Players {} hand.'.format(self.player_name))
        for card in self.hand:
            for card_name, card_value in self.card.items():
                print('Card {}: Value {}'.format(card_name, card_value))
        print(self.current_total)


pass
