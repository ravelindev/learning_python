# This is a program that will show some people name and the youngest person
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
] # list of people

youngest_name = "" # variable to hold the youngest name
youngest_age = 10000 # variable to hold the youngest age

for person in people: # for each person in the list
    name = person.split()[0] # split the name from the age
    age = int(person.split()[1]) # convert the age to an integer
    if age < youngest_age: # if the age is less than the current youngest age
        youngest_name = name # set the name to the youngest name
        youngest_age = age # set the age to the youngest age

print("The youngest person is", youngest_name, "and they are", youngest_age, "years old.") # print the youngest person

