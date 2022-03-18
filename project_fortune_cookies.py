import random # import random module

lucky_number  = random.randint(1, 50) # generate random number between 1 and 50

fortune_number = random.randint(1, 5) # generate random number between 1 and 5
fortune_text = " " # initialize variable

if fortune_number == 1:
    fortune_text = "You will have a great day!"
if fortune_number == 2:
    fortune_text = "Things will go your way."
if fortune_number == 3:
    fortune_text = "You will meet a new friend."
if fortune_number == 4:
    fortune_text = "You will make a difference."
if fortune_number == 5:
    fortune_text = "You will be successful."

        
print("Your lucky number is:", lucky_number)
print("Your fortune text is:", fortune_text)

