"""Tests for day_2.py."""

from day_2 import convert_to_int_list, calculate_paper_amount

def test_convert_to_int_list():
    """Tests that list of strings is converted into list of lists of strings."""
    assert convert_to_int_list(["29x13x26", "11x11x14"]) == [["29", "13", "26"], ["11", "11", "14"]]

def test_calculate_paper_amount():
    """Tests that correct amount of paper is calculated."""
    assert calculate_paper_amount(["2", "3", "4"]) == 58