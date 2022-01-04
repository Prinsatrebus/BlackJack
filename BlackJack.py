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
    perma = True

time.sleep(1)
print("Building deck...")
time.sleep(2)
game_deck = Variables.Deck()

print('\n')
print("Shuffling deck...")
time.sleep(2)
game_deck.shuffle()

dealer = Variables.Player('Dealer')
player_one = Variables.Player('One')

print('\n')
game_start = input("Are you ready to start?")
game_start = game_start.upper()
if game_start == "N" or game_start == "NO":
    exit()
    
time.sleep(1)

# Game Logic

# perma is always on until program ends; every iteration of perma displays cash, prize pools, and initial hands dealt

while perma:

    print('\n')
    time.sleep(1)
    
    print(f'Player one has ${player_one.cash} left.')
    time.sleep(1)
    print('\n')
    print(f'The dealer has ${dealer.cash} left.')
    print('\n')
    time.sleep(1)
    
    print("Buy in!")

    player_one.buy_in()
    dealer.buy_in()

    print('\n')
    time.sleep(1)
    print(f'Current prize pool: ${player_one.pool + dealer.pool}')
    
    print('\n')
    print('The dealer has dealt cards!')
    
    player_one.all_cards.append(game_deck.deal_one())
    player_one.all_cards.append(game_deck.deal_one())
    dealer.all_cards.append(game_deck.deal_one())
    dealer.all_cards.append(game_deck.deal_one())
    
    time.sleep(1)
    
    print('\n')
    print('Dealer')
    print('---------------------')
    print(*dealer.all_cards, sep='\n')
    print('---------------------')
    print('\n')
    
    time.sleep(1)

    print('\n')
    print('Player One')
    print('---------------------')
    print(*player_one.all_cards, sep='\n')
    print('---------------------')
    
# game_on is also permanently on until the program ends. It holds the while loop for every instance of dealing or not dealing cards, as well as determing bust
        

    while game_on:

        player_hit = ''
        dealer_hit = ''
        
        time.sleep(1)
        
        print('\n')
        player_hit = input("Hit or Stand?")
        player_hit = player_hit.upper()
        if player_hit != 'STAND':
            
            time.sleep(1)
            
            print('\n')
            print(f"Player one was dealt {game_deck.all_cards[0]}")
            player_one.all_cards.append(game_deck.deal_one())
            
            time.sleep(2)
            
            print('\n')
            print('Player One')
            print('---------------------')
            print(*player_one.all_cards, sep='\n')
            print('---------------------')
            print('\n')
            
            time.sleep(2)
            player_one.value_calculator()
            if player_one.bust == True:
                
                time.sleep(2)
                
                print("BUST!")
                
                time.sleep(2)
                
                dealer.collect_winnings()
                player_one.value_clear()
                dealer.value_clear()
                break
            player_one.hit_clear()
            
# Very simple conditional statement to determine if the dealer hits or stands

        dealer.value_calculator()
        if dealer.value < 14:
            
            dealer.hit_clear()
            
            time.sleep(2)
            
            print('\n')
            print("The dealer hits!")
            print('\n')
            dealer_hit = 'HIT'
        else:
            
            dealer.hit_clear()
            
            time.sleep(2)
            
            print('\n')
            print("The dealer stands!")
            print('\n')
            
            dealer_hit = 'STAND'
        if dealer_hit != 'STAND':
            
            time.sleep(2)
            
            print(f"Dealer was dealt {game_deck.all_cards[0]}")
            dealer.all_cards.append(game_deck.deal_one())
            
            time.sleep(2)
            
            print('\n')
            print('Dealer')
            print('---------------------')
            print(*dealer.all_cards, sep='\n')
            print('---------------------')
            print('\n')
            
            time.sleep(2)
            
            dealer.value_calculator()
            if dealer.bust == True:
                
                time.sleep(2)
                
                print('\n')
                print("Dealer has busted!")
                
                time.sleep(2)
                
                player_one.collect_winnings()
                player_one.value_clear()
                dealer.value_clear()
                break
            
# if neither the player nor the dealer has busted and both have decided to stand, the winner is determined by comparing hand values

        if player_hit == 'STAND' and dealer_hit == 'STAND':
            player_one.value_calculator()
            dealer.value_calculator()
            if player_one.value > dealer.value:
                
                time.sleep(2)
                
                print('\n')
                print("Player one has won this round!")
                
                time.sleep(2)
                
                player_one.collect_winnings()
                player_one.value_clear()
                dealer.value_clear()
                break
            elif player_one.value < dealer.value:
                
                time.sleep(2)
                
                print('\n')
                print("The dealer has won this round!")
                
                time.sleep(2)
                
                dealer.collect_winnings()
                player_one.value_clear()
                dealer.value_clear()
                break
            elif player_one.value == dealer.value:
                
                time.sleep(2)
                
                print('\n')
                print("Draw!")
                
                time.sleep(2)
                
                player_one.collect_winnings()
                dealer.collect_winnings()
                player_one.value_clear()
                dealer.value_clear()
                break



