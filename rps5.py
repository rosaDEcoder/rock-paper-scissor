import sys
import random
from enum import Enum

def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input("\nenter...\n1 for rock, \n2 for paper, or \n3 for scissor:\n\n")

        if playerchoice not in ["1","2","3"]:
            print("you must enter 1,2, or 3.")
            play_rps()
            
        player = int(playerchoice)

            
        computerchoice = random.randint(1,3)

        computer = int(computerchoice)


        print("\n you chose " + str(RPS(player)).replace('RPS.','') + ".")
        print(" python chose " + str(RPS(computer)).replace('RPS.','') + ".")
        print("")

        def decide_winner(player,computer):
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer ==3:
                player_wins += 1
                return " YOU WIN, MY HONEYBUN🙌🍾🥂🥳!"
            elif player == 2 and computer ==1:
                player_wins += 1
                return " YOU WIN, MY HONEYBUN 🙌🍾🥂🥳 !"
            elif player == 1 and computer ==3:
                player_wins += 1
                return " YOU WIN, MY HONEYBUN 🙌🍾🥂🥳!"
            elif player == computer:
                return " IT'S A TIE, MY SWEETIE🤜🤛!"
            else:
                python_wins += 1 
                return "PYTHON WINS!, NEXT TIME DARLING 😎😏"

        game_result = decide_winner(player,computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print("\nGame count:" + str(game_count))
        print("player wins:" + str(player_wins))
        print("python wins:" + str(python_wins))

        print("\nLET'S PLAY AGAIN!!!!")

        while True:

            playagain = input("\nY FOR YES or\nQ TO QUIT\n")
            if playagain.lower() not in ["y" , "q"]:
             continue
            else:
                break

        if playagain.lower( )=="y":
            play_rps()
        else:
            print("\n🙌🍾🥂")
            print("thank you for playing!!!!!!!!!!\n")
            playagain = False
            sys.exit("bye pookie💋")

    return play_rps()

play = rps()

play()