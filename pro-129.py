
import pandas as pd

data = pd.read_csv("Final_Final.csv")


del data["Star_name"]


data = data.dropna()


data.to_csv("Data.csv")