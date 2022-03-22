shopping_cart = [
    ["Chips", 2.99],
    ["Bread", 2.50],
    ["Milk", 3.19],
    ["Ice Cream", 6.99],
    ["Cheese", 5.99],
    ["Candy bar", 0.99]
]

max_price = -1

for item in shopping_cart:
    price = item[1]
    
    if price > max_price:
        max_price = price

print(f"\nThe highest price is: {max_price}")   # print the highest price
