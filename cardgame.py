from deck import Deck
from player import Player

class CardGame():

    def __init__(self, player1_name, player2_name):
        self.deck = Deck()
        self.players = [Player(player1_name), Player(player2_name)]
        self.current_player_index = 0

    def deal(self):
        #deal hands and downcards to players
        self.deck.shuffle()

        for player in self.players:
            #deal hands
            for _ in range(7):
                player.hand.append(self.deck.deal_one())

            #deal down cards
            for _ in range(4):
                player.downCards.append(self.deck.deal_one().flip())

    def pick_up_cards(self):
        for player in self.players:
            #deal hands
            for _ in range(4):
                card = input("What card do you want to put up? ")
                player.selectUpCards(card)

    def next_player(self):
        #switch to the next player
        if self.current_player_index != len(self.players) - 1:
            self.current_player_index = self.current_player_index + 1
        else:
            self.current_player_index = 0

    
