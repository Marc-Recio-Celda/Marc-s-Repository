"""

“Ah, well,” said Tonks, slamming the trunk’s lid shut, “at least it’s all in. That could do with a bit of cleaning, too.” She pointed her wand at Hedwig’s cage.
“Scourgify.” A few feathers and droppings vanished.

— Harry Potter and the Order of the Phoenix

Data, too, often needs to be “cleaned,” as by reformatting it, so that values are in a consistent, if not more convenient, format.
Consider, for instance, this CSV file of students, before.csv, below:

Source: en.wikipedia.org/wiki/List_of_Harry_Potter_characters

Even though each “row” in the file has three values (last name, first name, and house), the first two are combined into one “column” (name), escaped with double quotes,
with last name and first name separated by a comma and space. Not ideal if Hogwarts wants to send a form letter to each student, as via mail merge, since it’d be strange to start a letter with:

Dear Potter, Harry,

Rather than with, for instance:

Dear Harry,

In a file called scourgify.py, implement a program that:

1 Expects the user to provide two command-line arguments:
2 the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.

3 Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.
4 If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.

"""
import sys
import csv

#No daba problemas pero ahora si?
prompt_input = sys.argv[1]
prompt_output = sys.argv[2]


def main():
    new_dict()

def new_dict():
    hogwarts_student_list = []
    with open(prompt_output, "w") as file:
        #Prepare the 3 elements
        for info in take_argvs():
            #If i put this variable outside the loop, code its printing always the same student
            hogwarts_students = {}
            name, house = info
            last, first = name.rsplit(",")
            #make the dictionary again
            hogwarts_students.update({"last":last.strip(), "first": first.strip(), "house":house.strip()})
            hogwarts_student_list.append(hogwarts_students)
        #write in a new
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(hogwarts_student_list)

def take_argvs():
    try:
        #expects 2 command-line argument
        if len(sys.argv) == 3:
            #debe decir el numero de lineas excluyendo comentarios y lineas en blanco
            students= []
            listed_info =[]
            if prompt_input.endswith(".csv") and prompt_output.endswith(".csv"):
                with open(prompt_input, "r") as file:
                    reader = csv.DictReader(file)
                    #Take Dict from csv
                    for row in reader:
                        students.append(row)
                    #Pass Dict to a list
                    for student in students:
                        student_info = []
                        for stu in student:
                            student_info.append(student[stu])
                        listed_info.append(student_info)
                return listed_info
            else:
                sys.exit("Not a csv file")
        elif len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        else:
            sys.exit("Too many command-line arguments")

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")



if __name__ == "__main__":
    main()
