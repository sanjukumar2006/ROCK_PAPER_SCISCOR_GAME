import random as r
from art import *

object = ["rock","paper","scissor"]
user_point=0
bot_point=0
print(text2art("WELCOME TO GAME"))
print("═" * 55)
print("Player has to choose between: ROCK • PAPER • SCISSOR")
print("To quit type ----> Exit or Bye")
print("═" * 55)
print()
while True:

    bot_choice=r.choice(object)
    
    human_choice=input("enter your choice: ").lower()

    if human_choice=="exit" or human_choice=="bye":
        print("exiting, thankyou for playing")
        print(f"human point was:{user_point}")
        print(f"bot point was:{bot_point}")
        break

    print("the bot has choosen:",bot_choice)

    if bot_choice == human_choice:
        print("DRAW, no points to anyone")

    elif bot_choice != human_choice:
        if bot_choice=="scissor" and human_choice=="rock":
            user_point+=1
            print("you win, plus 1 point to human\nnow total point of both is\n","human point =",user_point,"\nbot point=",bot_point)
       
        elif bot_choice=="paper" and human_choice=="scissor":
            user_point+=1
            print("you win, plus 1 point to human\nnow total point of both is\n","human point =",user_point,"\nbot point=",bot_point)
        
        elif bot_choice=="rock" and human_choice=="paper":
            user_point+=1
            print("you win, plus 1 point to human\nnow total point of both is\n","human point =",user_point,"\nbot point=",bot_point)
        elif bot_choice=="paper" and human_choice=="rock":
            bot_point+=1
            print("you lose, plus 1 point to bot\nnow total point of both is\n","human point =",user_point,"\nbot point=",bot_point)
        elif bot_choice=="rock" and human_choice=="scissor":
            bot_point+=1
            print("you lose, plus 1 point to bot\nnow total point of both is\n","human point =",user_point,"\nbot point=",bot_point)
        elif bot_choice=="scissor" and human_choice=="paper":
            bot_point+=1
            print("you lose, plus 1 point to bot\nnow total point of both is\n","human point =",user_point,"\nbot point=",bot_point)
    
        else:
            print("wrong input, please choose from")
            print("rock")
            print("scissor")
            print("paper")



