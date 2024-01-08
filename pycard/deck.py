from random import shuffle

from .card import Card

SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
VALUES = ['Ace', '2', '3', '4', '5', '6', '7',
          '8', '9', '10', 'Jack', 'Queen', 'King']
DECK_SIZE = 52


class Deck:

    def __init__(self, num_decks: int = 2) -> None:
        self._cards: list[Card] = []
        self.new_deck(num_decks)

    @property
    def cards(self):
        return self._cards

    def new_deck(self, num_decks: int = 2) -> None:
        """
        Creates a new deck of cards

        Args:
        num_decks (int): Numner of individual decks added to this deck

        Raises:
            ValueError: Number of decks must be a positive integer
        """

        if not isinstance(num_decks, int) or num_decks <= 0:
            raise ValueError('Number of decks must be a positive integer')

        deck = [Card(value, suit) for value in VALUES for suit in SUITS]

        self._cards = deck * num_decks
        self.shuffle()

    def shuffle(self) -> None:
        shuffle(self._cards)

    def draw_card(self) -> Card:
        card = self._cards.pop(0)
        return card

    def deal_cards(self, num_cards: int, players) -> None:
        for _ in range(num_cards):
            for player in players:
                card = self.draw_card()
                player.add_cards(card)

    def get_cards(self) -> list[Card]:
        return self._cards
