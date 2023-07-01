# import argv from sys module
from sys import argv

# Assign command line arguments to variables
script, input_file = argv


# Define a function to print all the contents of the file
def print_all(f):
    print(f.read())


# Define another function to rewind the file to its original position
def rewind(f):
    f.seek(0)


# Define another function to print a line number followed but the contents of the line
def print_a_line(line_count, f):
    print(line_count, f.readline())


# Open a file and assign it to a variable
current_file = open(input_file)
print("First let's print the whole file:\n")
# Print out the contents of the file by calling the print_all function and passing the variable current_file
print_all(current_file)
print("Now let's rewind, kind of like a tape.")
# Rewind the file to the first position
rewind(current_file)
print("Let's print three lines:")
# Set the current line and print the contents of each line with the line number
current_line = 1
print_a_line(current_line, current_file)
# Increase the line number by 1
# Set the current line and print the contents of each line with the line number
current_line += 1
print_a_line(current_line, current_file)
# Increase the line number by 1
# Set the current line and print the contents of each line with the line number
current_line += 1
print_a_line(current_line, current_file)
