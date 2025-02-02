"""

When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr.
In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U)
omitted, whether inputted in uppercase or lowercase.

"""
#Quiero que me digan un texto y devolverlo sin vocales
def main():
    text = input("Enter a text: ").strip()
    print(convert(text))

def convert(words):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    shorten = []
    for word in words:
        if word in vowels:
            shorten.append("")
        else:
            shorten.append(word)
    return "".join(shorten)

main()

