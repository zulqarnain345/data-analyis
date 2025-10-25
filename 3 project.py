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
fig,axes=plt.subplots(1,2,figsize=(12,5))
for team,group in df.groupby("Team"):
    axes[0].plot(group["Player"],group['Goals'],marker="o",label=team)
axes[0].set_title("performance on the bases of goals")
axes[0].grid(True,alpha=0.5,linestyle="--") 
axes[0].legend()
axes[0].set_xlabel("Player")
axes[0].set_ylabel("GOals")   

for team,group in df.groupby("Team"):
    plt.plot(group['Player'],group['Matches_Played'],marker='o')
axes[1].set_title("performance on the bases of Matches played")
axes[1].grid(True,alpha=0.5,linestyle="--") 
axes[1].legend()
axes[1].set_xlabel("Player")
axes[1].set_ylabel("GOals")   
# adjust layout
plt.tight_layout()
plt.show()

# player with the most assists

for team,group in df.groupby("Team"):
    top_assists=df.loc[group["Assists"].idxmax(),"Player"]
    top_A=group["Assists"].max()
    print(f"the top assists in {team} in {top_assists} in {top_A}")


# Performance
def performance22(goals):
    if(goals>=8):
        return "Star Player"
    elif (goals>=5 and goals<8):
        return "Key Player"
    else:
        return "Average Player" 

df["Performance"]=df["Goals"].apply(performance22)


# sort by the team A first and team B 

sort=df.sort_values(by="Team",ascending=True)

# update bar chart of sort players by name 
colors=["red" if team=="Team A" else "Green" for team in sort["Team"]]
plt.bar(sort["Player"],sort["Goals"],color=colors,label="Team")
plt.axhline(sort["Goals"].mean(),linestyle="--",linewidth=2,label="average",color="black")
plt.legend()
plt.grid(True,alpha=0.5,linestyle="--")
plt.xlabel("Player")
plt.ylabel("Goals")
plt.title("update chart with sort team A and Team B")
plt.show()

# Calculate Goal Contribution

Goal_contribution=(df['Goals'] + df['Assists']) /(df['Matches_Played'] * 100)
df['Goal_contribustion']=Goal_contribution

# top 3 players overall in both teams

top_3=df.nlargest(3,"Goals")
print(f"\nTop 3 in both teams is \n{top_3}")

# bar chart of top 3 Players
colors=["red" if team=="Team A" else "green" for team in top_3["Team"]]
plt.bar(top_3["Player"],top_3["Goals"],color=colors,label=team)
plt.axhline(top_3["Goals"].mean(),linestyle="--",linewidth=2,color="black")
plt.legend()
plt.grid(True,alpha=0.5,linestyle="--")
plt.xlabel("Players")
plt.ylabel("Goals")
plt.title("TOP 3 PLayers")
plt.show()

# find discipline score = Yellow_Cards + 2 * Red_Cards

discipline_score=df['Yellow_Cards']+(2*df["Red_Cards"])
sort["Discipline_Score"]=discipline_score

print("\n",sort)

# 1. Find Top Scorer per Team with Rank
sort["top3_rank"]=sort.groupby("Team")['Goals'].rank(ascending=False)
top3_per_team = sort[sort['top3_rank'] <= 3]
print(top3_per_team)

# bar chart
colors=['red' if team=="Team A" else "green" for team in df["Team"]]
plt.bar(top3_per_team["Player"],top3_per_team["top3_rank"],color=colors,label=team)
plt.legend()
plt.grid(True,alpha=0.5,linestyle="--")
plt.xlabel("Player")
plt.ylabel("Goals")
plt.show()

# pie chart of performance
performance_count=df['Performance'].value_counts()
plt.pie(performance_count,autopct="%1.1f%%",startangle=90,labels=performance_count.index)
plt.title("Performance chart of the Bothe teams")
plt.tight_layout()
plt.axis("equal")

plt.show()
# updated DataFrame
df.to_csv("update.csv",index=False)
print("\nupdate the data!!")

