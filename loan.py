# This a program that will check if  a person is eligible for a loan.
# It will ask the user for those information below and then check if they are eligible.
# How large is the loan?
# How good is your credit history?
# How high is your income?
# How large is your down payment?

# The starting point of the program.
print("Welcome to the Loan Eligibility Checker!")
print(" ")
print("This program will check if you are eligible for a loan.")
print(" ")
print("Enter a number from 1 to 10 on the following questions:")
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
if loan_amount >= 5:
    if credit_score >= 7 and income >= 7:
        print("Yes, you are eligible for a loan.")
    elif credit_score >= 7 or income >= 7:
        print("Yes, you are eligible for a loan.")
    else:
        print("No, you are not eligible for a loan.")
    print(" ")
