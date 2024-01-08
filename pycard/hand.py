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

    def __init__(self) -> None:
        self._cards: list[Card] = []

    @property
    def cards(self):
        return self._cards

    def add_card(self, *cards: Card) -> None:
        self._cards.extend(cards)

    def calculate_value(self) -> int:
        value = 0

        for card in self._cards:
            value += int(card.value)

        return value

    def __len__(self) -> int:
        return len(self._cards)

    def __str__(self) -> str:
        return '\n\n'.join([f'{card.value} of {card.suit}' for card in self.cards])
