# Test script for RatVenture's functions & features

import pytest
from RatVenture import *


# def test_view_stats():
#     value = herostats()
#     assert value == "\nName: {} \nDamage: {}\nDefence: {}\nHP: {}\nDay: {}".format(player.name, player.damage, player.defence, player.hp, player.day)


# def testMainMenu(monkeypatch):

#     monkeypatch.setattr('builtins.input', lambda _: 1)
#     value = show_menu()
#     assert value == 1

def testMainMenu_over(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 6)
    value = show_menu()
    assert value == "Invalid Input"

# def testItem(generate, item):
#     value = generate('Town')
#     assert value == item


