"""

In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones.
Among the requirements, though, are:

“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”
In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not.
Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements
and False if it does not. Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

"""

def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if req1(s) == True and req2(s) == True and req3(s) == True and req4(s) == True:
        return True
    else:
        return False

#“All vanity plates must start with at least two letters.”
def req1(string):
    number = "0123456789"
    if len(string) > 1:
        if string[0] not in number and string[1] not in number:
            return True
    else:
        return False

#“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
def req2(lenght):
    if len(lenght) <= 6:
        return True
    else:
        return False


#“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
# The first number used cannot be a ‘0’.”
#1: Puede no haber números
#2: El primer número no debe ser un 0
#3: No puede haber letra después de número
def req3(char):
    number = "0123456789"
    found_number = False

    #En caso de que haya números y el primero no sea un 0 OK
    for i, c in enumerate(char):
        if c in number:
            if not found_number:
                found_number = True
                if c == "0":
                    return False
                #En caso que desde el primer número todo sean números OK
                for n in char[i:]:
                    if n not in number:
                        return False
    return True



#“No periods, spaces, or punctuation marks are allowed.”
def req4(no_symbols):
    symbols = ". ?"
    for ch in no_symbols:
        if ch in symbols:
            return False
    return True

main()

