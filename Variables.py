
#variables for card values

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':0}


import random

# Card class definition

class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit 

# Deck class definition

class Deck():

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)

                self.all_cards.append(created_card)

        print("Successfully created Deck")

    def shuffle(self):

        random.shuffle(self.all_cards)

    def deal_one(self):

        return self.all_cards.pop(0)


# Player class definition (TBD)

class Player():

    def __init__(self, name):
        self.name = name
        self.cash = 25
        self.pool = 0
        self.all_cards = []
        self.bust = False
        self.value = 0

    def remove_all(self):
        
        for x in self.all_cards:
            self.all_cards.pop(0)

    def value_calculator(self):
        
        for x in self.all_cards:
            if x.rank == 'Ace':
                if self.value + 11 < 21:
                    self.value += 11
                else:
                    self.value += 1
            self.value += x.value
        if self.value > 21:
            self.bust = True
            
    def value_clear(self):
        
        self.all_cards = []
        self.value = 0
        self.pool = 0
        self.bust = False
        
    def hit_clear(self):
        
        self.value = 0
        
    def buy_in(self):
        
        self.cash -= 5
        self.pool = 5
        
    def collect_winnings(self):
        
        self.cash += self.pool * 2 
        
    
            