''' The module containing the Player and Dealer class Parent
'''
from card import Card
from hand import Hand


class PlayerEntity:
    def __init__(self, name: str) -> None:
        self.name = name
        self.hand = Hand()

    def add_cards(self, cards: Card) -> None:
        self.hand.add_card(cards)
