"""
In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything,
outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

"""
#Program has to ask for the Great Question of Life, the Universe and Everything
answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ").strip().lower()

#If the answer is 42, forty two or forty-two, answer has to be yes, oherwise no
if answer == "42" or answer == "forty two" or answer == "forty-two":
    print("Yes")
else:
    print("No")

