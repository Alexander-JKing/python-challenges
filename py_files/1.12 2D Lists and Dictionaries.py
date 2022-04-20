# 1
"""TwoD_List = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
for i in TwoD_List:
    print(i)"""

# 2
"""TwoD_List = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
user_row = int(input("Please select a row from the list (0, 1, 2, 3): "))
user_column = int(input("Please select a column from the list (0, 1, 2): "))
print("Your value is {}".format(TwoD_List[user_row][user_column]))"""

# 3
"""TwoD_List = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
user_row = int(input("Please select which row to display from the list (0, 1, 2, 3): "))
print(TwoD_List[user_row])
new_value = int(input("Please enter a new value to add to that row: "))
TwoD_List[user_row].append(new_value)
print(TwoD_List[user_row])"""

# 4
"""TwoD_List = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
user_row = int(input("Which row do you want displayed? (0, 1, 2, 3): "))
print(TwoD_List[user_row])
user_column = int(input("Which column in that row do you want displayed? (0, 1, 2): "))
print(TwoD_List[user_row][user_column])
change_value = input("Do you wish to change the value? (Yes/No): ").lower()
condition1 = True
while condition1 is True:
    if change_value == 'yes':
        new_value = int(input("Please select a new value: "))
        TwoD_List[user_row][user_column] = new_value
        print("\nYour new list is now: {}".format(TwoD_List[user_row]))
        condition1 = False
    elif change_value == 'no':
        print("\nUnchanged List: {}".format(TwoD_List[user_row]))
        condition1 = False
    else:
        print("Please select yes or no")"""

# 5
"""twoD_Dictionary = {"John": {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
                   "Tom": {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
                   "Anne": {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859},
                   "Fiona": {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451}}"""

# 6
"""twoD_Dictionary = {"John": {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
                   "Tom": {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
                   "Anne": {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859},
                   "Fiona": {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451}}

for i in twoD_Dictionary:
    print(i)

chosen_name = input("\nPlease select an employee from the range above:  ")
chosen_region = input("Please select a region: ")
new_sales = int(input("Please enter the new sales for this employee: "))
twoD_Dictionary[chosen_name][chosen_region] = new_sales

print("The sales for this employee '{}', are {}".format(chosen_name, twoD_Dictionary[chosen_name][chosen_region]))"""

# 7
"""list = {}
for i in range(0, 4):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    shoe = int(input("Enter shoe size: "))
    list[name] = {"Age": age, "Shoe size": shoe}

# To create the rows of a dictionary, you can set it to an initial empty dictionary,
# then append the category that will be the row data into the list as the first index, 
# then assign the value (which will be a separate dictionary representing the columns).
print(list)

ask = input("\nEnter a name: ")
print(list[ask])"""

# 8
"""list = {}
for i in range(0, 4):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    shoe = int(input("Enter shoe size: "))
    list[name] = {"Age": age, "Shoe size": shoe}

for name in list:
    print(name, list[name]["Age"])"""

# 9
"""list = {}
for i in range(0, 4):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    shoe = int(input("Enter shoe size: "))
    list[name] = {"Age": age, "Shoe size": shoe}

for name in list:
    print("\n", name, list[name]["Age"], list[name]["Shoe size"])

removal = input("\nDo you wish to remove someone from the list (Yes/No): ").lower()
if removal == 'yes':
    name_remove = input("\nPlease enter the name of the person you wish to remove: ")
    del list[name_remove]
else:
    pass

for name in list:
    print(name, list[name]["Age"], list[name]["Shoe size"])"""


