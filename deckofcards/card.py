class Card:

	def __init__(self, suit, number):
		self._suit = suit
		self._number = number

	def __repr__(self):
		return self._number + " of " + self._suit
	
	@property
	def suit(self):
		return self._suit

	@suit.setter
	def suit(self, suit):
		if suit in ["Hearts", "Clubs", "Diamonds", "Spades"]:
			self._suit = suit
		else:
			print("That's not a suit!")


my_card = Card("hearts", "6")
print(my_card)

my_card.suit = "dinosaurs"
print(my_card)

