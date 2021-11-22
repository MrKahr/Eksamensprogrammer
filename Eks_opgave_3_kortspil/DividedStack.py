# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 14:01:02 2021

@author: danie
"""

import random
import copy

class Card:
    """Definér et kort"""
    def __init__(self, suit = "",rank = 0):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        if self.rank == 0:
            return ""
        else:
            return str(rank[self.rank]) + " of " + self.suit + ' '
    def __lt__(self,other):
        return (self.rank)<(other.rank)


suit = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

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
        self.deck += other.deck
        return self
    
    def __str__(self):
        deck = ''
        for card in self.deck:
            deck += str(card)
        return deck


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
        
    def __str__(self):
        return self.name
    

# ! Defines the game 'krig'
class KrigTheGame:
    # * Initiate KrigTheGame
    def __init__(self, player_count=2, round_cap=10, deck_count=1):
        self.round = 1 # Starting round
        self.round_cap = round_cap # Maximum amount of rounds
        
        self.player_names = ['Hans', 'Bonk', 'Paul', 'Eric', 'Tror', 'At', 'Du', 'Er', 'Til', 'Men'] # Availible player names
        self.player_count = player_count # Amount of players
        #self.players = self.players() # Generate players at the table
        #print(self.players)
        
        self.deck_count = deck_count # Amount of decks used
        self.card_stack = self.gen_deck() # Generate this games deck
        
        self.players_at_table = self.players()
        #self.dvd_card_stack = self.divide_stack()
        #print(self.dvd_card_stack)
    
    # * Generate deck
    def gen_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        card_stack = []
        
        # Generates card object for all cards in a deck, for all decks
        for deck in range(self.deck_count):
            for i, suit in enumerate(suits):
                for card in range(2, 15):
                    card_stack.append(Card(suit, card))
        return Deck(deck = card_stack)
    
    # * Generate players
    def players(self):
        players_at_table = []
        random.shuffle(self.player_names)
        
        for i in range(self.player_count):
            players_at_table.append(copy.deepcopy(Player(self.player_names[i])) )
        return players_at_table
    
    def div_stack(self):
        player_index = 0
        while len(self.card_stack.deck) > 0:
            card = self.card_stack.deal(1)[0]
            player = self.players_at_table[player_index]
            player.hand.deck.append(card)
            player_index += 1
            if player_index > len(self.players_at_table)-1:
                player_index = 0
        for player in self.players_at_table:
            print(player.hand, end='\n')
            print(len(player.hand.deck), end ='\n\n')


krig = KrigTheGame()
krig.div_stack()