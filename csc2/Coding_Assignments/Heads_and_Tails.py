####################################################################
####    Name:   Josephine Rei Sale                              ####
####    Date:   February 4th, 2022                              ####
####    Desc:   An easy way to simulate a game of probability   ####
####################################################################

from random import randint

num_games_ult = int (input("How many games? "))
num_coins_ult = int (input ("How many coin tosses per game? "))
wins = [0, 0, 0, 0]
game_num = 0
num_games = num_games_ult
while num_games > 0:
    game_num += 1
    num_games -= 1
    num_coins = num_coins_ult
    a_wins = 0
    b_wins = 0
    p_wins = 0
    while num_coins > 0:
        # 1 shall be heads and 0 shall be tails
        num_coins -= 1
        c_1 = randint (0, 1)
        c_2 = randint (0, 1)
        if c_1 == 1:
            if c_2 == 1:
                a_wins += 1
            else:
                p_wins += 1
        else:
            if c_2 == 1:
                p_wins += 1
            else:
                b_wins += 1
    if p_wins > a_wins and p_wins > b_wins:
        wins [2] += 1
    elif a_wins > b_wins and a_wins > p_wins:
        wins [0] += 1
    elif b_wins > a_wins and b_wins > p_wins:
        wins [1] += 1
    else:
        wins [3] += 1
        # I implimented a contengent plan for ties
    print (f"Game {game_num}:\nGroup A: {a_wins} ({round(a_wins/num_coins_ult * 100)}%)\tGroub B: {b_wins} ({round(b_wins/num_coins_ult * 100)}%)\t Professor: {p_wins} ({round(p_wins/num_coins_ult * 100)}%)")
print (f"Wins:\nGroup A: {wins [0]} ({round(wins [0]/num_games_ult * 100)}%)\tGroup B: {wins [1]} ({round(wins [1]/num_games_ult * 100)}%)\tProfessor: {wins [2]} ({round(wins [2]/num_games_ult * 100)}%)\tTies: {wins [3]} ({round(wins [3]/num_games_ult * 100)}%)")