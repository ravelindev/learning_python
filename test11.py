##### # Date: 2022-03-19
# Week 11 Prove: Milestone
# File: week11-prove.py
# Author: Vern Wolfley
# Purpose: Analyze dataset on life expectancies
#####

# Path to my directory
file_path = "life-expectancy.csv"
data = file_path

total = None
max_le = None
min_le = None
avg_le = None

life_info = []
entity = []
code = []
year = []
life_exp = []

# User input asks for a year
user_year = input("\nWhat year are you looking for?:  ")

with open(data, "r") as dataset:
    # Remove header row
    next(dataset)
    for row in dataset:
        info_set = row.strip()
        info = info_set.split(",")
        
        life_info.append(info)
        entity.append(info[0])
        code.append(info[1])
        year.append(info[2])
        life_exp.append(float((info[3])))
        
# print(life_info)
# print(entity) 
# print(code) 
# print(year)
# print(life_exp) 

# total = len(life_info)
max_le = max(life_exp)
min_le = min(life_exp)
# avg_le = sum(life_exp)/len(life_exp)

min_index = life_exp.index(min(life_exp))
max_index = life_exp.index(max(life_exp))

# print(minIndex)
# print(life_info[minIndex])

# Answer questions on data set
highest_le = f"\nFrom the data, the overall max life expectancy is {max_le:.1f} years, from {entity[max_index]} in {year[max_index]}."
lowest_le = f"\nFrom the data, the overall min life expectancy is {min_le:.1f} years, from {entity[min_index]} in {year[min_index]}."

print(highest_le)
print(lowest_le)

# Looks for the specified year in the data
le = [] 
countries = [] # 
for index in life_info:
    if index[2] == user_year:
#         print(index)
        files = index
        le.append(float(files[3]))
        countries.append(files[0])
        
sum_le = sum(le)
avg_le = sum_le / len(le)
le_min = min(le)
le_max = max(le)
min_i = le.index(le_min)
max_i = le.index(le_max)

average_life = f"\nFor the year {user_year}, the average life expectancy across all countries was {avg_le:.1f} years."
max_life = f"\nThe max life expectancy was in {countries[max_i]} with {le_max:.1f} years."
min_life = f"\nThe min life expectancy was in {countries[min_i]} with {le_min:.1f} years."

print(average_life)
print(max_life)
print(min_life)


# print(life_info)