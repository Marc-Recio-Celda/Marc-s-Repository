"""
Either before or after you implement jar.py, additionally implement, in a file called test_jar.py, four or more functions that collectively test your implementation of Jar thoroughly,
each of whose names should begin with test_ so that you can execute your tests with:
Note that it’s not as easy to test instance methods as it is to test functions alone, since instance methods sometimes manipulate the same “state” (i.e., instance variables).
To test one method (e.g., withdraw), then, you might need to call another method first (e.g., deposit). But the method you call first might itself not be correct!

And so programmers sometimes mock (i.e., simulate) state when testing methods, as with Python’s own mock object library, so that you can call just the one method but modify
the underlying state first, without calling the other method to do so.

For simplicity, though, no need to mock any state. Implement your tests as you normally would!

"""
from jar import Jar
import pytest

def test_init():
    with pytest.raises(ValueError):
        jar = Jar()
        jar.deposit("cat")
        str(jar)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar = Jar(15)
    jar.deposit(14)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(4)
    assert str(jar) == "🍪🍪🍪🍪"
    with pytest.raises(ValueError):
        jar = Jar()
        jar.deposit(13)
        str(jar)

def test_withdraw():
    jar = Jar()
    jar.deposit(2)
    jar.withdraw(1)
    assert str(jar) == "🍪"
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(3)
    assert str(jar) == "🍪🍪"
    with pytest.raises(ValueError):
        jar = Jar()
        jar.deposit(5)
        jar.withdraw(7)
        str(jar)

