from .card import Card
from .hand import Hand


class PlayerEntity:

    def __init__(self, name: str, balance: float) -> None:
        self.name = name
        self.balance = balance
        self.hand = Hand()

    def add_cards(self, cards: Card) -> None:
        self.hand.add_card(cards)
