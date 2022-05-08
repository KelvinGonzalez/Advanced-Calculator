Advanced Calculator

Calculator used for calculus, physics, or any other mathematical need

How to use:
-Write down whatever expression you'd like to get evaluated


Keywords:
var:
-Write variable name, an equal sign, and the value to assign. Ex: "var x1 = 1"

funct:
-Write function name, an equal sign, and the definition to assign. Ex: "funct f1(x) = x + 1"
-Functions may also support additional parameters. Ex: "function f2(x1, x2) = x1 + 2 * x2"

physics:
  object:
  -Write object name. Ex: "physics object obj1"

  modify:
  -Write object name, a colon, and all values to modify. Values to modify are written with attribute name, an equals sign, the value to assign, and separate with a comma. Ex: "physics modify obj1: initVelocity = 1, velocity = 2, time = 3"

  calculate:
  -Write object name, a colon, and all attributes to calculate separated with commas. Ex: "physics calculate obj1: displacement, acceleration"
  
  clear:
  -Write object name, a colon, and all attributes to clear separated with commas, or just the object name if you wish to clear all attributes. Ex: "physics clear obj1: time, velocity, acceleration"

delete:
-Write variable name. Ex: "delete x1"

variables:
-View all variables

clear variables:
-Clear all variables

save:
-Save stored variables

exit:
-Save stored variables and exit the program


Classes:
Vector:
-Object that represents a 3 dimensional vector
-Supports operations such as adding, subtracting, scalars, dot product, cross product
-Vector.API() method to see all available class methods

Function:
-Object that can be called to evaluate its stored function
-Supports operations such as addition, subtraction, multiplication, division, composition, slope, integral, series
-Function.API() method to see all available class methods

OneDimensionalPhysicsObject:
-Object that represents an object that moves in one dimension
-Attributes can be modified or calculated using various formulas
-OneDimensionalPhysicsObject.formulas() to see physics formulas used


Conversion file:
-Used to convert from a unit to another
-Method convert(from, to) will return a scalar used to convert. Ex: "10 * convert("meters", "kilo")" (Units with prefixes have all been added as just the prefix, will work for any type of unit)
