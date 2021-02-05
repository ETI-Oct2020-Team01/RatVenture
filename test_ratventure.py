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