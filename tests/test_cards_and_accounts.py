import pytest
from utils.cards_and_accounts import format_number


def test_format_number():
    assert format_number("Счет 84163357546688983493") == "Счет **3493"
    assert format_number("Maestro 3928549031574026") == "Maestro 3928 54** **** 4026"
    assert format_number("Visa Gold 9447344650495960") == "Visa Gold 9447 34** **** 5960"
    assert format_number("Visa Platinum 2256483756542539") == "Visa Platinum 2256 48** **** 2539"
    assert format_number("Visa Classic 6216537926639975") == "Visa Classic 6216 53** **** 9975"
    assert format_number("MasterCard 8532498887072395") == "MasterCard 8532 49** **** 2395"
    assert format_number("МИР 8193813157568899") == "МИР 8193 81** **** 8899"
    assert format_number("") == ""
