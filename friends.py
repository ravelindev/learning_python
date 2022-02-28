# This is an example of how to use list in python
friends = []

new_friend = None

while new_friend != "end":
    new_friend = input("Type the name of a friend: ")    
    if new_friend != "end":
        friends.append(new_friend)
    

print()
print("Your friend are: ")


for friend in friends:
    print(friend)


