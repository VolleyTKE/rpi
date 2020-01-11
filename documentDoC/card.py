class Card:
    """
    The Card class represents a single playing card and is initialised by passing a suit and number.
    """
    def __init__(self, suit, number):
        self._suit = suit
        self._number = number

    def __repr__(self):
        return self._number + " of " + self._suit

    @property
    def suit(self):
        """Gets or sets the suit of the Card"""
        return self._suit
    

    @suit.setter
    def suit(self, suit):
        #no need for a docstring on a setter
        if suit in ["hearts", "clubs", "diamonds", "spades"]:
            self._suit = suit
        else:
            print("That's not a suit!")

    @property
    def number(self):
        """Gets or sets the number of the Card"""
        return self._number

    @number.setter
    def number(self, number):
        valid = [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]
        if number in valid:
            self._number = number
        else:
            print("That's not a valid number")
