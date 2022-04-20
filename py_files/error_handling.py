import random

"""Python ships with a ton of built-in excpetion classes to voer a lot of error situations,
so that you don't have to define your own.

These classes are divided into Base error classes, from which error classes are defined, and
Concrete error classes, which define the exceptions you are more likely to see over time."""

# The simplest way to handle errors is to use the 'try' / 'except' block.
# The code in the 'try' block is executed and id an error, which is specified in the 'except' block is thrown,
# the code in the 'except' block is executed.

try:
    with open('inputtxt', 'r') as myinputfile:
        for line in myinputfile:
            print(line)
except FileNotFoundError:
    print("Whoops, file does not exist")

print("And on to the next line:::::")

# You can handle more than one exception by creating a tuple:
try:
    with open("Exceptions.txt", 'r') as yeaaahhhhh:
        for line in yeaaahhhhh:
            print(line)
except (FileNotFoundError, ValueError):
    print("Now we're cooking!!!!")


# However a better way to handle them is individually like so:
try:
    with open("Exceptions.txt", 'r') as yeaaahhhhh:
        for line in yeaaahhhhh:
            print(line)
except FileNotFoundError:
    print("Now we're cooking!!!!")
except ValueError:
    print("Really cooking:!!!")


"""If you are not quite sure which exception will be raised, then you can always catch the generic 'Exception'
It is good practice to catch the generic Exception at the end of more specific 'except' clauses and not by itself"""

try:
    with open("Exceptions.txt", 'r') as yeaaahhhhh:
        for line in yeaaahhhhh:
            print(line)
except FileNotFoundError:
    print("Now we're cooking!!!!")
except ValueError:
    print("Really cooking:!!!")
except Exception:
    print("When all else fails!!!")


# We can also include an else block in our exceptions!!!
# This Else block will run if no exceptions are raised.

try:
    with open("sample.txt", 'r') as yolo:
        for line in yolo:
            print(line)
except FileNotFoundError:
    print("NO YOLO")
except ValueError:
    print("NO YOLO TODAY")
except Exception:
    print("Something unforeseen happened")
else:
    print("Everything's coming up Millhouse...")


# FINALLY, we have the 'finally' keyword.
# this keyword defines a code block that must execute before the try, except block exits, irrespective of whether
# any exception occured.

try:
    with open("sample.txt", 'r') as yolo:
        for line in yolo:
            print(line)
except FileNotFoundError:
    print("NO YOLO")
except ValueError:
    print("NO YOLO TODAY")
except Exception:
    print("Something unforeseen happened")
finally:
    print("First out the gate, no exceptions yet")

"""The finally keyword is useful for example, in cases where some clean up logic needs to happen.
This might be closing files, closing database connections, or releasing system resources."""
print("--------------------")
print()

try:
    print(random.randinteger(1, 10))
except AttributeError:
    print("ATTRIBUTE EXCEPTION: This is not a valid attribute for this module")

"""CUSTOM EXCEPTIONS

Built-in exceptions cover a wide range of situations. 
Sometimes, however, you may need to define a custom exception to fit your specific application situation.
In this case, python contains the ability to add custom errors by extending the base Exception class"""

# Exceptions should be named with names ending with the word Error.


class RecipeNotValidError(Exception):
    def __init__(self):
        self.message = "Your recipe is not valid"


try:
    raise RecipeNotValidError
except RecipeNotValidError as e:
    print(e.message)

"""The custom exception class should just contain a few attributes (like message) 
that will help the user get more information about the error that occured."""


class IngredientsNotValidError(RecipeNotValidError):
    def __init__(self):
        self.gone_off = True


try:
    raise IngredientsNotValidError
except IngredientsNotValidError as i:
    print(i.gone_off)
