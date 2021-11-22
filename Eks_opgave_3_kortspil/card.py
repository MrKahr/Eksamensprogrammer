# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 14:08:29 2021

@author: danie
"""
import random


class Card:
    """Dette er hvert individuelt kort"""
    def __init__(self, suit = "",rank = 0):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        if self.rank == 0:
            return ""
        else:
            return str(rank[self.rank]) + " of " + self.suit
    def __lt__(self,other):
        return (self.rank)<(other.rank)


suit = ['Clubs', 'Hearts', 'Spades', 'Diamonds']
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

card1 = Card(suit=suit[random.randint(0,3)], rank=random.randint(2,14))
card2 = Card(suit=suit[random.randint(0,3)], rank=random.randint(2,14))

print(card1)
print(card2)

print(card1 < card2)