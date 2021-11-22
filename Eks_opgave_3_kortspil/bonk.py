import random


# ! Defines what a card is
class Card:
    # * Initiate Card
    def __init__(self, suit='', rank=0):
        self.suit = suit
        self.rank = rank
    
    # * Print card as string
    def __str__(self):
        if self.rank == 0:
            return ""
        else:
            return str(self.rank) + " of " + self.suit
    
    # * Define less than between two cards
    def __lt__(self, other):
        return (self.rank) < (other.rank)
    
    # * Define card name of face cards and ace
    def card_name(self, rank):
        name_list = {11: 'Jack',
                    12: 'Queen',
                    13: 'King',
                    14: 'Ace'}
        
        return name_list[rank]


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
    
    # * Play and remove top card from deck
    def play(self):
        return self.deck.pop(0)
    
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
        return self.hand.deal(self, 1)
    
    # * Vital status for given player
    def vital_status(self):
        # 0 for dead and 1 for living player
        if len(self.hand.deck) + len(self.discard.deck) == 0:
            return 0
        else:
            return 1
    
    # TODO random name
    # TODO hand as Deck
    # TODO discard pile as Deck
    # TODO Function to call deal from Deck
    # TODO Function to say if dead or not


# ! Defines the game 'krig'
class KrigTheGame:
    # * Initiate KrigTheGame
    def __init__(self, player_count=2, round_cap=10, deck_count=1):
        self.round = 1 # Starting round
        self.round_cap = round_cap # Maximum amount of rounds
        
        self.player_names = ['Hans', 'Bonk', 'Paul'] # Availible player names
        self.player_count = player_count # Amount of players
        self.players = self.players() # Generate players at the table
        #print(self.players)
        
        self.deck_count = deck_count # Amount of decks used
        self.card_stack = self.gen_deck() # Generate this games deck
        
        self.players_at_table = self.players()
        self.dvd_card_stack = self.divide_stack()
        print(self.dvd_card_stack)
    
    # * Generate deck
    def gen_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        card_stack = []
        
        # Generates card object for all cards in a deck, for all decks
        for deck in range(self.deck_count):
            for i, suit in enumerate(suits):
                for card in range(2, 15):
                    card_stack.append(Card(suit, card))
        
        return card_stack
    
    # * Generate players
    def players(self):
        players_at_table = []
        random.shuffle(self.player_names)
        
        for i, name in enumerate(self.player_names):
            players_at_table.append(Player(name))
        print(players_at_table)
        return players_at_table
    
    def divide_stack(self):
        dvd_card_stack = []
        amount = len(self.card_stack) // self.player_count
        
        for i in range(0, len(self.card_stack), amount):
            dvd_card_stack.append(self.card_stack[i:i+amount])
        
        return dvd_card_stack

Krig = KrigTheGame()
    # TODO Definer liste af spillere
    # TODO Vuder vinder af runden
    # TODO krig funktion
    # TODO Hold styr på nuværende runde
    # TODO Bordet som liste af aktiv kort
    # TODO Giv bordet til vinderen
    # TODO Dræb spiller
    # TODO Vurder vinderen
