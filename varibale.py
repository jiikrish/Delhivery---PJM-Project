"""
Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
"""
#Remember that variable names are case-sensitive

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#Concatinating variables
x = "awesome"
print("Python is " + x)


#Adding two variables

x = "Python is "
y = "awesome"
z =  x + y
print(z)


#For numbers, the '+'' character works as a mathematical operator
x = 5
y = 10
print(x + y)

"""
Variables that are created outside of a function (as in all of the examples above) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.
"""

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

