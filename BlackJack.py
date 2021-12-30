import Variables
import time

stack_value = 0

# Game Setup

game_start = input("Would you like to play?")
game_start = game_start.upper()
if game_start == "N" or game_start == "NO":
    exit()
else:
    game_on = True

print("Building deck...")
game_deck = Variables.Deck()

print("Shuffling deck...")
game_deck.shuffle()

game_start = input("Are you ready to start?")
game_start = game_start.upper()
if game_start == "N" or game_start == "NO":
    exit()

# Game Logic

card_stack = []
hit = ''

print(f'The dealer has dealt {game_deck.all_cards[0]}')

card_stack.append(game_deck.deal_one())
while game_on:

    hit = ''

    while hit != "HIT" and hit != "STAND":
        hit = input("Hit or Stand?")
        hit = hit.upper()

        if hit == "HIT":
            print(f'The dealer has dealt {game_deck.all_cards[0]}')
            card_stack.append(game_deck.deal_one())

            print("Cards currently on the table:")
            print(*card_stack, sep='\n')

            Variables.stack_value_calculate(card_stack)

            if stack_value == 21:
                print("Blackjack!")
                print("Thanks for playing!")
                exit()
            elif stack_value < 21:
                break
            elif stack_value > 21:
                print("Bust!")
                print("Thanks for playing!")
                exit()
        elif hit == "STAND":
            print("filler text")
            exit()


