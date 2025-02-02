"""

Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due.
Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore
any integer that isn’t an accepted denomination.

"""

#Quiero pedir que se inserte una moneda y responder la cantidad o cambio a partir de los 50cents
def main():
    money = int(50)
    moneda = int(input("Insert coin: "))
    #Mientras sea menos de 50 y siempre que se añada la moneda adecuada, seguir preguntando
    while money >= 0:
        if moneda == 25 or moneda == 10 or moneda == 5:
            money = money - moneda
            if money <= 0:
                break
            print(f"Amount Due: {money}")
            moneda = int(input(""))
        else:
            print(f"Amount Due: {money}" )
            moneda = int(input(""))
    #Cuando sea mas de 50, simplemente mostrar el cambio
    print(f"Change Owed: {-1 * money }")

main()


