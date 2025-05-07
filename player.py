class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.face_up = []
        self.face_down = []
    
    def deal_hand(self, deck):
        """Deal 7 cards to the player's hand."""
        self.hand = [deck.pop() for _ in range(7)]
    
    def deal_face_down(self, deck):
        """Deal 4 face-down cards."""
        self.face_down = [deck.pop() for _ in range(4)]

    def choose_face_up(self, cards):
        """Choose 4 face-up cards from hand"""
        self.face_up = [self.hand.remove(card) for card in cards]
    
    def play_card(self, cards):
        """Play card(s) from the player's hand."""
        return (self.hand.remove(card) for card in cards)
    
    def play_face_up_card(self, card_index):
        """Play face-up card"""
        return (self.face_up.pop(card_index))
    
    def play_face_down_card(self, card_index):
        """Play face-down card"""
        return (self.face_down.pop(card_index))
    
    def __repr__(self):
        return f"{self.name} - Hand: {self.hand}, Face-up: {self.face_up}, Number of face-down: {len(self.face_down)}"
