import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return f"{self.value} of {self.suit}"
    
    def __str__(self):
        return f"{self.value} of {self.suit}"
    
    # def __lt__(self, other):
    #     # Handle comparison of cards, for example: 2 < 3, Queen < King, etc.
    #     if self.value == other.value:
    #         return self.suit < other.suit  # or any other rule you want to implement for suits
    #     card_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    #     return card_values.index(self.value) < card_values.index(other.value)
    
    def flip(self):
        self.is_face_up = not self.is_face_up