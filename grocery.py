"""

Suppose that you’re in the habit of making a list of items you need from the grocery store.

In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program).
Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items.
Treat the user’s input case-insensitively.

"""
def main():
    grocery()

def grocery():
    g_list = []
    while True:
        try:
            item = input().strip().upper()
            g_list.append(item)
        except EOFError:
            break
    #Return innecesario
    return shopping_cart(g_list)

#Orden alfabetico
#Nombre de veces que se ha puesto
def shopping_cart(carrito):
    #definir num innecesario, product tambien
    num = int(1)
    product = sorted(carrito)
    grocery_list = {}
    for p in product:
        #Si el producto no esta en el carrito, añadir 1, Producto
        #Si el producto esta en el carrito, sumar 1 al numero de ese producto
        #grocery_list[item] = grocery_list.get(item, 0) + 1 (Alternativa chatgpt para contador sin if ni else)
        if p in grocery_list:
            grocery_list[p] = grocery_list[p] + 1
        else:
            grocery_list.update({p:num})

    """Alternativa para imprimir directamente el dic:
    for item in sorted(grocery_list.keys()):
        print(f"{grocery_list[item]} {item}") """
    product_list = []
    for prod in grocery_list:
        product_list.append(f"{grocery_list[prod]} {prod}")

    for products in range(len(product_list)):
        #\n no tiene efecto, ya hay un salto de linea tras cada impresion
        print(product_list[products], sep = "\n")




if __name__ == "__main__":
    main()
