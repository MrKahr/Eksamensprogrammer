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
            return str(rank[self.rank]) + " of " + self.suit
        
    def __lt__(self,other):
        return (self.rank,self.suit)<(other.rank,other.suit)


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
        self.hand = copy.deepcopy(Deck())
        self.discard = copy.deepcopy(Deck())
    
    # * Deals x amount of cards from players hand
    def play_card(self):
        if self.still_playing():
            if len(self.hand.deck) == 0:
                self.reshuffle()
            return self.hand.deal(1)
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
        self.hand += self.discard
        self.hand.shuffle()
        self.discard = copy.deepcopy(Deck())
        
    def __str__(self):
        return self.name
        
# ! Defines the game 'krig'
class KrigTheGame:
    # * Initiate KrigTheGame
    def __init__(self, player_count=10, round_cap=10, deck_count=1):
        self.round = 1 # Starting round
        self.round_cap = round_cap # Maximum amount of rounds
        
        self.player_names = ['Snake Eyes', 'Evil Eric', 'Dangerous Daniel', 'Anonymous Andreas', 'Mad Mads', 'Thieving Thor', 'Angry Adam', 'Divine Dat', 'Troublesome Tobias', 'Nefarious Nikolaj', 'Killer Krisitan', 'Kind Kristian', 'Kingly Kristian', 'Xtreme Xiaoyin', 'Glorious Gianni', 'Lucky Laila', 'Serious Sandra', 'Paitient Peter', 'Tactical Tereza', 'Keen Kristoffer', 'Kinetic Kasper', 'Salty Stefan'] # Availible player names
        self.player_count = player_count # Amount of players
        #self.players = self.players() # Generate players at the table
        #print(self.players)
        
        self.deck_count = deck_count # Amount of decks used
        self.card_stack = self.gen_deck() # Generate this games deck
        
        self.players_at_table = self.players()
        self.table = copy.deepcopy(Deck())
        self.pot = copy.deepcopy(Deck())
        #print(self.dvd_card_stack)
    
    # * Generate deck
    def gen_deck(self):
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
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
        self.card_stack.shuffle()
        while len(self.card_stack.deck) > 0:
            card = self.card_stack.deal(1)[0]
            player = self.players_at_table[player_index]
            player.hand.deck.append(card)
            player_index += 1
            if player_index > len(self.players_at_table)-1:
                player_index = 0
        
        #for player in self.players_at_table:
            #print(player.hand, end='\n')
            #print(len(player.hand.deck), end ='\n\n')
    
    def who_wins(self):
        highest = Card(suit = "", rank = 0)
        h_index = 0
        for i in range(len(self.table.deck)):
            #print((self.table.deck[i]))
            if highest < self.table.deck[i]:
                highest = self.table.deck[i]
                h_index = i
        self.pot = copy.deepcopy(Deck())
        print('Table:')
        for card in range(len(self.table.deck[:-1])):
            print(f'{self.table.deck[card]},', end=' ')
        print(self.table.deck[-1], end='\n\n')
        print(f'The highest card is {highest}', end = '\n\n')
        print(f'Player {self.players_at_table[h_index]} has won the round!', end='\n\n')
       
        return h_index
    
    def runRound(self):
        self.makeAllPlay()
        i = self.who_wins()
        winner = self.players_at_table[i]

        winner.discard += self.table
        
        print('The current standings are:')
        
        for player in self.players_at_table:
            standings = len(player.hand.deck) + len(player.discard.deck)
            print(f'{player}: {standings}')
            standings = copy.deepcopy(Deck())
        self.table = copy.deepcopy(Deck())

    def makeAllPlay(self):
        active_players = []
        for i in range(len(self.players_at_table)):
            player = self.players_at_table[i]
            if player.still_playing():
                active_players.append(player)
        self.players_at_table = copy.deepcopy(active_players)
        for player in self.players_at_table:
            card = player.play_card()[0]
            self.table += Deck(deck = [card])

    def print_hand(self):
        for player in self.players_at_table:
            print(player.hand, end='\n')
            print(len(player.hand.deck))
            print(len(player.discard.deck),end ='\n\n')
    
    def play_game(self):
        self.div_stack()
        for i in range(self.round_cap):
            print(f'\nRound {i}: ', end='\n')
            print('The players are:')
            for player in self.players_at_table[:-1]:
                print(f'{player} and ', end ='')
            print(self.players_at_table[-1], end='\n\n')
            self.runRound()
        win_points = 0
        winner_index_list = []
        for i in range(len(self.players_at_table)):
            player = self.players_at_table[i]
            standings = len(player.hand.deck) + len(player.discard.deck)
            if standings > win_points:
                win_points = standings
                winner_index = i
                draw = False
                winner_index_list = [i]
            elif standings == win_points:
                draw = True
                winner_index_list.append(i)
        if draw:
            print('\nThe game is a draw!')
            for index in winner_index_list[:-1]:
                print(f'{self.players_at_table[index]} and', end = ' ')
            print(self.players_at_table[winner_index_list[-1]])
        else:
            print(f'\nThe winner is {self.players_at_table[winner_index]}')


krig = KrigTheGame(round_cap = 10)
krig.play_game()