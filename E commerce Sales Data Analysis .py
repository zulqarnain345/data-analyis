import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("ecommerce_sales.csv")
print(df.head(10),"\n")

print(df.describe(),"\n")

# how many category are??
noOfCategoryies=df["Category"].nunique()
print(f"types of Categoryies = {noOfCategoryies} ")

# Product Types
typeofproduct=df["Product"].nunique()
print(f"The no of products = {typeofproduct}")

# total avenue are
total=df["Total_Sales"].sum()
print(f"Total avenue = {total}")

# profit on all products are 
profit=df["Profit"].sum()
print(f"Total profit = {profit}")

# how much money made
overallprofit=total-profit
print(f"Profit made = {overallprofit}")

# products you sell
quantity=df["Quantity"].sum()
print(f"Total Quantity of products we sell = {quantity}")

# order we dilvery
total_order=df["Order_ID"].count()
print(f"Total Order We Get = {total_order}\n")

# separating the category

for category, group in df.groupby("Category"):
    print(f"{category}: Total Sales = {group['Total_Sales'].sum()}")
print(" ") 

# category with the highest revenue 

category_revenue=df.groupby("Category")["Total_Sales"].sum()
highest_category=category_revenue.idxmax()
print(f"The top highest category is {highest_category} ")

# find the most products sell on category
for category,group in df.groupby("Category"):
    top_category=group.loc[group["Total_Sales"].idxmax()]
print(f"The top Category which genrate the most revenue are {top_category["Product"]} category of {top_category["Category"]}")        
    

# find the least category product sell
for category,group in df.groupby("Category"):
    least_category=group.loc[group["Total_Sales"].idxmin()]
print(f"The least Category which genrate the most revenue are {least_category["Product"]} with the price of {least_category["Category"]}")        


# product on which you give the highest discount

for product,group in df.groupby("Product"):
    top_discount=group.loc[group["Discount"].idxmax()]
print(f"The product {top_discount["Product"]} on which we give the highest discount is {top_discount["Discount"]*100:.0f}%")

# # product on which you give the least discount

for product,group in df.groupby("Product"):
    least_discount=group.loc[group["Discount"].idxmin()]
print(f"The product {least_discount["Product"]} on which we give the highest discount is {least_discount["Discount"]*100:.0f}%")


# bar chart product which show the price of the products
plt.bar(df["Product"],df["Price"],color="red")
plt.axhline(df["Price"].mean(),linestyle="--",linewidth=2,color="black")
plt.grid(True,alpha=0.5)
plt.legend()
plt.title("OVERALL PROJECT")
plt.xlabel("PRICE")
plt.ylabel("PRODUCT")
plt.show()

# bar chart represent the category wise 

unique_category=df["Category"].nunique()

if len(unique_category)<=10:
    palette=sns.color_palette("tab10",len(unique_category))
elif(len(unique_category)>10 & len(unique_category)<20):
    palette=sns.color_palette("tab20",len(unique_category))
else:
    palette=sns.color_palette("husl",len(unique_category))

category_color_map={category: palette[i % len(palette)]for i,category in enumerate(unique_category)}
color=[category_color_map[category]for categoru in df["Category"]]

plt.bar(df["Product"],df["Price"],color=color)
plt.show()