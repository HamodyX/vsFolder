import datetime
import os
import time

food = ['banana', 'apple', 'cherry']

hour = datetime.datetime.now().hour

def GameOver():
    if tries == max_tries:
        print("you lost, game over")

def clear_screen():
    os.system('cls' if os.name == "nt" else'clear')

max_tries = 3
tries = 0


if hour == 12:
    max_tries = float('inf')
    OutOF = "infinity"
else:
    OutOF = max_tries



while tries < max_tries:
    question = ("whats is your favorate food", food)
    answer = input(question)

    if answer in food:
        if answer == "banana":
            print("your answer is", answer, "and its correct")
            break
        if answer == "cherry":
            print
    else:
        print("undefined you lose one try")

    tries += 1
    print(tries,'/',OutOF,"try's used")

if tries == max_tries:
    GameOver()
    time.sleep(2)
    clear_screen()
