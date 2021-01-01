# Test script for RatVenture's functions & features

import pytest
from RatVenture import *


def testMainMenu(monkeypatch):

    monkeypatch.setattr('builtins.input', lambda _: 1)
    value = show_menu(menu)
    assert value == 1

def testMainMenu_over(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 6)
    value = show_menu(menu)
    assert value == "Invalid Input"
