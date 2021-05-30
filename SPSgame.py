import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

Choices = ["SCISSORS","PAPER","STONE"]
computer_choice = random.choice(Choices)
x = z = 0
player_point = x
computer_point = z

game_over = False
while game_over == False:
    for i in range(10):
        player_choice = input("Press '1' for SCISSORS\nPress '2' for PAPER\nPress '3' for STONE\n: ")
        print("")
        computer_choice = random.choice(["SCISSORS","PAPER","STONE"])

        if player_choice == str(1):
            if computer_choice == Choices[0]:
                print("****************************************************")
                print("")
                print(Fore.YELLOW + "Its a TIE\nComputer chose {}".format(Choices[2]))
                print("Player score = {}".format(player_point))
                print("Computer score = {}".format(computer_point))
                print("")
                print("****************************************************")

            elif computer_choice == Choices[1]:
                print("****************************************************")
                print("")
                print(Fore.GREEN + "Player wins\nComputer chose {}".format(Choices[0]))
                player_point = player_point + 1
                print("Player score = {}".format(player_point))
                print("Computer score = {}".format(computer_point))
                print("")
                print("****************************************************")

            elif computer_choice == Choices[2]:
                print("****************************************************")
                print("")
                print(Fore.RED + "Player loses\nComputer chose {}".format(Choices[1]))
                computer_point += 1
                print("Player score = {}".format(player_point))
                print("Computer score = {}".format(computer_point))
                print("")
                print("****************************************************")

        elif player_choice == str(2):
            if computer_choice == Choices[0]:
                print("****************************************************")
                print("")
                print(Fore.RED + "Player loses\nComputer chose {}".format(Choices[1]))
                computer_point += 1
                print("Player score = {}".format(player_point))
                print("Computer score = {}".format(computer_point))
                print("")
                print("****************************************************")

            elif computer_choice == Choices[1]:
                print("****************************************************")
                print("")
                print(Fore.YELLOW + "Its a TIE\nComputer chose {}".format(Choices[2]))
                print("Player score = {}".format(player_point))
                print("Computer score = {}".format(computer_point))
                print("")
                print("****************************************************")

            elif computer_choice == Choices[2]:
                print("****************************************************")
                print("")
                print(Fore.GREEN + "Player wins\nComputer chose {}".format(Choices[0]))
                player_point += 1    
                print("Player score = {}".format(player_point))
                print("Computer score = {}".format(computer_point))
                print("")
                print("****************************************************")

        elif player_choice == str(3):
            if computer_choice == Choices[0]:
                print("****************************************************")
                print("")
                print(Fore.GREEN + "Player wins\nComputer chose {}".format(Choices[0]))
                player_point += 1
                print("Player score = {}".format(player_point))
                print("Computer score = {}".format(computer_point))
                print("")
                print("****************************************************")
            elif computer_choice == Choices[1]:
                print("****************************************************")
                print("")
                print(Fore.RED + "Player loses\nComputer chose {}".format(Choices[1]))
                computer_point += 1
                print("Player score = {}".format(player_point))
                print("Computer score = {}".format(computer_point))
                print("")
                print("****************************************************")
                
            elif computer_choice == Choices[2]:
                print("****************************************************")
                print("")
                print(Fore.YELLOW + "Its a TIE\nComputer chose {}".format(Choices[2]))
                print("Player score = {}".format(player_point))
                print("Computer score = {}".format(computer_point))
                print("")
                print("****************************************************")

        else:
            print("Please select a valid number")

        playAgain = input("Press to play again (Y/N): ")
        if playAgain == "n" or playAgain == "No":
            exit()
        else:
            continue
            
