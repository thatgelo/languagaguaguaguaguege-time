import pandas as pd
import numpy as np
import random
import io

### languages = pd.read_csv(r"C:\Users\kamag\OneDrive\Desktop\languagetime\languagaguaguaguaguege-time\Languages.csv")
url = 'https://raw.githubusercontent.com/forxer/languages-list/master/src/Languages.csv'

languages = pd.read_csv(url)

language_names = languages.iloc[:, 3].array
native_scripts = languages.iloc[:, 4].array

def generate_random_number(start, stop):
    random_num = random.randint(start, stop)
    return random_num
 
def display_hint(random_number_generated):
    print(native_scripts[random_number_generated])

def correct_answer(random_number):
    correct = language_names[random_number]
    return correct

def guessing_game(score):
    game_state = True
    while game_state:
        random_number = generate_random_number(0, 184)
        display_hint(random_number)
        language_answer = correct_answer(random_number)
        user_answer = input()
        if user_answer.strip().lower() == language_answer.strip().lower():
            print("You got it!")
            score += 1
            game_state = False
        elif user_answer.strip().lower() == "no":
            print("the answer was " + language_answer)
            game_state = False    
        elif user_answer.strip().lower() != language_answer.strip().lower():
            print("you suck")
    play_again = "y"
    dont_play = "n"
    print("play again? [y]es or [n]o?")
    choice = input().strip().lower()
    if choice == play_again:
        guessing_game(score)
    elif choice == dont_play:
        print("thank u for playing! your score is: " + str(score))
        


guessing_game(0)
