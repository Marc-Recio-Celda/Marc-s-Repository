"""

In some languages, it’s common to use camel case (otherwise known as “mixed case”) for variables’ names when those names comprise multiple words,
whereby the first letter of the first word is lowercase but the first letter of each subsequent word is uppercase. For instance, whereas a variable
for a user’s name might be called name, a variable for a user’s first name might be called firstName, and a variable for a user’s preferred first name
(e.g., nickname) might be called preferredFirstName.

Python, by contrast, recommends snake case, whereby words are instead separated by underscores (_), with all letters in lowercase. For instance,
those same variables would be called name, first_name, and preferred_first_name, respectively, in Python.

In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case.
Assume that the user’s input will indeed be in camel case.

"""

#Quiero pedir un texto en camelCase y que se devuelva como snake_case
#Podria separar todas las letras en diferentes valores de un str y luego cambiar las mayúsculas por _

#devolver en case_snake
def main():
    var = input("Tell me one variable in caseCamel: ")
    var = convert_to_list(var)
    print(convert(var))

#devolver junto
def convert(case):
    case = "".join(case)
    return case

#cambiar mayúscula por _ + minúscula
def convert_to_list(snake):
    # snake = list(snake) no es necesario para el bucle, al tratarse de una lista de una palabra el mismo bucle lee las letras como una lista,
    # así que lo que conviene es crear una lista vacia y añadir los valores uno a uno
    snake_case = []
    for word in snake:
        if word.isupper():
           # word = word.replace(word, converted_word(word)) En vez de reemplazar simplemente añado a una lista vacía la palabra directamente cambiada
            snake_case.append("_" + word.lower())
        else:
            snake_case.append(word)
    return snake_case

main()
