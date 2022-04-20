# 1
"""name = input("Please enter your name: ")
for i in range(0, 3):
    print(name)"""

# 2
"""name = input("Please enter your name: ")
number = int(input("Please enter the number of times you wish your name to appear: "))
for i in range(0, number):
    print(name)"""

# 3
"""for i in name:
    print(i)"""

# 4
"""name = input("Please enter your name: ")
number = int(input("Please enter the number of times you wish your name to be repeated: "))
for i in range(0, number):
    for j in name:
        print(j)"""

# 5
"""number = int(input("Please enter a number between 1 and 12: "))
for num in range(0, number):
    print("{} * {} = {}".format(num, num, num * num))"""

# 6
"""number = int(input("Please enter a number below 50: "))
print("User entered {}".format(number))
print()
if number < 50:
    for num in range(50, number, -1):
        print(num)
else:
    print("Number entered outside range")"""

# 7
"""name = input("Please enter your name: ")
number = int(input("Please enter a number: "))
if number < 10:
    for num in range(0, number):
        print(name)
else:
    for i in range(0, 3):
        print("Too High!")"""

# 8
"""total = 0
for i in range(0, 5):
    request = int(input("Please enter five numbers separated by a space: "))
    request2 = input("Would you like to add that number to the list total?: ")
    if request2 == "YES" or request2 == "Yes" or request2 == "yes" or request2 == "Y":
        total += request
    else:
        total += 0
print(total)"""

# 9
"""direction = input("Which direction would you like to count? - up/down: ")
direction.lower()
if direction == "up":
    top_number = int(input("Please select a top number to count down from: "))
    for i in range(1, top_number):
        print(i)
elif direction == "down":
    bottom_number = int(input("Please enter a number below 20 to count down from: "))
    for i in range(bottom_number, 0, -1):
        print(i)
else:
    print("Invalid Selection")"""

# 10
"""guest_list = []
guest_num = int(input("How many people would you like to invite to the party?: "))
if guest_num < 10:
    for i in range(0, guest_num):
        guest_names = input("Please input the name of the guest: ")
        print(guest_names + " has been invited")"""
