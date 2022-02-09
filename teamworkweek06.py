may_ride = False # I set this to false to start

age1 = input("What is the age of the first rider? ")
age1 = int(age1)
height1 = input("What is the height of the first rider? ")
height1 = int(height1)

is_second_rider = input("Is there a second rider? (yes/no) ")
if is_second_rider.lower() == "yes":
    age2 = input("What is the age of the second rider? ")
    age2 = int(age2)
    height2 = input("What is the height of the second rider? ")
    height2 = int(height2)

# Rule # 1
    if height1 < 36 or height2 < 36:
        may_ride = False
    else:
        if age1 >= 18 or age2 >= 18:
            may_ride = True
        else:
            may_ride = False

# Rule # 2
else:
    if age1 >= 18 and height1 >= 62:
        may_ride = True
    else:
        may_ride = False
    

if may_ride:
    print("Welcome to the ride. Please be safe and have fun!")
else:
    print("Sorry, you may not ride.")
