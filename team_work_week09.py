import math # import the math module

# This is a program that will ask a list of number and then print the sum of the numbers.
# It will also calculate the average of the numbers.
# And it will print the largest. 

print("This program will ask you to enter a list of numbers and then print the sum of the numbers.")
print()
print("It will also calculate the average of the numbers.")
print()
print("And it will print the largest.")
print()

# This is an example of how to use list in python

numbers = [] # create an empty list

# if numbers == []: # if the list is empty
#     print("The list is empty.")
# else: # if the list is not empty
#     print("The list is not empty.")

new_number = None # create a variable to hold a new number

while new_number != 0: # loop until the user enters "0"
    new_number = int(input("Type a number: ")) # ask the user for a new number
    if new_number != 0: # if the user did not enter "0"
        numbers.append(new_number) # add the new number to the list

print() # print a blank line
print("The numbers are: ") # print a message
sum = 0
for number in numbers: # loop through the list
    sum = sum + number # add the numbers in the list
    print(number) # print each number


#sum = 0 # create a variable to hold the sum
#average = 0 # create a variable to hold the average
#largest = 0 # create a variable to hold the largest

#sum = sum(number) # calculate the sum
#average = sum / len(new_number) # calculate the average
#largest = max(numbers) # find the largest number

print()
print("The sum is: " + str(sum)) # print the sum
print()
count = len(numbers) # count the number of numbers in the list
average = sum / count # calculate the average
smallest = min(numbers) # find the smallest number
print()
print("The smallest number is: " + str(min(numbers))) # print the smallest number
print("The sorted number is: " + str(sorted(numbers))) # print the sorted list
sorted = sorted(numbers) # sort the list
print() 
print("The average is: " + str(average)) # print the average
print()
print("The largest number is: " + str(max(numbers))) # print the largest number
print()


