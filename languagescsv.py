import pandas as pd
import numpy as np
import io

### languages = pd.read_csv(r"C:\Users\kamag\OneDrive\Desktop\languagetime\languagaguaguaguaguege-time\Languages.csv")
url = 'https://raw.githubusercontent.com/forxer/languages-list/master/src/Languages.csv'

languages = pd.read_csv(url)

language_names = languages.iloc[:, 3].array
native_scripts = languages.iloc[:, 4].array
print(language_names)
print(native_scripts)