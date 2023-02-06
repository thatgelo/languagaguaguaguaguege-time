# -*- coding: utf-8 -*-

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
    # print("randnumgend: " + str(random_number_generated))
    # print("nativescripts[randnumgend]: " + str(native_scripts[random_number_generated]))
    # print("utf-8 encoded: " + str((native_scripts[random_number_generated]).encode("utf-8")))
    print("Guess the English name for the following language. The native script is: " 
          + str(native_scripts[random_number_generated]))

def correct_answer(random_number):
    correct = language_names[random_number]
    return correct

def guessing_game(score):
    
    game_state = True
    correct_guesses = []
    incorrect_guesses = []
    
    # want to stop showing languages that were gotten correct already
    
    while game_state:
        
        random_number = generate_random_number(0, len(language_names) - 1)
        # print("randnum: " + str(random_number))
        
        if native_scripts[random_number] not in correct_guesses: 
            display_hint(random_number)
            language_answer = correct_answer(random_number)
            user_answer = input()
            
            if user_answer.strip().lower() in language_answer.strip().lower():
                print("You got it!\n\n")
                correct_guesses.append(language_answer)
                score += 1
                
            elif user_answer.strip().lower() == "no":
                print("The answer was " + language_answer + "\n\n")
                incorrect_guesses.append(language_answer)
                game_state = False    
                
            elif user_answer.strip().lower() not in language_answer.strip().lower():
                print("Nice try, the language is " + str(language_answer) + "\n\n")
                incorrect_guesses.append(language_answer)
            
    play_again = "y"
    dont_play = "n"
    
    ### something wrong here, check scores mayhaps
    print("Game over D: You got " + str(score) + " correct so far! Do you want to play again? [y]es or [n]o?")
    choice = input().strip().lower()
    if play_again in choice:
        guessing_game(score)
<<<<<<< HEAD
    elif choice == dont_play:
        print("thank u for playing! your score is: " + str(score) + " and you got " + str(len(incorrect_guesses)) + " wrong!")
        print("you got these languages correct: " + str(correct_guesses))
        print("the ones u got wrong were: " + str(incorrect_guesses))
    
=======
    elif dont_play in choice:
        print("Thank you for playing! Your score is: " + str(score) + " and you got " + str(len(incorrect_guesses)) + " wrong!")
        print(incorrect_guesses)
>>>>>>> a401cc862d751abd6ee7460900a9473036c7375c
        


guessing_game(0)
