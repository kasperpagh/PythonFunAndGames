from entities.mainFile import capitalCaser
import pytest

def test_capitalCaser_00():
    assert capitalCaser("testString") == "TESTSTRING"

def test_capitalCaser_01():
    assert capitalCaser("TESTSTRING") == "TESTSTRING"

def test_capitalCaser_02():
    assert capitalCaser("teststring") == "TESTSTRING"

def test_capitalCaser_03():
    assert capitalCaser("test string") == "TEST STRING"


def test_capitalCaser_04():
    with pytest.raises(Exception):
        capitalCaser(234)

def test_capitalCaser_04():
    with pytest.raises(Exception):
        capitalCaser()

def test_capitalCaser_04():
    with pytest.raises(Exception):
        capitalCaser([1,"a",21,{}])