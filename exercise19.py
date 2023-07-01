# Define a function with two parameters
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # use arguments within the print statements inside the function
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


# call the function with numbers as arguments
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)
# Define two variables and assign numbers to them
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
# call the function passing the variables as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# call the function and pass some calculation as argument
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)
# call the function and pass calculations with variables and numbers
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
