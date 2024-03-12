import random

def coin_toss():
    return random.randint(0, 1)

def play_game():
    computer_bet = 0
    player_bet = 1
    
    # computer plays:
    coin_val = coin_toss()

    # player plays
    if coin_val == computer_bet: 
        coin_val = coin_toss()

        #computer plays
        if coin_val == player_bet:
            coin_val = coin_toss()
    
    return coin_val

n = 0
for _ in range(1000000):
    val = play_game()
    n += val

print(n)