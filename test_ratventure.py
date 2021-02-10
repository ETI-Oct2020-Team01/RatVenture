# Test script for RatVenture's functions & features

import pytest
import random
from RatVenture import *

# test for attack function
def test_attack_function():
       """This is to test the attack function and check whether the health of the rat decreases accordingly"""
       value = attack()
       assert rat.hp < 10

# test for hero stats function
def test_view_stats():
   """This is to test if the Hero Stats is displayed accordingly."""

   value = herostats()

   assert value == "\nName: {} \nDamage: {}\nDefence: {}\nHP: {}\nDay: {}".format(player.name, player.damage, player.defence, player.hp, player.day)

# test for rest function
def test_rest_function():
   """This is to test if rest function is working. The function will return the player health to 20 and will add a day to the player"""
   value = rest()
   assert value == (player.day)

# test for invalid input of main menu
def test_mainmenu_invalid(monkeypatch):
    """
    Input: 9

    Output: Invalid choice 
    """
    monkeypatch.setattr("builtins.input", lambda _: 9)  
    value = mainmenu_userinput()
    assert value == "Invalid choice!"