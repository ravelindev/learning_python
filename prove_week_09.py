# This si a program that will ask a user to enter some items in a cart and display the list of the cart

names = [] #create an empty list
prices = [] #create an empty list

action = "" #create an empty string

print() #print a blank line
print("Welcome to the Shopping Cart Program!") #print a welcome message

while action != "5":    #while the action is not equal to 5
    print("\nPlease select one of the following:\n" #print the following
    "1. Add item\n"
    "2. View cart\n"
    "3. Remove item\n"
    "4. Compute total\n"
    "5. Quit\n")
    action = input("Please enter an action: ") #ask the user to enter an action

    if action == "1": #if the action is equal to 1
        add_item = input("What item would you like to add? ") #ask the user to enter an item
        add_price = float(input(f"What is the price of '{add_item.capitalize()}'? "))
        print(f"'{add_item.capitalize()}' has been added to the cart.") #print the following
        names.append(add_item)  #add the item to the list
        prices.append(add_price)
    
    elif action == "2": #if the action is equal to 2
        print("The contents of the shopping cart are:") #print the following
        for i in range(len(names)): #for each item in the list
            add_item = names[i] #create a variable that is equal to the item
            add_price = prices[i]
            print(f"{i+1}. {add_item.capitalize()}") #print the following
    elif action == "5": #if the action is equal to 5
        print("Thank You. Goodbye\n") #print the following
        
    else:  #if the action is not equal to 1, 2, or 5
        print("Sorry. You have to choose a number between 1 to 5")



