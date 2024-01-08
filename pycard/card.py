class Card:

    def __init__(self, value: str, suit: str) -> None:
        """
        Initializes a new Card instance.

        Parameters:
            _value (str): The value of the card.
            _suit (str): The suit of the card.
        """
        self._value = value
        self._suit = suit

    @property
    def value(self) -> str:
        """
        Getter method for retrieving the value of the card.

        Returns:
            str: The value of the card.
        """

        return self._value

    @property
    def suit(self) -> str:
        """
        Getter method for retrieving the suit of the card.

        Returns:
            str: The suit of the card.
        """
        return self._suit

    def __str__(self) -> str:
        return f'{self._value} of {self._suit}'
