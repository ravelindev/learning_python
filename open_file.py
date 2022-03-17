# This progrma opens a file and prints the contents of the file.

with open("books.txt") as name_in_the_book_of_mormon:
    for line in name_in_the_book_of_mormon:
        line = line.rstrip()
        print(line)