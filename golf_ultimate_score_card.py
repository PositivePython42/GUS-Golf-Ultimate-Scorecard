"""
Golf's Ultimate ScoreCard app, written by Sean Massey,
Built on Python 3.11, in Thonny
Version 0.1
Full Details in the GitHub Repo, github.com/PositivePython42/Golf-Ultimate-Score-Card
Raise issues and feature requests at https://github.com/PositivePython42/Golf-Ultimate-Score-Card/issues
"""

import sys, gusc_courses, gusc_players


max_number_of_players = 4
number_of_players = 5
course_holes = 18
maximum_handicap = 36
valid_game = False

def make_player_list(n):  
    players = ['player{}'.format(i) for i in range(1, n + 1)]
    return players

def record_gross(h, p, cs):
    player_variable = "gusc_players.player"+str(p)+"_scorecard"
    hole_variable = "h"+str(h)+"gross"
    player_variable[hole_variable] = cs
    
# Main Programe
print("Welcome To GUS Golf's Ultimate Scorecard!\nYou can score all known golf game formats and even run a private golf league or run a competition!")

# Chose the format for play
print("\nChose today's game format.\n1. Medal\n2. Stableford\n\nQ. Quit")
while valid_game == False:
    game_format = input()
    if game_format == "q" or game_format == "Q":
        sys.exit("Thanks for using Golf's Ultimate Score Card App, come back soon.")
    elif int(game_format) <1 or int(game_format) >2:
        print("Please chose a number between 1 and 2")
        continue
    else:
        break 

#chose the number of players in the game
while number_of_players > max_number_of_players:
    number_of_players = int(input("\nHow many players are in the game? : "))
    if number_of_players > max_number_of_players:
        print("Maximum 4 players please")
    #else:
        #players = make_player_list(number_of_players)
    
#main medal scorecard loop
for hole in range(1, course_holes+1, 1):
    for player in range(1, number_of_players+1):
        current_score = input(f"Enter {player} score on hole {hole} : ")
        record_gross(hole, player, current_score) #TRY HAVING THE VARIABLES IN THIS FILE NEXT
        #record_nett(hole, player, current_score)

print_scorecard()
