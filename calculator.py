"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


while True:
    tokens = input(">").split(' ')
    # print(tokens)+

    if tokens[0] == "q":
        print("Quitting the calculator!")
        break
    elif tokens[0] == "+":
        print(add(float(tokens[1]), float(tokens[2])))