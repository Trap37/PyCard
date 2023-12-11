''' The module containing the Deck object
'''
from itertools import product
from random import shuffle
from card import Card
from player_entity import PlayerEntity

SUITS = ['CLUB', 'DIAMOND', 'HEART', 'SPADE']
VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


class Deck:
    ''' The Deck for the card game. Made of Cards
    '''

    def __init__(self, num_decks: int = 2) -> None:
        self._deck: list[Card] = []
        self.create_deck(num_decks)

    def create_deck(self, num_decks: int) -> None:
        '''create_deck Creates a new deck of cards

        Args:
            num_decks (int): Number of deck wanted
        '''

        if not isinstance(num_decks, int) or num_decks <= 0:
            raise ValueError("Number of decks must be a positive integer")

        deck: list[Card] = []

        for value, suit in product(VALUES, SUITS):
            card = Card(value, suit)
            deck.append(card)

        self._deck = deck * num_decks
        self.shuffle()

    def shuffle(self) -> None:
        '''shuffle Shuffles the deck
        '''
        shuffle(self._deck)

    def draw_card(self) -> Card:
        '''draw_card Draws a card from the Deck

        Returns:
            Card: A Card from the Deck
        '''
        card = self._deck.pop(0)
        return card

    def deal_cards(self, num_cards: int, players: list[PlayerEntity]) -> None:
        '''deal_cards Deals cards to all Players and the Dealer (if the dealer gets cards)

        Args:
            num_cards (int): Number of cards per hand to deal
            players (list[PlayerEntity]): The List of Players and the Dealer
        '''
        for _ in range(num_cards):
            for player in players:
                card = self.draw_card()
                player.add_cards(card)

    def get_cards(self) -> list[Card]:
        return self._deck
