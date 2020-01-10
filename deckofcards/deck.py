from card import Card

class Deck:

	def __init__(self):
		self.cards = []
		self.populate()
		print(self._cards)

	def populate(self):
		suits = ["hearts", "clubs", "diamonds", "spades"]
		numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

	cards = [] 
	#self._cards = [ Cards(s, n) for s in suits for n in number]
	for suit in suits:
		for number in numbers:
			cards.append( Card(suit, number) )
	self._cards = cards

my_deck = Deck()

