import arcade

class CardGame(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Multiplayer Card Game")
        self.cards= []