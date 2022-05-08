from math import *
from function import *
from vector import *
from conversion import *
from physics import *
import os
import json

variables = {}

# Load variable data
if os.path.isfile("save.txt"):
    load = open("save.txt", "r")
    variables = json.loads(load.readline())
    load.close()

# Print initial help data
print(
    "-----------------------------\n"
    "Help:\n"
    "[expression]\n"
    "var [x] = [y]\n"
    "funct [f]([x]) = [y]\n"
    "physics [task] [variable]: [attribute_1] = [value_1], [attribute_n] = [value_n]\n"
    "delete [variable]\n"
    "save\n"
    "exit\n"
    "-----------------------------"
)

while True:
    answer = input()

    if answer[:4] == "var ":
        # Create and store a variable with the name and value that the user provides
        expression = answer[4:]

        if "=" in expression:
            try:
                variable = expression[:expression.index('=')].strip()
                value = expression[expression.index('=') + 1:].strip()

                for key in variables.keys():
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

    elif answer[:6] == "funct ":
        # Create and store a function with the name and definition that the user provides
        expression = answer[6:]

        if "=" in expression and "(" in expression and ")" in expression:
            try:
                variable = expression[:expression.index('(')].strip()
                parameters = expression[expression.index('(') + 1:expression.index(')')].split(',')
                definition = expression[expression.index('=') + 1:].strip()

                for i in range(len(parameters)):
                    definition = definition.replace(parameters[i].strip(), f"x[{i}]")

                for key in variables.keys():
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

    elif answer[:8] == "physics ":
        # State that the user will be interacting with physics objects
        physicsExpression = answer[8:]

        if physicsExpression[:7] == "object ":
            # Create and store a physics object with the name provided by the user
            object = physicsExpression[7:]

            variables[object] = str(OneDimensionalPhysicsObject())

            print(f"One Dimensional Physics Object created with name {object}")

        elif physicsExpression[:7] == "modify ":
            # Modify the attributes of the object specified by the user
            expression = physicsExpression[7:]

            if ":" in expression and "=" in expression:
                try:
                    variable = expression[:expression.index(':')].strip()
                    assignments = expression[expression.index(':') + 1:].split(",")
                    obj = eval(variables[variable])

                    for assignment in assignments:
                        attribute = assignment[:assignment.index('=')].strip()
                        value = assignment[assignment.index('=') + 1:].strip()

                        for key in variables.keys():
                            value = value.replace(key, variables[key])

                        value = float(eval(value))

                        obj.modify(attribute, value)

                        print(f"Object {variable} had its attribute {attribute} modified to {value}")

                    variables[variable] = str(obj)

                except:
                    print("Object attributes could not be modified")

            else:
                print("Incorrect format, use x: y = z")

        elif physicsExpression[:10] == "calculate ":
            # Calculate the specified attribute for the object specified by the user
            expression = physicsExpression[10:]

            if ":" in expression:
                try:
                    variable = expression[:expression.index(':')].strip()
                    attributes = expression[expression.index(':') + 1:].split(",")
                    for i in range(len(attributes)):
                        attributes[i] = attributes[i].strip()

                    obj = eval(variables[variable])
                    obj.calculate(attributes)
                    variables[variable] = str(obj)

                except:
                    print("Object attributes could not be calculated")

            else:
                print("Incorrect format, use x: y")

        elif physicsExpression[:6] == "clear ":
            # Clear specific or all attribute data for a specified object
            if ":" in physicsExpression:
                variable = physicsExpression[6:physicsExpression.index(':')].strip()
                attributes = physicsExpression[physicsExpression.index(':') + 1:].split(",")
                obj = eval(variables[variable])

                for attribute in attributes:
                    obj.modify(attribute.strip(), None)

                variables[variable] = str(obj)

            else:
                variable = physicsExpression[6:]
                variables[variable] = str(OneDimensionalPhysicsObject())

            print(f"Object {variable} has been cleared")

    elif answer == "variables":
        # View all variables stored
        for x in variables.keys():
            print(f"{x}: {variables[x]}")

    elif answer == "exit":
        # Save variable data and exit the program
        save = open("save.txt", "w")
        save.write(json.dumps(variables))
        save.close()

        exit()

    elif answer == "save":
        # Save variable data
        save = open("save.txt", "w")
        save.write(json.dumps(variables))
        save.close()

        print("Data has been saved")

    elif answer == "delete variables":
        # Delete all variables stored
        variables.clear()
        print("All variable data has been cleared")

    elif answer[:24] == "delete variables except ":
        vars = answer[24:].split(",")
        for i in range(len(vars)):
            vars[i] = vars[i].strip()
        for key in list(variables.keys()):
            if key not in vars:
                variables.pop(key)
        print("All variables except specified have been deleted")

    elif answer[:7] == "delete ":
        # Delete a specified stored variable
        vars = answer[7:].split(",")

        for var in vars:
            if variables.get(var.strip()):
                variables.pop(var.strip())

        print("Found variables have been deleted")

    elif answer.strip() == "":
        # Allow the user to enter new lines freely
        continue

    else:
        # Evaluate the user's input
        try:
            expression = answer

            for key in variables.keys():
                expression = expression.replace(key, variables[key])

            print(f"Result: {eval(expression)}")

        except:
            print("Not a valid expression")
