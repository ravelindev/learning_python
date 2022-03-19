# This progam will look into a dataset and print out some data 
# It will iterate through the dataset and print out the data

import csv # import the csv module
import math # import the math module
import statistics # import the statistics module

total_life_exp = None # total life expectancy
max_life_exp = None # create a variable to hold the max life exp
min_life_exp = None # create a variable to hold the min life exp
avg_life_exp = None # create a variable to hold the avg life exp

life_information = [] # create a list to hold the life information
entity = [] # create a list to hold the entity
code = [] # create a list to hold the code
year = [] # create a list to hold the year
life_exp = [] # create a list to hold the life exp

# User input asks for a year
user_year = input("\nWhat year are you looking for?:  ")

with open("life-expectancy.csv", "r") as dataset:
    # Remove header row
    next(dataset)
    for row in dataset:
        info_set = row.strip()
        info = info_set.split(",")

        life_information.append(info)
        entity.append(info[0])
        code.append(info[1])
        year.append(info[2])
        life_exp.append(float((info[3])))
# Max and Min life exp
max_life_exp = max(life_exp)
min_life_exp = min(life_exp)

# Max and Min Index 
max_index = life_exp.index(max(life_exp))
min_index = life_exp.index(min(life_exp))

# Highest and Lowest life exp
highest_life_expectation = f"\nFrom the data, the overall max life expectancy is {max_life_exp:.1f} years, from {entity[max_index]} in {year[max_index]}."
lowest_life_expectation  = f"\nFrom the data, the overall min life expectancy is {min_life_exp:.1f} years, from {entity[min_index]} in {year[min_index]}."

print(highest_life_expectation)
print(lowest_life_expectation)

# For the specified year in the data set 
# Print out the data

life_exp_year = []
countries = []
for index in life_information:
    if index[2] == user_year:
        files = index
        life_exp_year.append(float(index[3]))
        countries.append(index[0])


sum_life_exp = sum(life_exp_year)
avg_life_exp = sum_life_exp / len(life_exp_year)
life_expectation_max = max(life_exp_year)
life_expectation_min = min(life_exp_year)

index_max = life_exp_year.index(max(life_exp_year))
index_min = life_exp_year.index(min(life_exp_year))


# Print out the data
avg_life_exp = f"\nThe average life expectancy for {user_year} is {avg_life_exp:.1f} years."
max_life_exp = f"\nThe max life expectancy for {user_year} is {life_expectation_max:.1f} years, from {countries[index_max]}."
min_life_exp = f"\nThe min life expectancy for {user_year} is {life_expectation_min:.1f} years, from {countries[index_min]}."

print(avg_life_exp)
print(max_life_exp)
print(min_life_exp)
print(highest_life_expectation)
print(lowest_life_expectation)
