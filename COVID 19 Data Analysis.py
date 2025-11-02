import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("COVID19_Data.csv")
print(df.head(20),"\n")


# overall analyis
analyis=df.describe()
print(analyis)




# find no of countries 
noCountry=df["Country"].nunique()
print(f"There are {noCountry} no of countries in the dataset.. \n")

# Number of positive and negative cases
numberofCases=df['Test_Result'].value_counts()
print(numberofCases)

positive =df[df["Test_Result"]=="Positive"]
nagative =df[df["Test_Result"]=="Negative"]
print(positive)
print(nagative)

# Percentage of vaccinated vs non-vaccinated people

percentage=df["Vaccinated"].value_counts(normalize=True)*100
percentage=percentage.round(2)
print(percentage)


# Average age of tested individuals
avg=df['Age'].mean().round(2)
print(f"The average tested age is :: {avg}\n")


# Positive cases by gender
gender=df.groupby("Gender")["Test_Result"].value_counts()
print(gender,"\n")

# Death rate by age group
bins=[0,30,50,70,100]
label=["0-30","31-50","51-70","70+"]
df["Age_Group"]=pd.cut(df["Age"],bins=bins,labels=label,right=False)

# calculate death rate by age group
DeathRate=df.groupby("Age_Group")["Death"].count()
print(DeathRate)



# Clean up the text columns first (remove spaces, make lowercase)
df["Recovered"] = df["Recovered"].str.strip().str.lower()
df["Vaccinated"] = df["Vaccinated"].str.strip().str.lower()
# Recovery rate among vaccinated vs unvaccinated people
df["Recovered_Flag"]=df["Recovered"].apply(lambda x:1 if x=="yes" else 0)
df["Recovered_Flag"] = df["Recovered_Flag"].astype(int)
recovery=df.groupby("Vaccinated")["Recovered_Flag"].mean().round(2)*100
print("REcovery Rate (%): ")
print(recovery)

# Average age of deaths
avg_age=df[df["Death"]== "Yes"]["Age"].mean().round(2)
print(f"The average of death age is :: {avg_age}")

# Death rate among vaccinated vs unvaccinated people
# Count total people in each group
vaccinated_total = df[df["Vaccinated"] == "Yes"].shape[0]
unvaccinated_total = df[df["Vaccinated"] == "No"].shape[0]

# Count deaths in each group
vaccinated_deaths = df[(df["Vaccinated"] == "Yes") & (df["Death"] == "Yes")].shape[0]
unvaccinated_deaths = df[(df["Vaccinated"] == "No") & (df["Death"] == "Yes")].shape[0]

# Avoid division by zero
if vaccinated_total > 0:
    death_rate_vaccinated = (vaccinated_deaths / vaccinated_total) * 100
else:
    death_rate_vaccinated = 0

if unvaccinated_total > 0:
    death_rate_unvaccinated = (unvaccinated_deaths / unvaccinated_total) * 100
else:
    death_rate_unvaccinated = 0

print(f"Death rate (Vaccinated): {death_rate_vaccinated:.2f}%")
print(f"Death rate (Unvaccinated): {death_rate_unvaccinated:.2f}%")


