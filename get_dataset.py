import pandas as pd
URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
pd.read_csv(URL).to_csv("titanic.csv", index=False)
print("Saved titanic.csv")
