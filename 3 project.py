import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("data.csv")

# separete by team 

TeamA=df[df['Team']=='Team A']
TeamB=df[df['Team']=='Team B']
TeamA.index=TeamA.index + 1
TeamB=TeamB.reset_index(drop=True)
TeamB.index=TeamB.index+1

print(TeamA)
print(TeamB)

# total goal

total_goal=df.groupby("Team")['Goals'].sum()
print(f"\nthe total goal by the both team is {total_goal}")


if total_goal["Team A"] > total_goal['Team B']:
    winner="Team A"
elif total_goal['Team B'] > total_goal["Team A"]:
    winner="Team B"
else:
    winner="draw!!"

print(f"\nThe team {winner} is win!!!!\n")

# top scorer in each team.

for team,group in df.groupby("Team"):
    # average by both team is 
    avg=group["Goals"].mean().round(2)
    print(f"the average of {team} is {avg}")
    top_player=group.loc[group['Goals'].idxmax(),'Player']
    top_score=group["Goals"].max()
    print(f"the player how score in {team} is {top_player} by {top_score}")



# Plot a bar chart showing player-wise goals:

colors=['red' if team=='Team A' else "green" for team in df["Team"]]
plt.bar(df["Player"],df["Goals"],color=colors,label=team)
plt.axhline(df['Goals'].mean().round(2),color="black",label="average",linewidth=2,linestyle="--")
plt.title("bar char shows player wise goals ")
plt.xlabel("GOals")
plt.ylabel("pLayer")
plt.grid(True,alpha=0.5,linestyle="--")
plt.legend()
plt.show()

# Plot a line chart comparing player-wise assists of both teams.
for team,group in df.groupby("Team"):
    plt.plot(group["Player"],group['Goals'],marker="o",label=team)
plt.title("performance on the bases of goals")
plt.grid(True,alpha=0.5,linestyle="--") 
plt.legend()
plt.xlabel("Player")
plt.ylabel("GOals")   
plt.show()


for team,group in df.groupby("Team"):
    plt.plot(group['Player'],group['Matches_Played'],marker='o')
plt.title("performance on the bases of Matches played")
plt.grid(True,alpha=0.5,linestyle="--") 
plt.legend()
plt.xlabel("Player")
plt.ylabel("GOals")   
plt.show()

# player with the most assists

for team,group in df.groupby("Team"):
    top_assists=df.loc[group["Assists"].idxmax(),"Player"]
    top_A=group["Assists"].max()
    print(f"the top assists in {team} in {top_assists} in {top_A}")


# Performance

if(df["Goals"]>=8):
    Performance="Star Player"
elif (df["Goals"]>=5 and df["Goals"]<8):
    Performance="Key Player"
else:
    Performance="Average Player" 

df["Performance"]=Performance
print(df)       

