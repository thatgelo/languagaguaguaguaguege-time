import pandas as pd
import numpy as np
import random
import io

url = 'https://raw.githubusercontent.com/forxer/languages-list/master/src/Languages.csv'

languages = pd.read_csv(url)

language_names = languages.iloc[:, 3].array
native_scripts = languages.iloc[:, 4].array

def generate_random_number(start, stop):
    random_num = random.randint(start, stop)
    return random_num
 
def display_hint(random_number_generated):
    print("the native script is: " + native_scripts[random_number_generated])

def correct_answer(random_number):
    correct = language_names[random_number]
    return correct

def guessing_game(score):
    game_state = True
    correct_guesses = []
    incorrect_guesses = []
    while game_state:
        random_number = generate_random_number(0, len(language_names) - 1)
        display_hint(random_number)
        language_answer = correct_answer(random_number)
        user_answer = input()
        if user_answer.strip().lower() == language_answer.strip().lower():
            print("You got it!")
            correct_guesses.append(language_answer)
            score += 1
        elif user_answer.strip().lower() == "no":
            print("the answer was " + language_answer)
            incorrect_guesses.append(language_answer)
            game_state = False    
        elif user_answer.strip().lower() != language_answer.strip().lower():
            print("nice try, the language is " + str(language_answer))
            incorrect_guesses.append(language_answer)
    play_again = "y"
    dont_play = "n"
    ### something wrong here, check scores mayhaps
    print("game over :D you got " + str(score) + " correct so far! do you want to play again? [y]es or [n]o?")
    choice = input().strip().lower()
    if choice == play_again:
        guessing_game(score)
    elif choice == dont_play:
        print("thank u for playing! your score is: " + str(score) + " and you got " + str(len(incorrect_guesses)) + " wrong!")
        print(incorrect_guesses)
        


guessing_game(0)
