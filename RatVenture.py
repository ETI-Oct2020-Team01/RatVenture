#####################
##### RatVenture ####
#####################

### Imports ###
from random import randint
import time
import pickle
import sys
import random

# global variable
global world_map

# Default world map
world_map = [['T', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', 'T', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', 'T', ' ', ' '],\
             [' ', 'T', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', 'T', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'K']]

# Hero's stats
class Player:
    # The player will start the game with these stats and variables.
    def __init__(self):
        self.name = 'The Hero'
        self.damage = '2 to 4'
        self.minDamage = 2
        self.maxDamage = 4
        self.defence = 1
        self.hp = 20
        self.day = 1
        self.positionX = 0
        self.positionY = 0
        self.location = 'You are in a Town'
        self.locationH = 'H'
        self.orb = [0,0]
        self.checklist = False

    def is_alive(self):
        return self.hp > 0

player = Player()

def herostats():
    stats = "\nName: {} \nDamage: {}\nDefence: {}\nHP: {}\nDay: {}".format(player.name, player.damage, player.defence, player.hp, player.day)
    print(stats)
    if player.checklist == True:
        print('You are holding the Orb of Power')
    return stats

# Rat's stats
class Rat(object):
    def __init__(self):
        self.name = 'Rat'
        self.damage = ' 1 to 3'
        self.minDamage = 1
        self.maxDamage = 3
        self.defence = 1
        self.hp = 10

rat = Rat()

def ratstats():
    stats = "\nDamage: {}\nDefence: {}\nHP: {}".format(rat.damage, rat.defence, rat.hp)
    print(stats)
    return stats

# Rat King's stats
class RatKing(object):
    def __init__(self):
        self.name = 'Rat King'
        self.damage = ' 8 to 12'
        self.minDamage = 8
        self.maxDamage = 12
        self.defence = 5
        self.hp = 25

rat_king = RatKing()

def ratkingstats():
    stats = "\nDamage: {}\nDefence: {}\nHP: {}".format(rat_king.damage, rat_king.defence, rat_king.hp)
    print(stats)
    return stats

# To display the world map
def display_map():
    row = ''
    for y in range(8): #the y axis of the world map
        print('+---+---+---+---+---+---+---+---+')
        for x in range(8): #the x axis of the world map
            if player.positionX == x and player.positionY == y:
                #if the player is on the space to replace the letter with the player's letter 'H'
                if world_map[y][x] == ' ':
                    row = row + '| H' + ' '
                else: 
                    row = row + '|H/' + str(world_map[y][x]) + ''

                if world_map[y][x] == 'T':
                    player.locationH = 'T'
                
                elif world_map[y][x] == 'K':
                    player.locationH = 'K'

                elif world_map[y][x] == ' ':
                    player.locationH = ' '
            else: 
                row = row + '| ' + str(world_map[x][y]) + ' '
        print(row + '|')
        row = ''
        
    print('+---+---+---+---+---+---+---+---+')

# Update the Player's Location
def updatelocation():
    for y in range(8): 
        for x in range(8):
            if player.positionX == x and player.positionY == y:
                if world_map[y][x] == 'T':
                    player.locationH == 'T'
                elif world_map[y][x] == 'K':
                    player.locationH == 'K'
                elif world_map[y][x] == ' ':
                    player.locationH == ' '

# Exit the game
def exit_game():
    exit()
    return

# Run
def run():
    print()
    print('You run and hide')
    rat.hp = 10
    rat_king.hp = 25
    outdoor_menu()

# Find event based on players position
def find_event():
    if player.locationH == 'T': #if the space is a town, player is in a town
        player.location = 'You are in a Town'
    elif player.locationH == ' ': #if the space is empty, player is outside
        player.location = 'You are out in the Open'
    elif player.locationH == 'K': #if the space is a rat king, player encounters rat king
        player.location = 'You see the Rat King'

# Movement based on the user's input (
# 'W' = move up, 'A' = move left, 'S' = move down, 'D' = move right)
def move():
    display_map()
    print('W = up; A = left; S = down; D = right')
    print()
    player.day += 1 # increase player day by 1

    playermove()

def playermove():
    playermove = input('Your Move: ')
    playermove = playermove.upper()
    valid_choice = ['W', 'A', 'S', 'D']
    try:
        while playermove not in valid_choice:
            print('You entered an invalid option. Enter only "W", "A", "S", "D" to move.')
            playermove = input('Your Move: ')
            playermove = playermove.upper()
        
        else:
            if playermove == 'W':
                top()
            elif playermove == 'A':
                left()
            elif playermove == 'S':
                bottom()
            elif playermove == 'D':
                right()
    except ValueError:
            print('You entered an invalid option. Enter only "W", "A", "S", "D" to move.')
            print()
            move()

# Character movement: move up ('W')
def top():
    mlist = [0,1,2,3,4,5,6,7]
    player.positionY -= 1
    #Detect whether player is attempting to move out of map boundaries
    if player.positionY < 0 and player.positionX in mlist:
        player.positionY += 1
        player.day -= 1
        print('Out of bounds! You are not allowed to move out of the map!')
        print()
        updatelocation()
    return player.positionY, player.positionX

# Character movement: move down ('S')
def bottom():
    mlist = [0,1,2,3,4,5,6,7]
    player.positionY += 1
    #Detect whether player is attempting to move out of map boundaries
    if player.positionY > 7 and player.positionX in mlist:
        player.positionY -= 1
        player.day -= 1
        print('Out of bounds! You are not allowed to move out of the map!')
        print()
        updatelocation()
    return player.positionY, player.positionX

# Character movement: move up ('A')
def left():
    mlist = [0,1,2,3,4,5,6,7]
    player.positionX -= 1
    #Detect whether player is attempting to move out of map boundaries
    if player.positionX < 0 and player.positionX not in mlist:
        player.positionX += 1
        player.day -= 1
        print('Out of bounds! You are not allowed to move out of the map!')
        print()
        updatelocation()
    return player.positionY, player.positionX

# Character movement: move right ('D')
def right():
    mlist = [0,1,2,3,4,5,6,7]
    player.positionX += 1
    #Detect whether player is attempting to move out of map boundaries
    if player.positionX > 7 and player.positionX not in mlist:
        player.positionX -= 1
        player.day -= 1
        print('Out of bounds! You are not allowed to move out of the map!')
        print()
        updatelocation()
    return player.positionY, player.positionX
# Rest
def rest():
    player.hp = 20
    player.day += 1
    print('You are fully healed.')#healing process
    return player.day


## Main menu ###
def main_menu():
    print("------------------------------------")
    print("⚔ Welcome adventurer, to RatVenture!")
    print("------------------------------------")
    print("[1] New Game")
    print("[2] Resume Game")
    print("[3] Exit Game")
    mainmenu_userinput()


def mainmenu_userinput():
    print()
    # Get user input in Main Menu and validate
    option = int(input('Enter your choice: '))
    try:
        if option > 3 or option < 0:
            print('Invalid choice!')
            return 'Invalid choice'
        else:
             # Option 1: New Game, display town menu
            if option == 1:
                town_menu(1)
            # Option 2: Resume Game
            elif option == 2:
                print() 
            else:
            # Option 3: Exit Game
                exit_game()
            return option
    except ValueError: 
        #if user inputs string/non-integers
            print('Invalid option. Enter only integers!')
            print()
            main_menu()
    # Return the user input    
    return option

## Town Menu ##
def town_menu(option):
    if option == 1:
        print()
        print('Day {}: You are in a {}.'.format(player.day, player.location))
        print("[1] View Character")
        print("[2] View Map")
        print("[3] Move")
        print("[4] Rest")
        print("[5] Save Game")
        print("[6] Exit Game")
    townmenu_userinput()

def townmenu_userinput():
    print()
    # Checks for user input/option
    option = int(input('Enter your choice: '))
    try:
    # If user inputs something that is not a proper value, return error message
        if option > 6 or option < 0:
            print('Invalid choice!')
            return 'Invalid choice'
        else:
        # Option 1: View Character
            if option == 1:
                herostats()
                town_menu(1)
        # Option 2: View Map
            elif option == 2:
                print()
                display_map()
                town_menu(1)
        # Option 3: Move Character
            elif option == 3:
                print()
                move()
                display_map()
                find_event()
                combat_menu()
                town_menu(1)
        # Option 4: Rest Character
            elif option == 4:
                print('\n')
                rest()
                town_menu(1)
        # Option 5: Save Game (Pending)
            elif option == 5:
                print()
                town_menu(1)
        # Option 6: Exit Game
            else:
                exit_game()
            return option
    except ValueError: 
        # If user inputs string, return error message
            print('Invalid option. Enter only integers!')
            print()
            town_menu(1)
    # Return the user input    
    return option

## Outdoor menu ##
def outdoor_menu():
    print("[1] View Character")
    print("[2] View Map")
    print("[3] Move")
    print("[4] Sense Orb")
    print("[5] Exit Game")

    outdoormenu_userinput()


def outdoormenu_userinput():
    option = int(input('Enter your choice: ')) #check for user input below 
    try:
        if option > 4 or option < 0:
            print('Invalid choice')
            return 'Invalid choice'
        else:
            if option == 1:
                herostats()
                outdoor_menu()
            elif option == 2:
                print()
                display_map()
                outdoor_menu()
            elif option == 3:
                print()
                move()
                display_map()
                find_event()
            elif option == 4:
                #sense_orb()
                outdoor_menu()
            else:
                exit_game()
            return option
    except ValueError: #if user inputs string
            print('Invalid option. Enter only integers!')
            print()
            outdoor_menu()
    # Return the user input    
    return option

# Combat Menu
def combat_menu():
    print()
    for y in range(8): 
        for x in range(8): # 'while loop' 
            if player.locationH == ' ':
                print('Day {}:'.format(player.day), player.location) # to display day and location text
                print('Encounter! - Rat') 
                # To display Rat stats
                print('Damage: {}'.format(rat.damage))
                print('Defence: {}'.format(rat.defence))
                print('HP: {}'.format(rat.hp))
                print("1) Attack")
                print("2) Run")
                combatmenu_userinput()
            
            else:
                town_menu(1)

def combatmenu_userinput():
    option = int(input('Enter your choice: '))#check for user choice below
    try:
        if option > 2 or option < 0:
            print('Invalid choice')
            return 'Invalid choice'
        else:
            if option == 1:
                attack()
            else:
                run()
    except ValueError: #if user inputs string
            print('Invalid option. Enter only integers!')
            print()
            combat_menu()
    # Return the user input    
    return option

# Attack rat
def attack():
    # Check whether the Orb of Power is obtained
        #if orb is obtained (True), boost player damage from 2-4 to 7-9
    if player.checklist == True:
        player.damage = randint(7, 9) 
        player.damage -= 1
        # if orb is not obtained (False), damage remains the same at 2-4
    elif player.checklist == False:
        player.damage = randint(2, 4)
        player.damage -= 1
    
    # While rat is alive, perform damage calculations for hero and rat damage
    while rat.hp > 0:
        # hero damage calculation (randint to randomise between min and max damage)
        playerdamage = random.randint(player.minDamage, player.maxDamage) 
        pdamage = playerdamage - rat.defence
        rat.hp = rat.hp - pdamage

        # rat damage calculation (randint to randomise between min and max damage)
        ratdamage = random.randint(rat.minDamage, rat.maxDamage)
        rdamage = ratdamage - player.defence
        player.hp = player.hp - rdamage

        # Output for attacking scenario with rat
        print()
        print('Oof! The Rat hit you for {} damage!'.format(pdamage)) # Damage taken
        print('You are left with {} HP.'.format(player.hp)) # HP left

        print()

        # Output for when player dies and reaches 0 HP; display game over message and exits game
        if player.hp < 1:
            print('--------------------')
            print('{:^20s}'.format('YOU DIED!'))
            print('{:^20s}'.format('GAME OVER!'))
            print('--------------------')
            sys.exit()
        
        # Output for when player sucessfully defeats rat, display sucesss message and continue display outdoor menu
        if rat.hp <1:
            print('The Rat is dead! You are victorious!')
            print()
            rat.hp = 8 
            outdoor_menu()
        break
    return rat.hp, pdamage


## Rat King menu ##
def king_combat_menu():
    if player.locationH == 'K':
        print('Day {}: You see the Rat King!'.format(player.day), player.location)
        print('Damage: {}'.format(rat_king.damage))
        print('Defence: {}'.format(rat_king.defence))
        print('HP: {}'.format(rat_king.hp))
        print("1) Attack")
        print("2) Run")

        kingcombatmenu_userinput()
    else:
        town_menu(1)

def kingcombatmenu_userinput():
    option = int(input('Enter your choice: '))#check for user choice below
    try:
        if option > 2 or option < 0:
            print('Invalid choice')
            return 'Invalid choice'
        else:
            if option == 1:
                if player.checklist == True:
                    king_attack()
                else:
                    failure_attack(Player)
            elif option == 2:
                run()
            return option
    except ValueError: #if user inputs string
            print('Invalid option. Enter only integers!')
            print()
            king_combat_menu()
    # Return the user input    
    return option

#successful attack
def king_attack():#orb attack
    while rat_king.hp > 0:
        # player damage calculation
        playerdamage = random.randint(player.minDamage, player.maxDamage)
        pdamage = playerdamage - rat_king.defence
        rat_king.hp = rat_king.hp - pdamage

        # rat king damage calculation
        ratkingdamage = random.randint(rat_king.minDamage, rat_king.maxDamage)
        rkdamge = ratkingdamage - player.defence
        player.hp = player.hp - rkdamge

        print()
        print('You dealt {} damage to the Rat King'.format(player.damage))
        print('Ouch! the Rat King hit you for {} damage!'.format(rat_king.damage))
        print('You have {} HP left.'.format(player.hp))

        print()

        if player.hp < 1: 
            print('--------------------')
            print('{:^20s}'.format('You died!'))
            print('{:^20s}'.format('GAME OVER!'))
            print('--------------------')
            sys.exit()
        
        if rat_king < 1:
            print('The Rat King is dead! You are victorious!')
            print('Congratulations! You have defeated the Rat King!')
            print('The world is saved, you WIN!!')
            print()
        
        break
    return pdamage

#attack withou an orb
def failure_attack(Player):#no orb attack sure die
    print('You do not have the Orb of Power - the Rat King is immune!')
    print('You deal 0 damage to the Rat King')
    king_damage = randint(6, 10)#randomise damage
    print('Ouch! The Rat King hit you for {} damage!'.format(king_damage))
    player.hp -= king_damage
    print('You have {} HP left.'.format(player.hp))#normal attack report
    return player

# ## Start of the program ##
# main_menu()

 

# Load save file
 #with open('savefile', 'w') as f:
    #pickle.dump(data, f)

#with open('savefile') as f:
    #data = pickle.load(f)