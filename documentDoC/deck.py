from card import Card

import random

class Deck:
    """
    The Deck class represents a deck of playing cards in order.
    """

    def __init__(self):
        self._cards = []
        self.populate()

    def populate(self):
        suits = ["hearts", "clubs", "diamonds", "spades"]
        numbers = [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]
        self._cards = [ Card(s, n) for s in suits for n in numbers ]

    def shuffle(self):
        random.shuffle(self._cards)

    def deal(self, no_of_cards):
        dealt_cards = []
        for i in range(no_of_cards):
            dealt_card = self._cards.pop(0)
            dealt_cards.append(dealt_card)
        return dealt_cards

    def __repr__(self):
        cards_in_deck = len(self._cards)
        return "Deck of " + str(cards_in_deck) + " cards"
        
deck = Deck()
print(deck)

#uncomment a line at a time to see methods in action
#hand = [deck.deal(4)]
#print(hand)

#print(deck)
#deck.shuffle()

#hand1 = [deck.deal(4)]
#print(hand1)
#print(deck)

