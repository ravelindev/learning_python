# This is an example of how to use list in python
friends = [] # create an empty list

new_friend = None # create a variable to hold a new friend

while new_friend != "end": # loop until the user enters "end"
    new_friend = input("Type the name of a friend: ") # ask the user for a new friend
    if new_friend != "end": # if the user did not enter "end"
        friends.append(new_friend) # add the new friend to the list
    

print() # print a blank line
print("Your friend are: ") # print a message


for friend in friends: # loop through the list
    print(friend) # print each friend

print() # print a blank line
print("End of program") # print a message
