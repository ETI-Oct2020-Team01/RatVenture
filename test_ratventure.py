# Test script for RatVenture's functions & features

import pytest
import random
from RatVenture import *



def test_attack_function():
       """This is to test the attack function and check whether the health of the rat decreases accordingly"""
       value = attack()
       assert rat.hp < 10