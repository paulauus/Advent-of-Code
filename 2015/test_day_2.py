"""Tests for day_2.py."""

from day_2 import convert_to_str_list, calculate_paper_amount, get_total_paper


def test_convert_to_str_list():
    """Tests that list of strings is converted into list of lists of strings."""
    assert convert_to_str_list("29x13x26") == ["29", "13", "26"]


def test_calculate_paper_amount():
    """Tests that correct amount of paper is calculated."""
    assert calculate_paper_amount(["2", "3", "4"]) == 58


def test_get_total_paper():
    """Tests that correct total amount is calculated."""
    assert get_total_paper(["2x3x4", "1x1x10"]) == 101
