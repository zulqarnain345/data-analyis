import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv("data set of performance.csv")

print(df.head(),"\n")  # show first 5 rows
# total number of teams
print(f"The total no Teams:: {df["Team"].nunique()}")
# total number of players
print(f"The total no Players in all teams:: {df["Player"].nunique()}")


# use describe quick overview of all numerical data
print(df.describe().round(2))

# Identify the player with the highest goals and highest assists.
for team,group in df.groupby("Team"):
    highest_goal=group.loc[group["Goals"].idxmax(),"Player"]
    top_score=group["Goals"].max()
    highest_assists=group.loc[group["Assists"].idxmax(),"Player"]
    top_scoreA=group["Assists"].max()
    # average goals per player
    avg=group["Goals"].mean().round(2)
print(f"\nThe average goal per player is:: {avg}")
print(f"PLAYER WITH THE HIGHEST GOAL DONE BY {highest_goal} WHICH SCORE {top_score}")
print(f"PLAYER WITH THE HIGHEST ASSISTS DONE BY {highest_assists} WHICH SCORE {top_scoreA}\n")

# average goals per player and per team
avg_team=df.groupby("Team")['Goals'].mean()
print(f"The average goal per player in team  {avg_team}\n")

# Find the top 3 players by goals and top 3 by assists.
top3_Goals=df.nlargest(3,"Goals")
top3_Goals=top3_Goals.reset_index(drop=True)
top3_Goals.index=top3_Goals.index+1
print(top3_Goals,"\n")
top3_Assists=df.nlargest(3,"Assists")
top3_Assists=top3_Assists.reset_index(drop=True)
top3_Assists.index=top3_Assists.index+1
print(top3_Assists,"\n")


# Calculate average goals and assists per team.
avg_goals=df.groupby("Team")["Goals"].mean().round(2)
print(f"The average goals per teams are:: {avg_goals}\n")

avg_assists=df.groupby("Team")["Assists"].mean().round(2)
print(f"The average assists per teams are:: {avg_assists}\n")

#Add a new column called Performance using these rules:

def performance(goal):
    if goal>=10:
        return "Star Player"
    elif goal>=6 and goal<10:
        return "Key Player"
    else:
        return "Average Player"
    
    
df["Performance"]=df["Goals"].apply(performance) 
print(df)   

#  total number of players performance
countPerformance=df["Performance"].value_counts()
print(f"TOTAL PER PEROFRMANCE \n{countPerformance}")

# team with best passing accuracy
avg_pass=df.groupby("Team")["PassAccuracy"].mean().round(2)
print(avg_pass)
least_av_pass=avg_pass.min()
avg_pass_top=avg_pass.max()
print(f"The team with the best PassAccuracy is {avg_pass_top}")
print(f"The team with the least PassAccuracy is {least_av_pass}")


# data show in bar chart of the teams player in ine chart 

unique_teams=df["Team"].unique()

if len(unique_teams)<=10:
    palette=sns.color_palette("tab10",len(unique_teams))
elif len(unique_teams)<=20:
    palette=sns.color_palette("tab20",len(unique_teams))
else:
    palette=sns.color_palette("husl",len(unique_teams))

team_color_map={team: palette[ i %len(palette)]for i,team in enumerate(unique_teams)}
colors=[team_color_map[team] for team in df["Team"]]

plt.figure(figsize=(12,6))
for team,group in df.groupby("Team"):
    color = team_color_map[team]  # get the color of that team
    plt.bar(group["Player"],group["Goals"],color=color,label=team)
plt.axhline(df["Goals"].mean(),linestyle="--",linewidth=2,color="black",label="average")
plt.xlabel("Team")
plt.ylabel("Players")
plt.grid(True,alpha=0.5,linestyle="--")
plt.legend()
plt.xticks(rotation=45)
plt.title("All the teams players ")
plt.show()

# total matches
total_matches=df['Matches'].sum(axis=0)
print(f"The overall matches played by the players are {total_matches}")

#total player appearances
total_matchesBy=df.groupby("Team")["Matches"].sum()
print(total_matchesBy)

# for team,group in df["Team"]:
less_matches=df[df["Matches"]<10]

# barchart of players how play less then 10 matches
plt.bar(less_matches["Player"],less_matches['Matches'],color="red")
plt.title("PLAYERS HOW PLAY LESS THEN 10 MATCHES ")
plt.xlabel("PLAYER")
plt.ylabel("MATCHES")
plt.xticks(rotation=45)
plt.grid(True,alpha=0.5,linestyle="--")
plt.show()


# Bar Chart – Average PassAccuracy of each team.
for team in avg_pass.index:
    color=team_color_map[team]
    plt.bar(team,avg_pass[team],color=color,label=team)
plt.title("Average passAccuracy of each team ")
plt.xlabel("Team")
plt.ylabel("PassAccuracy")
plt.legend()
plt.grid(True,alpha=0.5,linestyle="--")    
plt.show()





    






