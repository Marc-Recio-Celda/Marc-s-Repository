"""

Perhaps the most popular place for pizza in Harvard Square is Pinocchio’s Pizza & Subs, aka Noch’s, known for its Sicilian pizza, which is “a deep-dish or thick-crust pizza.”
Students tend to buy pizza by the slice, but Pinocchio’s also has whole pizzas on its menu too, per this CSV file of Sicilian pizzas, sicilian.csv, below:

See regular.csv for a CSV file of regular pizzas as well.

Of course, a CSV file isn’t the most customer-friendly format to look at. Prettier might be a table, formatted as ASCII art, like this one:

In a file called pizza.py, implement a program that expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format,
and outputs a table formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate. Format the table using the library’s grid format.
If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .csv, or if the specified file does not exist,
the program should instead exit via sys.exit.
grid_menu = tabulate(menu, showindex=True, tablefmt="grid")


print(tabulate(menu, headers = headers, tablefmt="grid"))
"""
import csv
from tabulate import tabulate
import sys

def main():
    try:
        #expects 1 command-line argument
        if len(sys.argv) == 2:
            prompt = sys.argv[1]
            if prompt.endswith(".csv"):
                menu = []
                with open(prompt, "r") as file:
                    reader = csv.DictReader(file)
                    #headers representa una lista con los nombres primeros
                    headers = reader.fieldnames
                    #Tengo aqui una lista de diccionarios, uno por fila
                    listed_menu = []
                    for row in reader:
                        menu.append(row)

                    for m in menu:
                        dish = []
                        for element in m:
                            dish.append(m[element])
                        listed_menu.append(dish)
                    #From https://pypi.org/project/tabulate
                    print(tabulate(listed_menu, headers = headers, tablefmt="grid"))

            else:
                sys.exit("Not a CSV file")

        elif len(sys.argv) == 1:
            sys.exit("Too few command-line arguments")
        else:
            sys.exit("Too many command-line arguments")

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
