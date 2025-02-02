import pytest
import sys
from project import catch_error, compound_identifier, compound_data

def test_sys_argv(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["project.py", "4.A6"])
    assert catch_error() == "7210430612"
    monkeypatch.setattr(sys, "argv", ["project.py"])
    with pytest.raises(SystemExit):
        catch_error()
    monkeypatch.setattr(sys, "argv", ["project.py", "4", "A6"])
    with pytest.raises(SystemExit):
        catch_error()

def test_Not_in_hit():
    assert compound_identifier("5.H18") == None
    assert compound_identifier("25.H1") == None

def test_Not_in_library():
    assert compound_identifier("5.H11") == ""

def test_catch_error():
    with pytest.raises(SystemExit):
        compound_identifier("4")
    with pytest.raises(SystemExit):
        compound_identifier("A6")
    with pytest.raises(SystemExit):
        compound_identifier("cat")
    with pytest.raises(SystemExit):
        compound_identifier("4 A6")

def test_compound_identifier():
    assert compound_identifier("4.A6") == "7210430612"
    assert compound_identifier("6.B5") == "7510350036"
    with pytest.raises(SystemExit):
        compound_identifier("4,A6")
    with pytest.raises(SystemExit):
        compound_identifier("4:A6")
def test_compound_data():
    assert compound_data("7210430612") == """
Hit info:
    ID Number: P7210430612
    Formula Structure: C13H12O5
    Molecular Weight: 248,23759"""

    assert compound_data("7510350036") == """
Hit info:
    ID Number: P7510350036
    Formula Structure: C20H27NO3
    Molecular Weight: 329,44309"""
