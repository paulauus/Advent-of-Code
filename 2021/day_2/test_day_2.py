"""Tests day_2.py."""

from day_2 import give_instructions

def test_give_instructions():
    assert give_instructions(["forward 5",
                             "down 5",
                             "forward 8",
                             "up 3",
                             "down 8",
                             "forward 2"]) == 150
