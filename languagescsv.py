import pandas as pd
import numpy as np

languages = pd.read_csv(r"C:\Users\kamag\Downloads\Languages.csv")
language_names = languages[["Language"]]
print(language_names)