# simple
import random
from random import randint

# moves of the player:
moves = ["rock", "paper", "scissor"]

while True:
    computer = moves[randint(0, 2)]
    player = input("rock, paper or scissor (or end the game)").lower()
    if player == "end the game":
        print("the game has ended.")
        break
    elif player == computer:
        print("it's a tie")
    
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "beats", player)
        else:
            print("You win!", player, "beats", computer)

    elif player == "paper":
        if computer == "scissor":
            print("You lose!", computer, "beats", player) 
        else:
            print("You won!", player, "beats", computer)

    elif player == "scissor":
        if computer == "rock":
            print("You lose!", computer, "beats", player) 
        else:
            print("You won!", player, "beats", computer)

    else:
        print("check the spelling")      


