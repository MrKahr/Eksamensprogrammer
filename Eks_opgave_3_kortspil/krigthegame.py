'''
Link til github: https://github.com/MrKahr/Eksamensprogrammer
Tredje eksamens opgave i IPD: Kort spil
@authors: Mads Andersen, Eric van den Brand, Daniel Hansen, Thor Skatka og Andreas Hansen
Beskrivelse: Programmet udfører spillet krig, med valgfrit antal runder og spillere
'''

import random
import copy

rank = {2:2,
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


# ! Define Card class
class Card:
    # * Assign atributes to Card class
    def __init__(self, suit= '', rank = 0):
        self.suit = suit
        self.rank = rank
    
    # * Set str() method to print card instance
    def __str__(self):
        if self.rank == 0:
            return ''
        else:
            return str(rank[self.rank]) + ' of ' + self.suit
    
    # * Overload < operator to compare card instances
    def __lt__(self,other):
        return (self.rank, self.suit) < (other.rank, other.suit) # Compares ranks. If ranks are equal, compare suits


# ! Defines Deck class
class Deck:
    # * Assign atributes to Deck class
    def __init__(self, deck= []):
        self.deck = deck
    
    # * Shuffle a deck
    def shuffle(self): 
        random.shuffle(self.deck)
        return self.deck
    
    # * Deals x amount of cards from deck
    def deal(self, amount):
        dealt_hand = self.deck[:amount]
        self.deck = self.deck[amount:]
        
        return dealt_hand
    
    # * Overload + operator to concatenate deck with other deck
    def __add__(self, other):
        self.deck += other.deck
        return self
    
    # * Set str() method to print deck instance
    def __str__(self):
        deck = ''
        for card in self.deck:
            deck += str(card)
        
        return deck


# ! Defines Player class
class Player:
    # * Assign atributes to Player class
    def __init__(self, name=''):
        self.name = name
        self.hand = copy.deepcopy(Deck())
        self.discard = copy.deepcopy(Deck())
    
    # * Deals x amount of cards from players hand
    def play_card(self):
        if len(self.hand.deck) == 0: # If hand is empty, add discard pile to hand
            self.reshuffle()
        
        return self.hand.deal(1) # Player plays a card
    
    # * Checks if player is out of cards
    def still_playing(self):
        # If player has no cards left return False, else return True
        if len(self.hand.deck) + len(self.discard.deck) == 0:
            return False
        else:
            return True
    
    # * Add cards from discard pile to hand
    def reshuffle(self):
        self.hand += self.discard
        self.hand.shuffle()
        self.discard = copy.deepcopy(Deck())
    
    # * Set str() method to print name of player instance
    def __str__(self):
        return self.name


# ! Defines the game 'krig'
class KrigTheGame:
    # * Assign atributes to KrigTheGame class
    def __init__(self, player_count= 10, round_cap= 10): # Define optional parameters according to exam discription
        self.round = 1 # Starting round
        self.round_cap = round_cap # Maximum amount of rounds
        
        
        # Availible player names
        self.player_names = ['Snake Eyes', 'Evil Eric', 'Dangerous Daniel', 
                            'Anonymous Andreas', 'Mad Mads', 'Thieving Thor', 
                            'Angry Adam', 'Divine Dat', 'Troublesome Tobias', 
                            'Nefarious Nikolaj', 'Killer Krisitan', 'Kind Kristian', 
                            'Kingly Kristian', 'Xtreme Xiaoyin', 'Glorious Gianni', 
                            'Lucky Laila', 'Serious Sandra', 'Paitient Peter', 
                            'Tactical Tereza', 'Keen Kristoffer', 'Kinetic Kasper', 
                            'Salty Stefan']
        
        self.player_count = player_count # Amount of players
        self.deck_count = 1 # Amount of decks used
        
        self.card_stack = self.gen_deck() # Generate full deck for game instance
        
        self.players_at_table = self.players() # Generate players at table
        self.table = copy.deepcopy(Deck()) # Generate deck for played cards i.e. the active cards
    
    # * Generate deck
    def gen_deck(self):
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        card_stack = []
        
        # Generate deck, with size of deck_count, consisting of card objects for all cards
        for deck in range(self.deck_count):
            for i, suit in enumerate(suits):
                for rank in range(2, 15): 
                    card_stack.append(Card(suit, rank))
        
        return Deck(deck = card_stack)
    
    # * Generate players
    def players(self):
        players_at_table = []
        random.shuffle(self.player_names) # Shuffle available player names
        
        for i in range(self.player_count): # Assign each player a name from available player names
            players_at_table.append(copy.deepcopy(Player(self.player_names[i])))
        
        return players_at_table
    
    # * Divide available cards among all players
    def div_stack(self):
        player_index = 0
        self.card_stack.shuffle() # Shuffle the card stack
        
        # Deals one card off the top of the deck to each player, until card stack is empty
        while len(self.card_stack.deck) > 0:
            card = self.card_stack.deal(1)[0] # Locates the top card
            player = self.players_at_table[player_index] # Locates player to receive card
            
            player.hand.deck.append(card) # Give card to player
            player_index += 1
            
            if player_index > len(self.players_at_table)-1: # Returns to the first player after giving a card to the last player
                player_index = 0
    
    # * Defines who wins the round
    def who_wins(self):
        highest = Card(suit = "", rank = 0)
        h_index = 0
        
        for i in range(len(self.table.deck)): # Loops over cards in play and finds the highest one
            if highest < self.table.deck[i]:
                highest = self.table.deck[i]
                h_index = i
        
        print('Table:')
        
        for card in range(len(self.table.deck[:-1])): # Prints all cards in play exept the last card
            print(f'{self.table.deck[card]},', end=' ')
        
        print(self.table.deck[-1], end='\n\n') # Prints last card in play
        
        print(f'The highest card is {highest}', end = '\n\n') # Prints highest card
        print(f'Player {self.players_at_table[h_index]} has won the round!', end='\n\n') # Prints winner of the round
        
        return h_index
    
    # * Makes all players play a card and checks for active players
    def make_all_play(self):
        active_players = []
        
        for i in range(len(self.players_at_table)): # Checks wich players are still in the game
            player = self.players_at_table[i]
            
            if player.still_playing():
                active_players.append(player)
        
        self.players_at_table = copy.deepcopy(active_players) # Sets active players to players at table
        
        for player in self.players_at_table: # Makea all players play a card
            card = player.play_card()[0]
            self.table += Deck(deck = [card])
    
    # * Runs one round of the game
    def run_round(self):
        self.make_all_play() # Makes all active players play a card
        i = self.who_wins() # Finds winner of the round
        winner = self.players_at_table[i]
        winner.discard += self.table # Adds cards from table to winners discard pile
        
        print('The current standings are:')
        
        for player in self.players_at_table: # Prints amount of cards each player has
            standings = len(player.hand.deck) + len(player.discard.deck)
            print(f'{player}: {standings}')
            standings = copy.deepcopy(Deck())
        
        self.table = copy.deepcopy(Deck())
    
    # * Prints the hand of each player (error check function)
    def print_hand(self):
        for player in self.players_at_table:
            print(player.hand, end='\n')
            print(len(player.hand.deck))
            print(len(player.discard.deck),end ='\n\n')
    
    # * Runs the game
    def play_game(self):
        self.div_stack() # Divides the card stack
        
        for i in range(self.round_cap):
            if len(self.players_at_table) > 1: # Check if more than one player is still playing
                print(f'\nRound {i+1}: ', end='\n')
                print('The players are:')
                
                for player in self.players_at_table[:-1]: # Print each player at table exept last player
                    print(f'{player} and ', end ='')
                
                print(self.players_at_table[-1], end='\n\n') # Print last player at table
                
                self.run_round() # Runs the round
                
                most_cards = 0
                winner_index_list = []
                
                for j in range(len(self.players_at_table)): # For each player at table
                    player = self.players_at_table[j]
                    standings = len(player.hand.deck) + len(player.discard.deck) # Players total amount of cards
                    
                    if standings > most_cards: # If players card total > than previous most cards
                        most_cards = standings # Sets most cards to players card total
                        winner_index = j
                        draw = False
                        winner_index_list = [j] # Sets player as current lead
                    elif standings == most_cards: # If players card total == current lead card total
                        draw = True
                        winner_index_list.append(j) # Add player to current lead(s)
                
                if i == self.round_cap-1: # Last round
                    if draw:
                        print('\nThe game is a draw!')
                        print('The winners are:')
                        for index in winner_index_list[:-1]: # Prints all winners of game except last one
                            print(f'{self.players_at_table[index]} and', end = ' ')
                        
                        print(self.players_at_table[winner_index_list[-1]]) # Prints last winner
                    else:
                        print(f'\nThe winner is {self.players_at_table[winner_index]}') # Print winner
            else:
                break

krig = KrigTheGame()
krig.play_game()
