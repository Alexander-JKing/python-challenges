"""You can arrange your code into pieces called modules, which make it easier to group related functionality together.
Once you have created a module, it becomes very easy to refer to that collection of functionalities again.

Specifically, a module in python is any file with a .py extension
A package is therefore defined as a collection of modules, they are a good way of separating your modules from others,
to avoid name clashes."""

import itertools
import string
import random

# dir(itertools)
# help(itertools)

# Define a function called package_enumerator(), which will take a package or module name and
# print out the names of all the resources defined in the package or module.


def package_enumerator(package):
    for module in dir(package):
        print(module)


# package_enumerator(string)


def random_number_generator(integer):
    random_list = []
    for i in range(0, integer):
        r_int = random.randint(0, 1000)
        random_list.append(r_int)
    return random_list


print(random_number_generator(10))