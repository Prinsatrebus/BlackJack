
#variables for card values

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


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

# card stack value calculating function

def stack_value_calculate(card_stack):

    global stack_value
    stack_value = 0

    for x in card_stack:
        stack_value += x.value
    
    print(f'{stack_value}')


# Player class definition (TBD)