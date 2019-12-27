class Player:
    max_value = 21

    def __init__(self):
        self.hand = {}
        self.current_total = self.compute_total()
        self.player_name = input('Please enter a name for this player.')
        pass

    def hit(self, new_card):
        self.hand.update(new_card)
        self.current_total = self.compute_total()

    def stay(self):
        pass

    def compute_total(self):
        total = 0
        for card_name, card_value in self.hand.items():
            if card_name != 'Ace':
                total += card_value[1]
            else:
                total += self.choose_ace_value(self)
        return total

    def choose_ace_value(self):
        while ace_value != 1 or ace_value != 11:
            ace_value = input('{} Please enter a value for your Ace (1 or 11)'.format(self.player_name))
            if ace_value != 1 or ace_value != 11:
                print('That is not a valid Ace value, please try again.')
        return ace_value


pass
