# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 14:04:32 2021
@author: mdsan
"""
import random

class Kort:
    '''Definer et kort'''

cards1 = [1,2,3,4,5]
cards2 = [1,2,3,4,5]

class Deck:
    '''Definer et stak kort'''
    
    # Make dummy deck with stack of cards 
    def __init__(self, size = 4): 
        self.size = 4
        
    # Shuffle a stack of cards
    def cshuffle(self): 
        random.shuffle(self)
        return self 

    # Play and remove top card from deck
    def cplay(self): 
        return self.pop(0)  
    
    # Add cards won to deck
    def __add__(self, other):
        return self + other

# q = Stack.cshuffle(cards1)
# p = Stack.cplay(cards1)
z = Deck.__add__(cards1, cards2)


