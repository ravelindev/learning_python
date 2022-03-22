# This is a way to find the largest and number in a list of numbers.

numbers = [42, 25, 18, 83, 23, 85, 38, 2] # create a list of numbers

largest_so_far = [0] # create a list to hold the largest number

for number in numbers: # iterate through the numbers
    if number > largest_so_far[0]: # if the number is greater than the largest number
        largest_so_far[0] = number # set the largest number to the number
    
print(f"The largest number is: {largest_so_far}") # print the largest number

