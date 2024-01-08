from .player_entity import PlayerEntity


class Player(PlayerEntity):

    def __init__(self, name: str, balance: float) -> None:
        super().__init__(name, balance)
