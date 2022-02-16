"""
File: while_loop.py
Author: Rudy Ravelin

Purpose: Practice while loops.
"""

# This a program that asks a user to add a number to see if is positive or negative or zero.
# If the number is positive, the program will print "Your number is positive and print the number entered".
# If the number is negative, the program will print "Your number is negative, please try again".
# If the number is zero, the program will print "Your number is zero and print the number entered"

print("Welcome to the guessing game!")
print("Please enter a number:")
number = int(input())
while number < 0:
    print("Your number is negative, please try again type a positif number")
    number = int(input())
print(f"Your number is positive and the number is: {number}")
print("")

# The program will alos aks the user to simulate a child asking their parent for a piece of candy.
# Have the program keep looping until the user answers "yes", then have the program output "Thank you.

print("asking their parent for a piece of candy")
candy = input("May I have a piece of candy? (yes/no) ").lower()
while candy == "no":
    print("May I have a piece of candy? ")
    candy = input("May I have a piece of candy? (yes/no) ").lower()
    
print("Thank you!")