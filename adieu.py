"""

In The Sound of Music, there’s a song sung largely in English, So Long, Farewell, with these lyrics, wherein “adieu” means “goodbye” in French:

Adieu, adieu, to yieu and yieu and yieu

Of course, the line isn’t grammatically correct, since it would typically be written (with an Oxford comma) as:

Adieu, adieu, to yieu, yieu, and yieu

To be fair, “yieu” isn’t even a word; it just rhymes with “you”!

In a file called adieu.py, implement a program that prompts the user for names, one per line, until the user inputs control-d. Assume that the user will input at least one name.
Then bid adieu to those names, separating two names with one and, three names with two commas and one and, and names with commas and one and, as in the below:

Adieu, adieu, to Liesl
Adieu, adieu, to Liesl and Friedrich
Adieu, adieu, to Liesl, Friedrich, and Louisa
Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl

names_list = []
    for n in allnames:
        if len(allnames) > 2 and n == allnames[-2]:
            names_list.append(f"{n}, and")
        elif n == allnames[-1]:
            names_list.append(f"{n}")
        elif len(allnames) == 2 and n == allnames[-2]:
            names_list.append(f"{n} and")
        else:
            names_list.append(f"{n},")
    print("Adieu, adieu, to", end = " ")
    for name in range(len(names_list)):
        print(names_list[name], end = " ")
    print("")

"""
import inflect

def main():
    salutacions()

def salutacions():
    names = []
    while True:
        try:
            name = input("Name: ").strip()
            names.append(name)
        except EOFError:
            break
    format_coma(names)

def format_coma(allnames):
    names_list = inflect.engine()
    formatted_names = names_list.join(allnames)
    print(f"Adieu, adieu, to {formatted_names}")


if __name__ == "__main__":
    main()

