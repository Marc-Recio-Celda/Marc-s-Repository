"""
Source: Sesame Street

Suppose that you’d like to implement a cookie jar in which to store cookies. In a file called jar.py, implement a class called Jar with these methods:
  -  __init__ should initialize a cookie jar with the given capacity, which represents the maximum number of cookies that can fit in the cookie jar. If capacity is not a non-negative int,
     though, __init__ should instead raise a ValueError.
  -  __str__ should return a str with n🍪, where n is the number of cookies in the cookie jar. For instance, if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"
  -  deposit should add n cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity, though, deposit should instead raise a ValueError.
  -  withdraw should remove n cookies from the cookie jar. Nom nom nom. If there aren’t that many cookies in the cookie jar, though, withdraw should instead raise a ValueError.
  -  capacity should return the cookie jar’s capacity.
  -  size should return the number of cookies actually in the cookie jar, initially 0.

Structure your class per the below. You may not alter these methods’ parameters, but you may add your own methods.

"""
class Jar:
    def __init__(self, capacity=12, size = 0):
        #capacity is the number maximum of cookies that can fit. If is a negative int should raise a ValueError
        self.capacity = capacity
        self.size = size

    def __str__(self):
        #should return n, that is the number of "n🍪" cookies in the jar, if there are 3, should return "🍪🍪🍪"
        return "🍪" * self.size

    def deposit(self, n):
        #should add n cookies to the jar. If exceed the capacity, raise a ValueError
        n = int(n)
        if self.size + n > self.capacity:
            raise ValueError("Not enough capacity")
        self.size += n

    def withdraw(self, n):
        #should remove n cookies from the cookie jar. If there are not enough raise a ValueError
        n = int(n)
        if self.size - n < 0:
            raise ValueError("not enough cookies to withdraw")
        self.size -= n


    @property
    def capacity(self):
        #cookies jar capacity
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if int(capacity) < 12:
            raise ValueError("Too low capacity")
        self._capacity = capacity

    @property
    def size(self):
        #number of cookies in the cookie jar
        return self._size

    @size.setter
    def size(self, size):
        if int(size) > int(self.capacity) or size < 0:
            raise ValueError("Too much cookies")
        self._size = size


def main():
    cookies = get_cookies()
    print(cookies)

def get_cookies():
    jar = Jar()
    jar.deposit(int(input("Deposit: ")))
    jar.withdraw(int(input("Withdraw: ")))
    return jar


if __name__ == "__main__":
    main()
