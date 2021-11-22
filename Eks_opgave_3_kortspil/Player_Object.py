import random


class Card:
    """Definér et kort"""
    def __init__(self, suit = "",rank = 0):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        if self.rank == 0:
            return ""
        else:
            return str(rank[self.rank]) + " of " + str(suits[self.suit])
    def __lt__(self,other):
        return (self.suit,self.rank)<(other.suit,other.rank)


suits = {1: 'Clubs',
         2: 'Diamonds',
         3: 'Hearts',
         4: 'Spades'}

rank =      {2:2,
             3:3,
             4:4,
             5:5,
             6:6,
             7:7,
             8:8,
             9:9,
             10:10,
             11: 'Jack',
             12: 'Queen',
             13: 'King',
             14: 'Ace'}


# ! Defines what a deck is
class Deck:
    # * Make dummy deck with stack of cards 
    def __init__(self, deck=[]):
        self.deck = deck
        #self.size = size
        
    # * Shuffle a stack of cards
    def shuffle(self): 
        random.shuffle(self.deck)
        return self.deck

    
    def deal(self, amount):
        dealt_hand = self.deck[:amount]
        self.deck = self.deck[amount:]
        
        return dealt_hand
    
    # * Add cards won to deck
    def __add__(self, other):
        return self.deck + other.deck


# ! Defines what a player is
class Player:
    # * Initialize Player
    def __init__(self, name=''):
        self.name = name
        self.hand = Deck()
        self.discard = Deck()
    
    # * Deals x amount of cards from players hand
    def play_card(self):
        if self.still_playing(self):
            if len(self.hand) == 0:
                self.reshuffle(self)
            self.hand.deal(self,1)
        else:     
            return False, f'Player {self.name} is no longer playing'
    
    # * Vital status for given player
    def still_playing(self):
        # 0 for dead and 1 for living player
        if len(self.hand.deck) + len(self.discard.deck) == 0:
            return False
        else:
            return True
    
    def reshuffle(self):
        self.__add__(self.hand,self.discard)
        self.discard = []
    
    # TODO random name
    # TODO hand as Deck
    # TODO discard pile as Deck
    # TODO Function to call deal from Deck
    # TODO Function to say if dead or not