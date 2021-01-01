import pytest
from RatVenture import *


# to test a valid input of main menu ('1' keypress)
def test_MainMenu(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 1)
    value = show_menu()
    assert value == 1

#to test an invalid input of main menu ('6' keypress)
def test_MainMenuInvalid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 6)
    value = show_menu('main')
    assert value == "Invalid Input"


#test rest function - health will be reset to 20 and player day will increase by 1
def test_restFunction():
   value = rest()
   assert value == (20, player.day+1)

#to return the hero's stats
   def test_viewHeroStats():
    value = herostats()
    assert value == "\nName: {} \nDamage: {}\nDefence: {}\nHP: {}\nDay: {}".format(player.name, player.damage, player.defence, player.hp, player.day)

