"""

One of David’s first toys as a child, funny enough, was Little Professor, a “calculator” that would generate ten different math problems for David to solve.
For instance, if the toy were to display 4 + 0 = , David would (hopefully) answer with 4. If the toy were to display 4 + 1 = , David would (hopefully) answer with 5.
If David were to answer incorrectly, the toy would display EEE. And after three incorrect answers for the same problem, the toy would simply display the correct answer
(e.g., 4 + 0 = 4 or 4 + 1 = 5).

In a file called professor.py, implement a program that:

Prompts the user for a level,
. If the user does not input 1, 2, or 3, the program should prompt again.
Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with
 digits. No need to support operations other than addition (+).
Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again,
allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program should output the correct answer.
The program should ultimately output the user’s score: the number of correct answers out of 10.
Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, and generate_integer returns a randomly
generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:

"""
import random


def main():
    create_problems()

def create_problems():
    problem = []
    level = get_level()
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        problem.append(f"{int(x)} + {int(y)}")
    return solve_problems(problem)

def get_level():
    while True:
        try:
            level = input("Level: ")
            if int(level) > 0 and int(level) <= 3:
                return level
        except ValueError:
            pass

def generate_integer(lev):
        if lev == "1":
            return random.randint(0, 9)
        elif lev == "2":
            return random.randint(10, 99)
        elif lev == "3":
            return random.randint(100, 999)

def solve_problems(problems):
    grade = 0
    for p in problems:
        try:
            for t in range(4):
                if t < 3:
                    answer = int(input(f"{p} = "))
                    if answer == int(eval(p)):
                        grade +=1
                        break
                    else:
                        print("EEE")
                elif t == 3:
                    print(f"{p} = {eval(p)}")
        except ValueError:
            pass
    print(f"Score: {grade}")

if __name__ == "__main__":
    main()
