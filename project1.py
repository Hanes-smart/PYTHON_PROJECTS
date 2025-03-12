import random

def roll():
    min_value=1
    max_value=6
    roll = random.randint(min_value,max_value)
    return roll
value =roll()


while True:
    players=input("Enter the no players (2-4): ")
    if players.isdigit(): # checks if a str contains digits
        players=int(players)  ## changing str to int
        if 2<= players <=4:
           break
        else:
            print("Must be between (1-4) ")
    else:
        print("Invalid,try again")

max_score =50
players_score = [0 for _ in range(players)]

while max(players_score)<max_score:
    for player_idx in range(players):
        print("\nplayer",player_idx+1,"turn has just has started\n")
        print("Your total score",players_score[player_idx])
        current_score =0
        while True:
            should_roll =input("Would u like to roll(y)?")
            if should_roll.lower() != "y": # if Y changes to lower case
                break

            value =roll() # stats to roll
            if value ==1:
                print("You are 1,turn done")
                break
            else:
                current_score += value
                print("You rolled",current_score)

            print("The current score",current_score)
        players_score[player_idx] +=current_score
        print("your total score:",players_score[player_idx])

max_score =max(players_score)
winner_idx = players_score.index(max_score)
print("player number",winner_idx+1,"is the winner with the score of:",max_score)
