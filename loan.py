
"""
File: loan.py
Author: Rudy Ravelin

Purpose: Practice if statements with loan questions
"""
# This a program that will check if  a person is eligible for a loan.
# It will ask the user for those information below and then check if they are eligible.
# How large is the loan?
# How good is your credit history?
# How high is your income?
# How large is your down payment?

# The starting point of the program.
print("***Welcome to the Loan Eligibility Checker!***")
print("***This program will check if you are eligible for a loan.***")
print("***Enter a number from 1 to 10 on the following questions: ***")
print(" ")

# Now the questions listed below.
print("How large is the loan?")
loan_amount = float(input("Enter the loan amount: "))
print(" ")
print("How good is your credit history?")
credit_score = float(input("Enter your credit score: "))
print(" ")
print("How high is your income?")
income = float(input("Enter your income: "))
print(" ")
print("How large is your down payment?")
down_payment = float(input("Enter your down payment: "))
print(" ")
# Now the conditions for the loan.
should_loan = False # Set the default value to false.
if loan_amount >= 5:
    if credit_score >= 7 and income >= 7:
        should_loan = True

    if credit_score >= 7 or income >= 7:
        if down_payment >= 5:
             should_loan = True
    else:
        should_loan = False
else:
    if loan_amount < 4:
        should_loan = False
    if credit_score >=7 or down_payment >= 7:
        should_loan = True
    if credit_score >= 4 and down_payment  >= 4:
        should_loan = True
    else:
        should_loan = False
    print(" ")
if should_loan:
    print("You are eligible for a loan.")
else:
    print("You are not eligible for a loan.")
print(" ")
print("Thank you for using the Loan Eligibility Checker!")
print(" ")
print("Created by: Rudy Ravelin")
print("Date: 02/Feb/2022")
print("Version: 1.0")
print("Copyright (c) 2022 Rudy Ravelin")
print("All rights reserved.")
print("This game is not for sale.")
print("This game is not for resale.")
print("Game created for educational purposes only.")