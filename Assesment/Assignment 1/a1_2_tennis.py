"""
CP1401 2024 TR3 Assignment 1
Program 2 – Tennis Results
Student Name: Md Shafiur Rahman Diganta
Date started: 28 / 10 / 2024
Pseudocode:

GREETING_THRESHOLD = 8

get player_1_score, player_2_score

if player_1_score > player_2_score
    display "You won! :)"

else if player_1_score < player_2_score
    display "You lost! :( Keep trying."
else
    display "It's a draw."

if player_1_score + player_2_score >=  GREETING_THRESHOLD
        display Congratulations on playing a fast match!
"""

GREETING_THRESHOLD = 8

print("Welcome Player 1. How was your match?")
player_1_score = int(input("Your Score: "))
player_2_score = int(input("Opponent Score: "))

if player_1_score > player_2_score:
    print("You won! :)")

elif player_1_score < player_2_score:
    print("You lost! :( Keep trying.")
else:
    print("It's a draw.")

if player_1_score + player_2_score >=  GREETING_THRESHOLD:
        print("Congratulations on playing a fast match!")