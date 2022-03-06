#SHOPPING CART PYTHON

names = []
prices = []

action = ""

print()

print("Welcome to the Shopping Cart Program!")

while action != "5":
    print("\nPlease select one of the following:\n"
    "1. Add item\n"
    "2. View cart\n"
    "3. Remove item\n"
    "4. Compute total\n"
    "5. Quit\n")
    action = input("Please enter an action: ")

    if action == "1":
        add_item = input("What item would you like to add? ")
        #add_price = float(input(f"What is the price of '{add_item.capitalize()}'? "))
        print(f"'{add_item.capitalize()}' has been added to the cart.")
        names.append(add_item)
        #prices.append(add_price)
    
    elif action == "2":
        print("The contents of the shopping cart are:")
        for i in range(len(names)):
            add_item = names[i]
            #add_price = prices[i]
            print(f"{i+1}. {add_item.capitalize()}")
    elif action == "5":
        print("Thank You. Goodbye\n") 
        
    else:
        print("Sorry. You have to choose a number between 1 to 5")