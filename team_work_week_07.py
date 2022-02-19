import random

number = random.randint(1, 100)
print(number)

# print("Welcome to the guessing game!")
# print(" ")
# print("Please enter a number:")
# number = int(input("Number: ")) # User enter the numer
# print(" ")

# asking the user for a guess
print("What is your guess?")
# guess = int(input("Guess: ")) # This for the guess
#print(" ")
# Conditional statement
guess = ''
while number != guess:
    guess = int(input("Guess: "))
    if number < guess:
        print("Go Lower")
    elif number > guess:
        print("Go Higher")
    else:
        print("You guesse it!")

    



# This is the end of the program.


