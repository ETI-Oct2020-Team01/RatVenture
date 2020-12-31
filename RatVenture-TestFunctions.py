# Test script for RatVenture's functions & features

import pytest
from RatVenture import *

# https://stackoverflow.com/questions/35851323/how-to-test-a-function-with-input-call
# def testMainMenu(monkeypatch):

#     monkeypatch.setattr('builtins.input', lambda _: 1)
#     value = mainMenu()
#     assert value == 1

def test_move_function_LEFT():
   """This is to test if the move "left" function is working. When the player feeds input "A", the H (Hero) indicator should move accordingly and the map will be updated"""
   value = move()
   assert value == (player.positionX, player.positionX+1)
