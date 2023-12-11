''' The module containing the Card object
'''


class Card:
    ''' The Card objects in the Player hands and the Deck 
    '''

    def __init__(self, value: str, suit: str) -> None:
        self._value = value
        self._suit = suit

    def get_value(self) -> str:
        return self._value

    def get_suit(self) -> str:
        return self._suit

    def __str__(self) -> str:
        return f'{self._value} of {self._suit}'
