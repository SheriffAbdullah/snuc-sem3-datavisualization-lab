'''
Abdullah Sheriff - AI & DS - SNUC
Exploratory Data Analysis and Data Visualisation Lab (CS2805), 3rd Semester

Exercise 1 - Data Wrangling
Question 1 - Use 'pandas' Library and perform Data Wrangling Operations (a-e)

21/07/2022
'''

import pandas as pd

# (a) Read employees.csv file.
data = pd.read_csv("employees.csv")
print("(a) *** employees.csv ***\n")
print(data.head())

# (b) Find the number of non-null values in each column present.
print("\n(b) Number of Non-Null Values in Each Column.")
print("\nColumn Name      |  Non-Null Count\n", end="")
print("----------------------------------")
print(data.notnull().sum())

# (c) Remove the rows containing null values from the non-numeric columns.
data = data.dropna(subset=["First Name", "Gender", "Start Date", "Last Login Time", "Senior Management", "Team"])
print("\n(c) Rows with null values in non-numeric columns removed.\n")
data.info()

# (d) Find out the columns containing only numeric values.
numeric_data = data[["Salary", "Bonus %"]]
print("\n(d) Columns containing only numeric values.\n")
print(numeric_data.head())

# (e) Create a Pandas Dataframe containing count, minimum value, 
# maximum value, mean, and standard deviation for those columns 
# contaning numeric values alone.
print("\n(e) Description of Numeric Columns.\n")
data_describe = numeric_data.describe()
print(data_describe)


#%%

'''
Abdullah Sheriff - 21110220 - AI & DS Section A - SNUC
Exploratory Data Analysis and Data Visualisation Lab (CS2805), 3rd Semester

Exercise 1 - Data Wrangling
Question 2 - Use 'pandas' Library and 'matplotlib'/'seaborn' for the following (a-c)

21/07/2022
'''

import pandas as pd
import matplotlib.pyplot as plt

# (a) Read the stores.xlsx file.
data = pd.read_excel("stores.xlsx")

# (b) Create a column called "shipment_days" which sould contain the
# difference in days between order date and ship date.
data["shipment_days"] = data["Ship Date"] - data["Order Date"]

# (c) Create suitable graphs using the numeric columns available in the data 
# by using 'matplotlib' or 'seaborn'.
data = data[["Sales", "Quantity", "Discount", "Profit", "shipment_days"]]

fig, axs = plt.subplots(2, 2)

axs[0, 0].hist(data["Sales"], bins=100, range=(0, 500))
axs[0, 0].set_title("Sales")
axs[0, 0].set_xlabel("Sales")
axs[0, 0].set_ylabel("Count")

axs[0, 1].hist(data["Quantity"], bins = 10, range=(0, 25))
axs[0, 1].set_title("Quantity")
axs[0, 1].set_xlabel("Quantity")
axs[0, 1].set_ylabel("Count")

axs[1, 0].hist(data["Discount"], bins = 8, range=(0, 1))
axs[1, 0].set_title("Discount")
axs[1, 0].set_xlabel("Discount")
axs[1, 0].set_ylabel("Count")

axs[1, 1].hist(data["Profit"], bins = 100, range=(-100, 100))
axs[1, 1].set_title("Profit")
axs[1, 1].set_xlabel("Profit")
axs[1, 1].set_ylabel("Count")

fig.tight_layout()

# Shipment Days - Bar Graph
fig, axs = plt.subplots()
shipment_days = data.groupby(by="shipment_days").size()

for i in range(len(shipment_days)):
    plt.bar(x=i, height=shipment_days[i])

plt.title("Shipment Days")
plt.xlabel("Shipment Days")
plt.ylabel("Count")