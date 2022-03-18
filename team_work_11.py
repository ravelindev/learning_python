

# This is a program that opens a file and prints the contents of the file.

with open("hr_system.txt") as person_file: # Open the file
    for line in person_file: # For each line in the file
        line = line.split(" ") # Split the line into a list
        # I want to print the name and the title of the person.
        name = line[0] # The first item in the list is the name
        title = line[2] # The third item in the list is the title
        print(f"Name: {name}, Title: {title}.") # Print the name and title

        