''' The module containing the Hand object
'''
from .card import Card

card_values = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
    'A': 11,
}


class Hand:
    '''The Hand object of Players or Dealers
    '''

    def __init__(self) -> None:
        self._cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        '''add_cards Adds a card to a player's hand

        Args:
            cards (Card): The Card object that you want added
        '''
        self._cards.append(card)

    def calculate_value(self) -> int:
        '''calculate_value Calculates the numeric value of a hand

        Returns:
            int: Numeric value of a Hand
        '''
        value = 0
        for card in self._cards:
            value += int(card.get_value())
        return value
