#####################
##### RatVenture ####
#####################

### Imports ###
import sys
add from random import randint
import time
import pickle


#setting of global variables
global world_map

#Default world map
world_map = [['T', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', 'T', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', 'T', ' ', ' '],\
             [' ', 'T', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', 'T', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'K']]

##################
##### Classes ####
##################

# Player/Hero's stats
class Player:
    #the player will start off with these stats
    def __init__(self):
        self.name = 'The Hero'
        self.damage = '2 to 4'
        self.minDamage = '2'
        self.maxDamage = '4'
        self.defence = '1'
        self.hp = 20
        self.day = 1
        self.positionX = 0
        self.positionY = 0
        self.location = 'You are in a town.'
        self.locationH = ' '

    def is_alive(self): 
        return self.hp > 0

player = Player()

# Rat's stats
class Rat(object): 
    def __init__(self):
        self.name = 'Rat'
        self.damage = '1-3'
        self.damage_min = 1 
        self.damage_max = 3
        self.defence = 1
        self.hp = 10 
        #self.location = 'a2'
    
rat = Rat()

# Display hero's name and stats
def herostats():
    stats = player.name + "\nDamage: {}\nDefence: {}\nHP: {}\nDay: {}".format(player.damage, player.defence, player.hp, player.day)
    print(stats)
    return stats

# Display the world map
def display_map(): 
    for row in range(len(world_map)):
        #this is for the y axis of the map
        print('+---+---+---+---+---+---+---+---+')
        print('|',end='')
        for col in range(len(world_map[row])):
            #this is for the x axis of the map
            if player.positionX and player.positionY == [row, col]:
                #if the player is on the space to replace the letter with the player's letter 'H'
                if world_map[row][col] == ' ':
                    world_map[row][col] = 'H'
                if world_map[row][col] == 'T':
                    world_map[row][col] = 'H/T'
                if world_map[row][col] == 'K':
                    world_map[row][col] = 'H/K'
            else:
                #else to replace it back to the default letter
                if world_map[row][col] == 'H':
                    world_map[row][col] = ' '
                if world_map[row][col] == 'H/T':
                    world_map[row][col] = 'T'
                if world_map[row][col] == 'H/K':
                    world_map[row][col] = 'K'
            print('{:^3}|'.format(world_map[row][col]), end='')
        print()
    print('+---+---+---+---+---+---+---+---+')

def find_event(): #finding the event based on players position
    event = ''
    for row in range(len(world_map)):
        for col in range(len(world_map[row])):
            if player.positionY and player.positionX == [row, col]:
                if world_map[row][col] == ' ': #if the space is empty, player is outside
                    event = 'Outside'
                if world_map[row][col] == 'T': #if the space is a town, player is in a town
                    event = 'Town'
                if world_map[row][col] == 'K': #if the space is a rat king, player encounters rat king
                    event = 'Rat King'
    return event

def move(m): #movement based on the user input
   #positionX, positionY = positionX[0], positionY[1]
    prev_positionY, prev_positionX = player.positionY, player.positionX

    if m.upper() == 'W':
       player.positionY -= 1
    elif m.upper() == 'A':
       player.positionX -= 1
    elif m.upper() == 'S':
       player.positionY += 1
    elif m.upper() == 'D':
       player.positionX += 1
    else:
       print('Invalid Input')
    for i in player.positionY and player.positionX: #if player tries to move out of the map, it will be an invalid move.
        if i < 0 or i > len(world_map)-1:
            player.positionY, player.positionX =  prev_positionY, prev_positionX
            print('You cannot move there')
    
    if [prev_positionY, prev_positionX] != player.positionY and player.positionX: #if the player has moved to a new space
        player.day += 1
        player.locationH = find_event() #find new space event
    display_map()

### Main Menu ###
def mainMenu():
    print("------------------------------------")
    print("⚔ Welcome adventurer, to RatVenture!")
    print("------------------------------------")
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
        # Option 1 - New Game
        print("Option 1 has been called")
    elif option == 2:
        # Option 2 - Resume Game
        print("Option 2 has been called")
    elif option == 3: 
        # Option 3 - Exit Game
        print("Exiting game... goodbye!")
        sys.exit()
    else:
        print("Invalid option. Please choose between the three given options.")

    print()
    mainMenu()
    option = int(input("Enter your option: "))

### Town Menu ###

# Display town menu (need to display this after new/resume game)
def townMenu():
    option = int(input("Enter your option: "))
    while option != 0:
        if option == 1:
            print("Day #: You are in a town.")
            print("1) View Character Stats")
            print("2) View World Map")
            print("3) Move")
            print("4) Rest")
            print("5) Save Game")
            print("6) Exit Game")
        
        if option == 1:
            print("Do view character stats")
        elif option == 2:
            print("DO VIEW WORLD MAP ")
        elif option == 3:
            print("DO MOVE")
        elif option == 4:
            print("DO REST")
        elif option == 5:
            print("DO SAVE")
        elif option == 6:
            print("Exiting game... goodbye!")
            sys.exit()
        else:
            print("Invalid option. Please choose between the three given options.")

# Load save file
 #with open('savefile', 'w') as f:
    #pickle.dump(data, f)

#with open('savefile') as f:
    #data = pickle.load(f)