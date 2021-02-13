# Test script for RatVenture's functions & features

import pytest
import random
from RatVenture import *

# test for attack function
def test_attack_function():
       """This is to test the attack function and check whether the health of the rat decreases accordingly"""
       value = attack()
       assert rat.hp < 10

# test for displaying hero stats function
def test_view_stats():
   """This is to test if the Hero Stats is displayed accordingly."""
   value = herostats()
   assert value == "\nName: {} \nDamage: {}\nDefence: {}\nHP: {}\nDay: {}".format(player.name, player.damage, player.defence, player.hp, player.day)

# test for rat stats function
def test_view_rat_stats():
   """This is to test if the Rat Stats is displayed accordingly."""
   value = ratstats()
   assert value == "\nDamage: {}\nDefence: {}\nHP: {}".format(rat.damage, rat.defence, rat.hp)

# test for displaying rat king stats function
def test_ratking_stats():
       """This is to test if the Rat King stats are correctly displayed. """
       value = ratkingstats()
       assert value == "\nDamage: {}\nDefence: {}\nHP: {}".format(rat_king.damage, rat_king.defence, rat_king.hp)
       
# test for rest function
def test_rest_function():
   """This is to test if rest function is working. The function will return the player health to 20 and will add a day to the player"""
   value = rest()
   assert value == (player.day)

#test for run function
def test_run_function(monkeypatch):
       """This is to test the run function when encountering a rat."""
       monkeypatch.setattr("builtins.input", lambda _: 2)
       value = combat_menu()
       assert value == 'You run and hide'
      
       
