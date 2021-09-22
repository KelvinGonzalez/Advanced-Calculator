from math import *
from function import *
from vector import *
from conversion import *
import os
import json

variables = {}

if os.path.isfile("save.txt"):
    load = open("save.txt", "r")
    variables = json.loads(load.readline())
    load.close()

print(
    "-----------------------------\n"
    "Help:\n"
    "[expression]\n"
    "var [x] = [y]\n"
    "funct [f] = [y]\n"
    "delete [variable]\n"
    "exit\n"
    "-----------------------------"
)

while True:
    answer = input()

    if answer[:4].lower() == "var ":
        expression = answer[4:]

        if " = " in expression:
            try:
                variable = expression[:expression.index('=') - 1]
                value = expression[expression.index('=') + 2:]

                for key in list(variables.keys())[::-1]:
                    value = value.replace(key, variables[key])

                value = str(eval(value))

                if variables.get(variable) is not None:
                    variables[variable] = value
                    print(f"Variable {variable}'s value has been changed to {value}")
                    continue

                variables[variable] = value

                print(f"Variable {variable} was created with value {value}")

            except:
                print("Variable was not assigned")

        else:
            print("Incorrect format, use x = y")

    elif answer[:6].lower() == "funct ":
        expression = answer[6:]

        if " = " in expression:
            try:
                variable = expression[:expression.index('=') - 1]
                definition = expression[expression.index('=') + 2:]

                for key in list(variables.keys())[::-1]:
                    definition = definition.replace(key, variables[key])

                function = str(Function(definition))

                if variables.get(variable) is not None:
                    variables[variable] = function
                    print(f"Function {variable}'s definition has been changed to {definition}")
                    continue

                variables[variable] = function

                print(f"Function {variable} was created with definition {definition}")

            except:
                print("Function was not assigned")

        else:
            print("Incorrect format, use f(x) = y")

    elif answer[:7].lower() == "delete ":
        variable = answer[7:]

        if variables.get(variable):
            variables.pop(variable)
            print(f"Variable {variable} has been deleted")
        else:
            print(f"Variable {variable} not found")

    elif answer.lower() == "variables":
        for x in variables.keys():
            print(f"{x}: {variables[x]}")

    elif answer.lower() == "exit":
        save = open("save.txt", "w")
        save.write(json.dumps(variables))
        save.close()

        exit()

    elif answer.lower() == "save":
        save = open("save.txt", "w")
        save.write(json.dumps(variables))
        save.close()

        print("Data has been saved")

    elif answer.lower() == "clear variables":
        variables.clear()
        print("All variable data has been cleared")

    elif answer.lower().replace(" ", "") == "":
        continue

    else:
        try:
            expression = answer

            for key in list(variables.keys())[::-1]:
                expression = expression.replace(key, variables[key])

            print(f"Result: {eval(expression)}")

        except:
            print("Not a valid expression")
