"""

Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full,
and 3/4 indicates that a tank is 75% full.

In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs,
as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions
like ValueError or ZeroDivisionError.

"""

#User has to prompt 1/4, then 1 has to be assigned to X and 4 to Y, then make the fraction
#If X or Y is not an int or Y is 0, prompt ValueError and ask again
#If X is greater than Y, ask again
#If <= 1% output "E"
#If >= 99% output "F"
def main():
    x = fuel_percentage("How many fuel is in the tank (Write in fractions)? ")
    print(x)

def fuel_percentage(prompt):
    while True:
        try:
            fuel = (input(prompt))
            x,y = fuel.split("/")
            x = int(x)
            y = int(y)
            percentage = float((x/y)*100)
            if percentage <= 1 and percentage >= 0:
                return "E"
            elif percentage >= 99 and percentage <= 100:
                return "F"
            elif x <= y:
                return f"{percentage:.0f}%"
        except ValueError:
                pass
        except ZeroDivisionError:
                pass

main()




