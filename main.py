# create the header
print("====================")
print("Welcome to the UMBC")
print("House Hunting Form!")
print("====================")
print()
# provide instructions for multiple choice
print("(For multiple choice problems, please enter the letter of the selection you're looking for)")
print("~ Rooms~")

#ask user how many bedrooms they want
print("1. How many bedrooms do you want in your home?")
print("  a. 1")
print("  b. 2")
print("  c. 3")
print("  d. 4")

#ask user to enter letter a-d
firstanswer=input("Please enter 'a' - 'd':  ")
print( )

# ask user how many bathrooms they want
print("2. How many bathrooms do you want in your home?")
print("  a. 1")
print("  b. 2")
print("  c. 3")

# ask user to enter letter a-c
secondanswer=input("Please enter 'a' - 'c': ")
print( )

print("~ Location ~")
# ask user if they want to live in a city
print("3. Do you want to live in a city?")
thirdanswer=input("Please enter 'yes' or 'no': ")
print( )

# ask user which state they want to live in
print("4. What state do you want to live in?")
fourthanswer=input("Please enter the name of the state: ")
print( )

print("~ Design ~")
# ask user what color they want they want their house to be
print("5. What color do you want your house to be?")
fifthanswer=input("Please enter the color you would like your house to be: ")
print( )

#ask the user if they want a garage
print("6. Do you want a garage attached to your house?")
sixthanswer=input("Please enter 'yes' or 'no': ")
print( )

# display all the answers in a summary
print("=================")
print("~ Summary ~")
print(f"Number of bedrooms: {firstanswer} ")
print(f"Number of bathrooms: {secondanswer}")
print(f"Live in a city: {thirdanswer}")
print(f"State to live in: {fourthanswer}")
print(f"Color of house: {fifthanswer}")
print(f"Garage attached: {sixthanswer}")
