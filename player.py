class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.downCards = []
        self.upCards = []

    def selectUpCards(self, card):
        self.hand.remove(card)
        self.upCards.append(card)

    def playCardFromHand(self, cards):
        for card in cards:
            self.hand.remove(card)
        return cards

    def pickUpCards(self, cards):
        for card in cards:
            self.hand.append(card)

    def playDownCard(self):
        self.downCards.pop()

    def __repr__(self):
        return f"{self.name} - Hand: {self.hand}, Face-up: {self.upCards}"