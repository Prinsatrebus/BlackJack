import Variables
import time

stack_value = 0

# Game Setup

game_start = input("Would you like to play?")
print('\n')
game_start = game_start.upper()
if game_start == "N" or game_start == "NO":
    exit()
else:
    game_on = True

print("Building deck...")
game_deck = Variables.Deck()

print('\n')
print("Shuffling deck...")
game_deck.shuffle()

dealer = Variables.Player('Dealer')
player_one = Variables.Player('One')

print('\n')
game_start = input("Are you ready to start?")
game_start = game_start.upper()
if game_start == "N" or game_start == "NO":
    exit()

# Game Logic

while game_on:

    player_hit = ''
    dealer_hit = ''

    print('\n')
    print('The dealer has dealt cards!')

    if player_hit != 'STAND':
        player_one.all_cards.append(game_deck.deal_one())
    if dealer_hit != 'STAND':
        dealer.all_cards.append(game_deck.deal_one())
    if player_hit = 'STAND' and dealer_hit = 'STAND':
        Variables.stack_value_calculate(dealer.all_cards, player_one.all_cards)        

    print('\n')
    print('Dealer')
    print('---------------------')
    print(*dealer.all_cards, sep='\n')
    print('---------------------')
    print('\n')

    print('\n')
    print('Player One')
    print('---------------------')
    print(*player_one.all_cards, sep='\n')
    print('---------------------')
    print('\n')

    while hit != "HIT" and hit != "STAND":
        print('\n')
        hit = input("Hit or Stand?")
        hit = hit.upper()

        if hit == "HIT":
            print('\n')
            print(f'The dealer has dealt {game_deck.all_cards[0]}')
            card_stack.append(game_deck.deal_one())

            print('\n')
            print("Cards currently on the table:")
            print('\n')
            print(*card_stack, sep='\n')

            Variables.stack_value_calculate(card_stack)

        elif hit == "STAND":
            print('\n')
            print("filler text")
            exit()


