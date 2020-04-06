class Deck:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def reset_deck(self):
        self.cards = []

    def add_card_to_deck(self, card):
        self.cards.append(card)

    def del_card_from_deck(self, card):
        self.cards.remove(card)
