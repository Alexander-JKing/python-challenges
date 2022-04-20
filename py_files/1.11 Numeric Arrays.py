from random import *
from array import *

# 'i', 'l', 'f', 'd'

# 1
"""user_array = array('i', [])
for x in range(0, 5):
    additional_number = int(input("\nPlease enter a number to add to the array: "))
    user_array.append((additional_number))
    print(user_array)

sorted_array = sorted(user_array)
sorted_array.reverse()
print("\n", sorted_array)"""

# 2
"""array1 = array('i', [])
for x in range(0, 5):
    random_number = random.randint(0, 1000)
    array1.append(random_number)

for num in array1:
    print(num)"""

# 3
"""array1 = array('i', [])
in_range = 0
while in_range < 5:
    numbers = int(input("Please enter a number between 10 and 20: "))
    if numbers >= 10 and numbers <= 20:
        in_range += 1
        array1.append(numbers)
    else:
        print("Outside the range!")
print("Thank you!")
for number in array1:
    print("Array no: {}".format(number))"""

# 4
"""array1 = array('i', [12, 45, 12, 67, 89])
print(array1)
user_input = int(input("Please enter one of the numbers from the array: "))
if array1.count(user_input) == 1:
    print("Your number appears once in the array")
else:
    print("Your number appears {} times".format(array1.count(user_input)))"""

# 5
"""array1 = array('i', [])
array2 = array('i', [])
for i in range(0, 3):
    numbers = int(input("Please enter a number for array1: "))
    array1.append(numbers)
for i in range(0, 5):
    array2.append(randint(0, 1000))
print(array1)
print(array2)
array2.extend(array1)
array_joined = array2
print(sorted(array_joined))"""

# 6
"""array1 = array('i', [])
array2 = array('i', [])
for i in range(0, 5):
    numbers = int(input("Please enter a number: "))
    array1.append(numbers)
print(sorted(array1))
pop_number = int(input("Please select a number from the array you wish to remove: "))
array1.remove(pop_number)
array2.append(pop_number)
print()
print(array1)
print(array2)"""

# 7
"""array1 = array('i', [23, 56, 78, 34, 97])
print(array1)
condition1 = True
while condition1 is True:
    number = int(input("\nPlease select a number to remove from the array: "))
    if number in array1:
        print("index of your selection is {}".format(array1.index(number)))
        condition1 = False
    else:
        print("Please select a number that is within the array:")"""

# 8
"""array1 = array('f', [11.00, 22.00, 33.05, 44.12, 67.34])
condition1 = True
while condition1 is True:
    number = int(input("Please enter a whole number between 2 and 5: "))
    if number >= 2 and number <= 5:
        for i in array1:
            result = i / number
            print("Array entry {} divided by {} = {}".format(round(i, 2), number, round(result, 2)))
        condition1 = False
    else:
        print("Please enter a number from those specified: ")"""