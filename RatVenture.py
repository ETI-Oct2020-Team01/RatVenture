#RatVenture
#Description: Computer role-playing game(RPG) called RatVenture which is text-based.
#             Your objective is to defeat the Rat King and save the world!.

#importing of libraries
from random import randint
import time


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
        self.positionX = 0
        self.positionY = 0
        self.location = 'You are in a Town'
        self.locationH = ' '

    def is_alive(self): 
        return self.hp > 0

player = Player()

def display_map(): #to display the world map
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

