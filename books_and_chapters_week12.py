# This is a program that opens a file and prints the contents of the file.
# It will print the books and the chapters of the books.
# It will find the largest number of chapters in the scripture.
# It will also find the book that has the largest number of chapters in the scripture.

max_chapter = 0 # The largest number of chapters
book_with_max_chapter = "" # The book with the largest number of chapters


#First thing to do is to open the file.
with open("books_and_chapters.txt") as file: # Open the file
    #Then we will loop through the file.
    for line in file: # For each line in the file
        #We will split the line into a list.
        parts = line.split(":") # Split the line based on the ":"
        #We will print the book and the chapter.
        scripture = parts[2].strip() # Get the volume of scripture and strip off any leading/trailing whitespace
        chapter = int(parts[1]) # Get the number of chapters as an integer
        book = parts[0].strip() # Get the book and strip off any leading/trailing whitespace
        print(f"Scripture:  {scripture}, Book: {book}, Chapter: {chapter}.") # Print the book and the chapter
        #We will check to see if the chapter is greater than the max_chapter.
        if chapter > max_chapter: # If the chapter is greater than the max_chapter
            max_chapter = chapter # The max_chapter is now this chapter
            book_with_max_chapter = book # The book with the max_chapter is now this book
print() # Print a blank line
print(f"The book with the largest number of chapters is {book_with_max_chapter}") # Print the book with the largest number of chapters
print(f"The largest number of chapters is {max_chapter}.") # Print the largest number of chapters
print() # Print a blank line
print("Thank you for using the program") # Print a thank you message




        