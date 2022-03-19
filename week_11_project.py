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
user_year = input("\nWhat year are you looking for?:  ") # ask for a year

with open("life-expectancy.csv", "r") as dataset: # open the dataset
    # Remove header row
    next(dataset) # skip the header row
    for row in dataset: # iterate through the dataset
        info_set = row.strip() # strip the row
        info = info_set.split(",") # split the row

        life_information.append(info) # append the info to the list 
        entity.append(info[0]) # append the entity to the list
        code.append(info[1]) # append the code to the list
        year.append(info[2]) # append the year to the list
        life_exp.append(float((info[3]))) # append the life exp to the list
# Max and Min life exp
max_life_exp = max(life_exp) # find the max life exp
min_life_exp = min(life_exp)    # find the min life exp

# Max and Min Index 
max_index = life_exp.index(max(life_exp)) # find the max index
min_index = life_exp.index(min(life_exp)) # find the min index

# Highest and Lowest life exp
highest_life_expectation = f"\nFrom the data, the overall max life expectancy is {max_life_exp:.1f} years, from {entity[max_index]} in {year[max_index]}." # print the highest life exp
lowest_life_expectation  = f"\nFrom the data, the overall min life expectancy is {min_life_exp:.1f} years, from {entity[min_index]} in {year[min_index]}." # print the lowest life exp

print(highest_life_expectation) # print the highest life exp
print(lowest_life_expectation) # print the lowest life exp

# For the specified year in the data set 
# Print out the data

life_exp_year = [] # create a list to hold the life exp for the specified year
countries = [] # create a list to hold the countries
for index in life_information: # iterate through the life information
    if index[2] == user_year: # if the year is the same as the user input
        files = index # set the files to the index
        life_exp_year.append(float(index[3])) # append the life exp to the list
        countries.append(index[0]) # append the country to the list


sum_life_exp = sum(life_exp_year) # sum the life exp for the specified year
avg_life_exp = sum_life_exp / len(life_exp_year) # calculate the avg life exp for the specified year
life_expectation_max = max(life_exp_year) # find the max life exp for the specified year
life_expectation_min = min(life_exp_year) # find the min life exp for the specified year

index_max = life_exp_year.index(max(life_exp_year)) # find the max index for the specified year
index_min = life_exp_year.index(min(life_exp_year)) # find the min index for the specified year


# Print out the data
print(f"\nfor the year {user_year}") # print the year
avg_life_exp = f"\nThe average life expectancy for {user_year} is {avg_life_exp:.1f} years." # print the avg life exp
max_life_exp = f"\nThe max life expectancy for {user_year} is {life_expectation_max:.1f} years, from {countries[index_max]}."   # print the max life exp
min_life_exp = f"\nThe min life expectancy for {user_year} is {life_expectation_min:.1f} years, from {countries[index_min]}." # print the min life exp

print(avg_life_exp) # print the avg life exp
print(max_life_exp) # print the max life exp
print(min_life_exp) # print the min life exp
