import pandas as pd

df = pd.read_csv("data set of performance.csv")

print(df.head())  # show first 5 rows

print("Unique Teams:")
print(df["Team"].unique())

print("\nPlayers per Team:")
print(df["Team"].value_counts())

teams = {name: data for name, data in df.groupby("Team")}
print(teams)
