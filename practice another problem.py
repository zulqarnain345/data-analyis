import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("second.csv")
print(df,'\n')

# separating two groups
teamA=df[df['Team']=="Team A"]
teamB=df[df['Team']=="Team B"]
teamA.index=teamA.index + 1
teamB=teamB.reset_index(drop=True)
teamB.index=teamB.index + 1
print(f"the team A is\n{teamA}\n")
print(f"the team B is\n{teamB}\n")

# total runs in each team

total_run=df.groupby("Team")['Runs'].sum()
print(total_run)

if total_run['Team A']>total_run['Team B']:
    winner='Team A'
elif total_run['Team B']>total_run['Team A']:
    winner='Team B'

else:
    winner='Draw!!'
print(f"\nthe Winner!! team is {winner}")      

# top player in team A
top=df.groupby("Player")['Runs'].sum().idxmax()
print(f"\nthe highest score in both team:: {top}")

# separately both team highest score by the player is

for team,group in df.groupby("Team"):
    top1=group.loc[group['Runs'].idxmax(),"Player"]
    top2=group['Runs'].max()
    print(f"the player in {team} high score by {top1} with runs {top2}\n")


# balls played by both team 

total_ball=df.groupby("Team")['Balls'].sum()
print(f"The total balls played by the {total_ball}\n")

#total Fours 
total_fours=df.groupby("Team")['Fours'].sum()
print(f"The total fours by the eacg team is {total_fours}\n")

# total sixs
total_six=df.groupby("Team")['Sixes'].sum()
print(f"The sixes by the both team is{total_six}\n")

# how  fours 

for team,group in df.groupby("Team"):
    top_four=group.loc[group['Fours'].idxmax(),"Player"]
    top_score=group['Fours'].max()
    print(f"the highes fours by {top_four} is {top_score}0")

#which score most sixes
print("\n")
for team,group in df.groupby("Team"):
    top_player=group.loc[group['Sixes'].idxmax(),"Player"]
    top_score2=group["Sixes"].max()
    print(f"the most sixes by {top_player} is {top_score2}") 
# print(df)
# bar chart which 
colors=['red' if team=="Team A" else "green" for team in df["Team"]]

plt.bar(df['Player'],df['Runs'],color=colors)
plt.axhline(df['Runs'].mean(),linestyle="--",linewidth=2,color="black",label="Team")
plt.xlabel("Players")
plt.ylabel("Runs")
plt.title("CHART OF BOTH TEAM SCORE PLAYERS RUNS")
plt.legend()
plt.grid(True,linestyle='--',alpha=0.5)
plt.show()


# line chart of each player is
for team,group in df.groupby("Team"):
    plt.plot(group['Player'],group["Runs"],marker='o',label="Team")
plt.xlabel("Player")
plt.ylabel("Runs")
plt.title("Performance by the runs")
plt.legend()
plt.grid(True,linestyle='--',alpha=0.5)
plt.show()

for team,group in df.groupby("Team"):
    plt.plot(group["Player"],group["Balls"],marker="o",label="Team")
plt.xlabel("Player")
plt.ylabel("Balls")
plt.title("Performance by the Balls")
plt.legend()
plt.grid(True,linestyle='--',alpha=0.5)
plt.show()    


for team,group in df.groupby("Team"):
    plt.plot(group['Player'],group['Fours'],marker='o',label="Team")

plt.xlabel("Player")
plt.ylabel("Fours")
plt.title("Performance by the Fours")
plt.legend()
plt.grid(True,linestyle='--',alpha=0.5)
plt.show()

for team,group in df.groupby("Team"):
    plt.plot(group['Player'],group['Sixes'],marker="o",label=team)
plt.xlabel("Player")
plt.ylabel("Sixes")
plt.title("Performance by Sixes")
plt.legend()
plt.grid(True,linestyle='--',alpha=0.5)
plt.show()


# pie chart 
plt.pie(total_run,labels=total_run.index,autopct="%1.1f%%",startangle=90)
plt.title("chart represent ")
plt.tight_layout()
plt.axis("equal")
plt.show()