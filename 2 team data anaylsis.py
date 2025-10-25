import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("team_data.csv")


# separating teams

teamA=df[df['Team']=='Team A']
teamB=df[df['Team']=='Team B']

# team A
teamA.index=teamA.index+1
print(teamA,"\n\n")

# team B
teamB=teamB.reset_index(drop=True)
teamB.index=teamB.index+1
print(teamB)


# total runs by the each team is 

total_runs_team=df.groupby('Team')['Runs'].sum()
print(f"\nTotal Runs by The Each Team is:: {total_runs_team}")

if total_runs_team['Team A']>total_runs_team["Team B"]:
    winner='Team A'
elif total_runs_team['Team B']>total_runs_team['Team B']:
    winner="Team B"

else:
    winner='Draw!!'
print(f"\nThe Winning Team is: {winner}\n")

df['Win'] = df['Team'] == winner if winner != 'Draw' else False
print(df)


# Wickets  

total_wickets=df.groupby("Team")['Wickets'].sum()
print(f"\nTotal Wickets by The Each Team is:: {total_wickets}")

# strilerate

total_strikerate=df.groupby("Team")['StrikeRate'].sum()
print(f"\nTotal strikerate by The Each Team is:: {total_strikerate}\n")



# calculate the avg of both teams things
# runs

avg_runs=total_runs_team.mean()
print(f"The average runs of both team is:: {avg_runs}")



# wickets
avg_wickets=total_wickets.mean()
print(f"The average wickets of both team is:: {avg_wickets}")

# strikerate
avg_strikerate=total_strikerate.mean()
print(f"The average strikerate of both team is:: {avg_strikerate}\n")


# top playes of each team playes in wickets and runs are
# teamA
# runs
playes=df.groupby('Player')['Runs'].sum()
highest_player=playes.idxmax()
print(f"the highest runs in both team is done by {highest_player}")

# wickets

playes=df.groupby('Player')['Wickets'].sum()
highest_player=playes.idxmax()
print(f"the highest wickets taken by in both team is {highest_player}\n\n")



# Find top 3 players by runs and wickets.

runs=df.nlargest(3,'Runs')
print(runs)


# bar chart of both players and runs

colors=['red' if team == 'Team A' else 'green' for team in df['Team']]
plt.bar(df['Player'],df['Runs'],color=colors)
plt.axhline(df['Runs'].mean(),linewidth=2,linestyle="--",label="average",color="black")
plt.grid(True,linestyle='--',alpha=0.5)
plt.legend()
plt.xlabel("Team")
plt.ylabel("Runs")
plt.show()


# bar chart of the total runs by the each team is 
teams=['Team A','Team B']
plt.bar(teams,total_runs_team,color=['gray','Black'])
plt.axhline(avg_runs,linestyle="--",color='red',linewidth=2,label="average")
plt.grid(True,alpha=0.5,linestyle='--')
plt.legend()
plt.xlabel("Teams")
plt.ylabel("Runs")
plt.show()



# Pie chart showing each team’s contribution to total runs.

plt.pie(total_runs_team,labels=total_runs_team.index,autopct="%1.1f%%",startangle=90)
plt.title("CHART SHOWING EACH TEAM CONTRIBUTION IN TOTAL RUNS")
plt.axis("equal")
plt.tight_layout()
plt.show()


for team, group in df.groupby('Team'):
    plt.plot(group['Player'], group['Runs'], marker='o', label=team)

plt.title("Player wise Performance Comparison by Team")
plt.xlabel("Player")
plt.ylabel("Runs")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()


for team,group in df.groupby("Team"):
    plt.plot(group['Player'],group["Wickets"],marker='o',label=team)

plt.title("Player wise performance Comparison by Team")
plt.xlabel("Player")
plt.ylabel("wickets")
plt.legend()
plt.grid(True,linestyle='--',alpha=0.5)
plt.show()


for team,group in df.groupby("Team"):
    plt.plot(group['Player'],group['StrikeRate'],marker='o',label=team)
plt.title("Performance by the each player")
plt.xlabel("Players")
plt.ylabel("StrickeRate")
plt.legend()
plt.grid(True,alpha=0.5,linestyle='--')
plt.show()    


for team,group in df.groupby("Team"):
    plt.plot(group["Player"],group['Matches'],marker='o',label=team)
plt.title("performance by the each player is")
plt.xlabel("Player")
plt.ylabel("runs")
plt.legend()
plt.grid(True,linestyle='--',alpha=0.5)

plt.show()


df.to_csv("team_analysis_result.csv", index=False)
print("\nUpdated analysis saved successfully!")
