#####################
##### RatVenture ####
#####################

### Imports ###
import sys
from random import randint
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
        #self.positionX = 0
       #self.positionY = 0
        self.position = [0,0]
        #self.location = 'You are in a Town'
        self.locationH = 'Town'
        self.event = ['Town', 'Outside', 'Encounter', 'Combat']

    def is_alive(self): 
        return self.hp > 0

player = Player()

### Show Menu ###
# Display the all of the menu function
def show_menu(menu):
    menu_list = {'main': ('New Game','Resume Game','Exit Game'),
                 'town': ('View Character','View Map','Move','Rest','Save Game', 'Exit Game'),
                 'fight': ('Attack','Run'),
                 'open': ('View Character','View Map','Move','Exit Game')}
    menu_text = menu_list[menu]
    for option in range(len(menu_text)): #for printing of the menu
        print('{}) {}'.format(option+1, menu_text[option]))

def display_map(): #to display the world map
    for row in range(len(world_map)):
        #this is for the y axis of the map
        print('+---+---+---+---+---+---+---+---+')
        print('|',end='')
        for col in range(len(world_map[row])):
            #this is for the x axis of the map
            if player.position == [row, col]:
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
            if player.position == [row, col]:
                if world_map[row][col] == ' ': #if the space is empty, player is outside
                    event = 'Outside'
                if world_map[row][col] == 'T': #if the space is a town, player is in a town
                    event = 'Town'
                if world_map[row][col] == 'K': #if the space is a rat king, player encounters rat king
                    event = 'Rat King'
    return event

def move(m): #movement based on the user input
   #positionX, positionY = positionX[0], positionY[1]
    prev_positionY, prev_positionX = player.position[0], player.position[1]

    if m.upper() == 'W':
       player.position[0] -= 1
    elif m.upper() == 'A':
       player.position[1] -= 1
    elif m.upper() == 'S':
       player.position[0] += 1
    elif m.upper() == 'D':
       player.position[1] += 1
    else:
       print('Invalid Input')
    for i in player.position: #if player tries to move out of the map, it will be an invalid move.
        if i < 0 or i > len(world_map)-1:
            player.position[0], player.position[1] =  prev_positionY, prev_positionX
            print('You cannot move there')
    
    if [prev_positionY, prev_positionX] != player.position: #if the player has moved to a new space
        player.day += 1
        player.event = find_event() #find new space event
    display_map()

    

def generate(item): #generation of town
    possible = []

    if item == 'Town': #if parameter is 'Town', generate towns
        for row in range(len(world_map)): #removing existing towns from default map
            for col in range(len(world_map[row])):
                if world_map[row][col] == 'T':
                    world_map[row][col] = ' '
                    
        possible.append([0,0]) #fixed default starting town
        count = 0
        while len(possible) < 5: #run through this algorithm until there are 5 coordinates
            y, x = randint(0,len(world_map)-1), randint(0,len(world_map)-1) #generate random new combinations
            if world_map[y][x] == ' ': #if the space is empty, this excludes spaces where there are towns or kings
                for i in possible:
                    if (i[0] - y)**2 + (i[1] - x)**2 > 4: #formula to distance town from one another
                        count += 1
            if count == len(possible):
                if [y,x] not in possible: #if the new combination are not the same as in the possible list
                    possible.append([y,x]) #append valid coordinates into possible list
                    count = 0
            else: #if there are no more possible combinations reset
                count = 0
                possible = [[0,0]]
        return possible #return valid town coordinates           

### Start of the program ###
print("------------------------------------")
print("⚔ Welcome adventurer, to RatVenture!")
print("------------------------------------")
while True:
    try:
        show_menu('main') #start the program with the main menu
        option = int(input('Enter your option: '))

    
        if option == 1: #new game
            town_location = generate('Town') # get a new generated town coordinates in a list
            for t in town_location: #assigning of new towns in a map
                world_map[t[0]][t[1]] = 'T'  
            
            #player = Player()
            game_over = False

        if option == 2: #resume game
            print()

        if option == 3: #exit game
            sys.exit()

# start of the game        
        while game_over == False:
            try:
# if player is in town
                if player.locationH == 'Town':
                    print('\nDay {}: You are in Town'.format(player.day))
                    show_menu('town')
                    choice = int(input('Enter your option: '))

                    if choice == 1: #view the player stats
                        #herostats()
                        print()

                    elif choice == 2: # view the world map
                        display_map()
                    
                    elif choice == 3: # player to move around the map
                        display_map()
                        print('W = up; A = left; S = down; D = right')
                        move(input('Your move: '))
                    
                    elif choice == 4: # rest
                        player.hp = 20
                        player.day += 1
                        print('\nYou are fully healed.')
                    
                    #elif choice == 5: #save file 

                    elif choice == 6: # exit game
                        game_over = True

                    else:
                        print('Invalid Input\n')

# if the player is outside 
                if player.event == 'Outside':
                    print('Day {}: You are out in the open.'.format(player.day))
                    #rat.Rat()
                    

                    #mob = rat.Rat()[randint(0,len(rat.Rat)-1)]
                    #day_multipler = player.day//10
                    player.event = 'Encounter' # to change the player event to encounter

# if the player is in an encounter 
                if player.event == 'Encounter':
                    #rat.Rat()
                    show_menu('fight')
                    choice = int(input('Enter choice: '))
                    if choice == 1: #if the player, chooses to fight the mob
                        player.event = 'Combat' #change player event to combat
                    elif choice == 2: #if the player, chooses to run away
                        player.event = 'Ran' #change player event to ran
                    else:
                        print('Invalid Input\n')

#if player is in combat
                if player.event == 'Combat':
                    damage_dealt = (randint(player.minDamage, player.maxDamage)) #"""mob['Defence']"""
                    damage_taken = player.defence #"""randint(mob['Min Damage'], mob['Max Damage'])"""

                    if damage_dealt <= 0: #if the damage is in negative range, set to 0
                        damage_dealt = 0
                    #if rat. == 'Rat King' and player.orb == False:
                    #print('\nYou do not have the Orb of Power - the Rat King is immune!')
                    # damage_dealt = 0

            except: #if the player has input an invalid input during the game
                print('Invalid Input\n')
        else: #if game_over == True
            sys.exit()
    except: #if the player has input an invalid input during the main menu
        print('Invalid Input\n')
        continue

 

# Load save file
 #with open('savefile', 'w') as f:
    #pickle.dump(data, f)

#with open('savefile') as f:
    #data = pickle.load(f)