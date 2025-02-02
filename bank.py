"""

In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0.
If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting,
and treat the user’s greeting case-insensitively.

"""
def greetings():

    greeting = input("Make a greeting: ").strip().casefold()
    #if says hello output 0$
    if greeting.startswith("hello"):
        print("$0")
    #if starts with h output 20$
    elif greeting.startswith("h"):
        print("$20")
    #Otherwise output 100$
    else:
        print("$100")

greetings()
