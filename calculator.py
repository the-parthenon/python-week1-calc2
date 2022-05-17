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
    elif tokens[0] == "-":
        print(subtract(float(tokens[1]), float(tokens[2])))
    elif tokens[0] == "*":
        print(multiply(float(tokens[1]), float(tokens[2])))
    elif tokens[0] == "/":
        print(divide(float(tokens[1]), float(tokens[2])))
    elif tokens[0] == "square":
        print(square(float(tokens[1])))
    elif tokens[0] == "cube":
        print(cube(float(tokens[1])))
    elif tokens[0] == "pow":
        print(power(float(tokens[1]), float(tokens[2])))
    elif tokens[0] == "mod":
        print(mod(float(tokens[1]), float(tokens[2])))