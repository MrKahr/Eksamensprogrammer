# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 14:08:29 2021

@author: danie
"""
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

card1 = Card(suit=random.randint(1,4), rank=10)
card2 = Card(suit=random.randint(1,4), rank=10)

print(card1)
print(card2)
print(card1<card2)
