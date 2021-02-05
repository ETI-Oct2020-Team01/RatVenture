#####################
##### RatVenture ####
#####################

### Imports ###
from random import randint
import time
import pickle
import sys

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
    for row in range(len(world_map)): #the y axis of the world map
        print('+---+---+---+---+---+---+---+---+')
        print('|',end='')
        for col in range(len(world_map[row])): #the x axis of the world map
            if player.position == [row, col]:
                 #if the player is on the space to replace the letter with the player's letter 'H'
                if world_map[row][col] == ' ':
                    world_map[row][col] = 'H'
                if world_map[row][col] == 'T':
                    world_map[row][col] = 'H/T'
                if world_map[row][col] == 'K':
                    world_map[row][col] = 'H/K'
            else: #else to replace it back to the default letter
                if world_map[row][col] == 'H':
                    world_map[row][col] = ' '
                if world_map[row][col] == 'H/T':
                    world_map[row][col] = 'T'
                if world_map[row][col] == 'H/K':
                    world_map[row][col] = 'K'
            print('{:^3}|'.format(world_map[row][col]), end='')
        print()
    print('+---+---+---+---+---+---+---+---+')



# Exit the game
def exit_game():
    exit()
    return

# Run
def run():
    print('You run and hide')
    coward = True
    return coward

# Find event based on players position
def find_event():
    event = ''
    for row in range(len(world_map)):
        for col in range(len(world_map[row])):
            if player.position == [row, col]:
                if world_map[row][col] == ' ': #if the space is empty, player is outside
                    event = 'Rat'
                if world_map[row][col] == 'T': #if the space is a town, player is in a town
                    event = 'Town'
                if world_map[row][col] == 'K': #if the space is a rat king, player encounters rat king
                    event = 'Rat King'
    return event

# Movement based on the user's input ('W', 'A', 'S', 'D')
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
            print('You have entered an invalid option. Enter only "W", "A", "S", "D" to move.')
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
    except ValueError: #if user inputs string
            print('Invalid option. Enter only letter!')
            print()
            move()

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
def town_menu(Player):
    town_text = ["View Character", "View Map", "Move", "Rest", "Save Game", "Exit Game"]
    print('Day {}: You are in a {}.'.format(player.day, player.locationH))
    while True:#keep looping till user input is accepted
        #show town text
        for i in range(len(town_text)):
            print('{}) {}'.format(i + 1, town_text[i]))
        try:
            option = int(input('Enter your choice: '))
            #check user input for town text
            if option == 1:
                herostats()
                continue
            elif option == 2:
                display_map()
                print()
                continue
            elif option == 3:
                display_map()
                print('W = up; A = left; S = down; D = right')
                move(input('Your move: '))#map movement map
                print('\n')
                break
            elif option == 4:
                #regenerate health
                print('\n')
                Player = rest()
                break
            elif option == 5:
                print()
                #save hero stats and location to file
                #save_game(hero, day_counter, checklist, coordinates, town_coordinates)
                continue
            elif option == 6:
                exit_game()
                break
            else:
                print('Invalid choice')
                print()
        except ValueError: #if user inputs string
            print('Invalid option. Enter only integers!')
            print()
    return player

# Outdoor menu
def outdoor_menu(Player, coward):
    open_text = ["View Character", "View Map", "Move", "Sense Orb", "Exit Game"]
    while True:
        print()
        for i in range(len(open_text)):
            print('{}) {}'.format(i + 1, open_text[i]))
        try:
            option = int(input('Enter your choice: '))
        except ValueError:
            print('Invalid option. Enter only integers!')
            print()
            continue
        if option == 1:
            herostats()
            continue
        elif option == 2:
            display_map()
            print()
            continue
        elif option == 3:
            display_map()
            print('W = up; A = left; S = down; D = right')
            move(input('Your move: '))
            break
        elif option == 4:
            if coward == True: #cant get orb till you kill rat
                coward = combat_menu(Player, Rat)
            else:
                print()
                #sense_orb()
                
            continue
        elif option == 5:
            exit_game() #exit game
            break
        else:
            print('Invalid choice')
            print()
            continue  
    return player

# Combat Menu
def combat_menu(Player, Rat):
    coward = False
    print('Day {}: You are in the open.'.format(player.day))
    is_rat_alive = True#loop till input accepted
    while True:
        print('Encounter! - Rat')
        ratstats()
        fight_text = ["Attack", "Run"]
        for i in range(len(fight_text)):#fight text
            print('{}) {}'.format(i + 1, fight_text[i]))
        try:
            option = int(input('Enter your choice: '))
            if option == 1:
                Player, Rat, is_rat_alive = attack(is_rat_alive, player, rat)#fight rat
                if is_rat_alive == True:#rat alive
                    pass
                else:
                    print('The Rat is dead! You are victorious!')
                    break
            elif option == 2:
                coward = run() #rrun away from rat
                break
            else:
                print('Number entered is out of range')
                print()
        except ValueError:
            print('Invalid option. Enter only integers!')
            print()
        print()
    return coward

# Attack rat
def attack(is_rat_alive, Player, Rat):
    if player.checklist == True:#orb is obtained
        player.damage = randint(7, 9) 
        player.damage -= 1
    elif player.checklist == False:#no orb
        player.damage = randint(2, 4)
        player.damage -= 1
    rat.hp -= player.damage 
    rat.damage = randint(1, 3) #damage to rat
    print('You dealt {} damage to the Rat'.format(player.damage))
    if rat.hp < 1:
        is_rat_alive = False # rat survived
        return player, rat, is_rat_alive
    elif rat.hp > 1:
        if player.checklist == True:# have orb damage taken
            rat.damage -= 6
            if rat.damage <= 0:
                rat.damage = 0
        else: #no orb damage taken
            rat.damage -= 1
        player.hp -= rat.damage
        print('Ouch! the Rat hit you for {} damage!'.format(rat.damage))#damage taken
        print('You have {} HP left.'.format(player.hp))#hp left
    if player.hp < 1:# player die
        print('--------------------')
        print('{:^20s}'.format('YOU DIED!'))
        print('{:^20s}'.format('GAME OVER!'))
        print('--------------------')
        exit()
    return player, rat, is_rat_alive

# Rat King menu
def king_combat_menu(Player, RatKing):
    print('Day {}: You see the Rat King!'.format(player.day))
    rat_king
    is_king_alive = True #run till king == False
    while True:
        print('Encounter! - Rat King')
        ratkingstats()
        fight_text = ["Attack", "Run"]
        for i in range(len(fight_text)):# show fight or run
            print('{}) {}'.format(i + 1, fight_text[i]))
        print()
        try:
            option = int(input('Enter choice: '))
            if option == 1:
                if player.checklist == True:
                    Player, RatKing, is_king_alive = king_attack(player, rat_king, is_king_alive)
                    if is_king_alive == False:
                        print('The Rat King is dead! You are victorious!')
                        print('Congratulations! You have defeated the Rat King!')
                        print('The world is saved, you WIN!!')
                        break
                    else:
                        pass
                else:
                    failure_attack(Player)
            elif option == 2:
                run()
                break
            else:
                print('Invalid choice!')
                print()
        except ValueError: 
            print('Invalid option. Enter only integers!')
            print()
    return 

#successful attack
def king_attack(Player, rat_king, is_king_alive):#orb attack
    player.damage = randint(7, 9) #randomise damage
    player.damage -= 5
    rat_king.hp -= player.damage 
    rat_king.damage = randint(6,10) #randomise damage
    print('You dealt {} damage to the Rat King'.format(player.damage))
    rat_king.damage -= 6
    player.hp -= rat_king.damage
    if player.hp < 1: #no health and died
        print('--------------------')
        print('{:^20s}'.format('You died!'))
        print('{:^20s}'.format('GAME OVER!'))
        print('--------------------')
        exit()
    elif rat_king.hp < 1: #rat king died
        is_king_alive = False
    else:#normal combat report
        print('Ouch! the Rat King hit you for {} damage!'.format(rat_king.damage))
        print('You have {} HP left.'.format(player.hp))
    return Player, rat_king, is_king_alive

#attack withou an orb
def failure_attack(Player):#no orb attack sure die
    print('You do not have the Orb of Power - the Rat King is immune!')
    print('You deal 0 damage to the Rat King')
    king_damage = randint(6, 10)#randomise damage
    print('Ouch! The Rat King hit you for {} damage!'.format(king_damage))
    player.hp -= king_damage
    print('You have {} HP left.'.format(player.hp))#normal attack report
    return player

## Start of the program ##
Player = main_menu(player)
while player.locationH != 'Rat King':
    if player.locationH == 'Town':
        Player = town_menu(player.day)
    elif player.locationH == 'Rat':#fight rat then can see town
        coward = combat_menu(player.day, rat)
        player = outdoor_menu(player, coward)
king_combat_menu(player, rat_king)

 

# Load save file
 #with open('savefile', 'w') as f:
    #pickle.dump(data, f)

#with open('savefile') as f:
    #data = pickle.load(f)