''' The module containing the Player and Dealer class Parent
'''
from .card import Card
from .hand import Hand


class PlayerEntity:
    ''' The Parent class of the Dealer and Player
    '''

    def __init__(self, name: str = '', balance: float = 0.0) -> None:
        self.name = name
        self.balance = balance
        self.hand = Hand()

    def add_cards(self, cards: Card) -> None:
        '''add_cards Add Cards to the object's Hand

        Args:
            cards (Card): A Card object
        '''
        self.hand.add_card(cards)
