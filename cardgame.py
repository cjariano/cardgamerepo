from card import Card
from player import Player
import random

class CardGame():

    def __init__(self, player1_name, player2_name):
        self.deck = self.create_deck()
        self.players = [Player(player1_name), Player(player2_name)]
        self.current_player_index = 0
        self.play_pile = []

    def create_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        deck = [Card(suit, value) for suit in suits for value in values]
        random.shuffle(deck)
        return deck
    
    def deal_cards(self):
        #deal hands and downcards to players
        for player in self.players:
            player.deal_face_down(self.deck)
            player.deal_hand(self.deck)

            #implement click for this
            face_up_cards = input("What 4 cards do you want face-up? ")

            player.choose_face_up(face_up_cards)

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

    def get_current_player(self):
        return self.players[self.current_player_index]


    def player_turn(self):
        current_player = self.get_current_player()
        print(f"{current_player.name}'s turn")

        #implement click
        cards_to_play = input("What card(s) do you want to play? ")

    
