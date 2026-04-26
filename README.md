# Rock Paper Scissor Game (Python CLI)

This is a simple command line based game written in python where a player can play Rock Paper Scissor against the computer (bot). The game runs in loop and keeps track of score until the user decides to exit.

## About the game

The player has to choose between three options:

* rock
* paper
* scissor

At the same time, the bot randomly selects one of these options. Based on the rules of the game, winner is decided and points are updated.

## Rules

* Rock beats Scissor
* Scissor beats Paper
* Paper beats Rock
* If both choose same then it is a draw

## Features

* Simple CLI interface
* Random bot choice using python random module
* Score tracking for both player and bot
* Exit option anytime during the game
* ASCII art welcome banner using art library

## How to run

1. Make sure python is installed on your system

2. Install the required library:

   pip install art
   pip install random

3. Run the script:

   python filename.py

## How to play

* When the game starts, you will see a welcome banner
* Enter your choice when prompted
* Valid inputs are: rock, paper, scissor
* To quit the game, type: exit or bye

## Notes

* Input is not case sensitive
* If wrong input is given, game will ask again
* Scores are shown after every round

## Future improvements (optional)

* Can add GUI version
* Can improve input validation
* Can add best of 3 or best of 5 mode
* Sound effects can also be added

## Author

Sanju

This is a basic project but good for learning python loops, conditions and user input handling.
