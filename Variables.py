
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

# card stack value calculating function

def stack_value_calculate(dealer, player_one):

    dealer_value = 0
    player_one_value = 0


    for x in dealer:
        if x.rank == 'Ace':
            if dealer_value + 10 < 21:
                dealer_value += 10
            else:
                dealer_value += 1
        dealer_value += x.value
    
    print('\n')
    print(f'The dealer is at {dealer_value}')

    for x in player_one:
        if x.rank == 'Ace':
            if player_one_value + 10 < 21:
                player_one_value += 10
            else:
                player_one_value += 1
        player_one_value += x.value
    
    print('\n')
    print(f'Player One is at {player_one_value}')

    if dealer_value == player_one_value:
        print('Draw!')
    elif dealer_value > player_one_value:
        print("The dealer wins this round!")
        player_one.cash -= 5
        dealer.cash += 5
    else:
        print("Player One wins this round!")
        dealer.cash -= 5
        player_one.cash += 5
        


# Player class definition (TBD)

class Player():

    def __init__(self, name):
        self.name = name
        self.cash = 25
        self.all_cards = []

    def remove_all(self):
        
        for x in self.all_cards:
            self.all_cards.pop(0)

