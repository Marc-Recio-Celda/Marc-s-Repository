"""

Among the fonts supported by FIGlet are those at figlet.org/examples.html.

FIGlet has since been ported to Python as a module called pyfiglet.

In a file called figlet.py, implement a program that:

Expects zero or two command-line arguments:
Zero if the user would like to output text in a random font.
Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
Prompts the user for a str of text.
Outputs that text in the desired font.
If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.

"""
from pyfiglet import Figlet
import random
import sys
figlet = Figlet()

def main():
    print(formatted())

def formatted():
    fuentes = figlet.getFonts()
    # 0 or 2 command-line arg
    if len(sys.argv) == 1:
    #0 if user want a random font
        phrase = input("prompt a string of text: ").strip()
        fuente = random.choice(fuentes)
        figlet.setFont(font = fuente)
        return figlet.renderText(phrase)

    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fuentes:
    #2 if user want a text in specific font. first arg --font and second arg name of the font (dic?)
        phrase = input("prompt a string of text: ").strip()
        figlet.setFont(font = sys.argv[2])
        return figlet.renderText(phrase)
    else:
        #if attribute error, sys exit and error message
        sys.exit("Invalid usage")











if __name__ == "__main__":
    main()
