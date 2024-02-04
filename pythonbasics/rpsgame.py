#!/usr/bin/python3

import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Rock, paper or scissors?: ").lower()

    if player == computer:
        print("Computer: ", computer)
        print("Player: ", player)
        print("Tie!")

    elif player == "rock":
        if computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You lose!")
        if computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win!")
    
    elif player == "scissors":
        if computer == "paper":
                print("Computer: ", computer)
                print("Player: ", player)
                print("You win!")
        if computer == "rock":
                print("Computer: ", computer)
                print("Player: ", player)
                print("You lose!")
    
    elif player == "paper":
        if computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You lose!")
        if computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win!")

# This is a simple rock, paper, scissors game. The computer will randomly choose rock, paper or scissors and the player will be prompted to choose one of the three.
# The game will then determine the winner. The game will continue to run until the user decides to quit.
# Implement play again option, score tracker, and error handling and exit game option.