import pandas as pd
import numpy as np
import random
import io

### languages = pd.read_csv(r"C:\Users\kamag\OneDrive\Desktop\languagetime\languagaguaguaguaguege-time\Languages.csv")
url = 'https://raw.githubusercontent.com/forxer/languages-list/master/src/Languages.csv'

languages = pd.read_csv(url)

language_names = languages.iloc[:, 3].array
native_scripts = languages.iloc[:, 4].array

print(language_names)
print(native_scripts)


def answer():
    randomized_number = random.randint(0, 185)
    correct_answer = language_names[randomized_number]
    displayed_hint = native_scripts[randomized_number]
    print(displayed_hint)
    user_answer = input()
    while user_answer.strip().lower() != correct_answer.strip().lower():
        print("bad try again")
        user_answer = input()
        if user_answer == "i hate this game":
            answer()
    print("asdlkfasjf")
    

answer()