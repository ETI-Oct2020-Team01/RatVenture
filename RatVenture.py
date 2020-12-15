#####################
##### RatVenture ####
#####################

### Imports ###
import sys


### Main Menu ###
def mainMenu():
    print("Welcome adventurer, to RatVenture!")
    print("----------------------------------")
    print("Please select an option:")
    print("1) New Game")
    print("2) Resume Game")
    print("3) Exit Game")

mainMenu()
### Main Menu Options ###
#def mainMenu_options():
option = int(input("Enter your option: "))

while option != 0:
    if option == 1:
        # do option 1 stuff
        print("Option 1 has been called")
    elif option == 2:
        # do option 2 stuff
        print("Option 2 has been called")
    elif option == 3: 
        # do option 3 stuff
        print("Option 3 has been called")
    else:
        print("Invalid option. Please choose between the three given options.")

    print()
    mainMenu()
    option = int(input("Enter your option: "))
