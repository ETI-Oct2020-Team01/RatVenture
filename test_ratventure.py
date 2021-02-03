# Test script for RatVenture's functions & features

import pytest
import random
from RatVenture import *


def test_MainMenu(monkeypatch):
    """
    Input: 1

    Output: 1
    """
    
    monkeypatch.setattr("builtins.input", lambda _: 1)  
    value = main_menu(Player)
    assert value == 1

def test_MainMenu_over(monkeypatch):
    """
    Input: 6
    Output: Invalid choice
    """
    monkeypatch.setattr("builtins.input", lambda _: 6)  
    value = main_menu(Player)
    assert value == "Invalid choice"

def test_MainMenu_invalid(monkeypatch):
    """
    Input: a
    Output: Invalid option. Enter only integers!
    """
    monkeypatch.setattr("builtins.input", lambda _: 9)
    value = main_menu(Player)
    assert value == "Invalid option. Enter only integers!"

def test_rest_function():
   """This is to test if rest function is working. By calling this function, player health will restore to 20 and add 1 day to the day count."""
   value = rest()
   assert value == (20, player.day)
