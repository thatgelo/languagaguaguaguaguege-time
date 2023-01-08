import pandas as pd
import numpy as np

languages = pd.read_csv(r"C:\Users\kamag\OneDrive\Desktop\languagetime\languagaguaguaguaguege-time\Languages.csv")
names = languages.iloc[:, 3]
print(names)