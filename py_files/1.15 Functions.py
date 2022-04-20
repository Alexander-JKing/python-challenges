import random
import csv

# 1
"""def enter_number():
    num = int(input("Please enter a number: "))
    return num


def count():
    number = enter_number()
    for i in range(1, number):
        print(i)


count()"""

# 2
"""def high_low():
    high = int(input("Please pick a high number close to 100: "))
    low = int(input("Please pick a low number close to 1: "))
    comp_num = random.randint(low, high)
    return comp_num


def guess_num():
    print("I am thinking of a number between 1 and 100..........: ")
    guess = int(input("Guess which number: "))
    return guess


def validation(comp_num, guess):
    condition1 = True
    while condition1 is True:
        if guess != comp_num:
            if guess < comp_num:
                guess = int(input("You are too low!, guess again: "))
            elif guess > comp_num:
                guess = int(input("You are too high!, guess again: "))
        else:
            print("Correct!, YOU WIN!")
            condition1 = False


validation(high_low(), guess_num())"""

# 3
"""def addition():
    number1 = random.randint(5, 21)
    number2 = random.randint(5, 21)
    add_num = number1 + number2
    user_result = int(input("What is {} + {}".format(number1, number2)))
    if user_result == add_num:
        print("You were correct!")
        return user_result, "\n", add_num
    else:
        print("Sorry, you were incorrect!")
        return user_result, "\n", add_num


def subtraction():
    number1 = random.randint(25, 51)
    number2 = random.randint(1, 25)
    sub_number = number1 - number2
    user_result = int(input("What is {} - {}".format(number1, number2)))
    if user_result == sub_number:
        print("You were correct!")
        return user_result, "\n", sub_number
    else:
        print("Sorry, Not correct this time!")
        return user_result, "\n", sub_number


menu_bar = "1) Addition \n" \
           "2) Subtraction \n" \
           "Enter 1 or 2"
print(menu_bar)
user_option = int(input("\nPlease select 1 or 2: "))
if user_option == 1:
    addition()
elif user_option == 2:
    subtraction()
else:
    print("You have entered an invalid selection!")"""

# 4
# Option1
"""def option1():
    new_entry = input("Please enter a name you would like to add to the list: ")
    list_of_names.append(new_entry)
    return list_of_names


def option2():
    x = 0
    for i in list_of_names:
        print(x, ": ", i)
        x += 1

    row_select = int(input("\nPlease select a row you would like to change"))
    new_value = input("Please enter the replacement name: \n")
    list_of_names[row_select] = new_value
    for i in list_of_names:
        print(i)
    return list_of_names


def option3():
    x = 0
    for i in list_of_names:
        print(x, ": ", i)
        x += 1

    row_select = int(input("\nPlease select a row you would like to change: "))
    list_of_names.remove(list_of_names[row_select])
    for i in list_of_names:
        print(i)
    return list_of_names


def option4():
    x = 0
    for i in list_of_names:
        print(x, ": ", i)
        x += 1
    return list_of_names


list_of_names = ["Alex", "John", "Cathal", "Cooney"]

print(list_of_names)

user_options = "1) Add to list: \n" \
               "2) Alter item: \n" \
               "3) Delete item: \n" \
               "4) View all records \n" \
               "5) Terminate Program"

print(user_options)

condition1 = True
while condition1 is True:
    user_option = int(input("\nPlease select an action from the list: "))

    if user_option == 1:
        option1()
        print("\nYou have selected option1 (Add to List)")

    elif user_option == 2:
        option2()
        print("\nYou have selected option2 (Alter item)")

    elif user_option == 3:
        option3()
        print("\nYou have selected option3 (Delete item)")

    elif user_option == 4:
        option4()
        print("\nYou have selected option4 (View all records)")

    elif user_option == 5:
        condition1 = False
        print("You have selected option5 (Terminate Program)")

    else:
        print("Invalid selection: ")"""



# 5
"""def option1():
    with open("Salaries.csv", 'a') as salary:
        employee_name = input("Please enter name: ")
        employee_name = "\n" + employee_name
        employee_salary = input("Please enter salary: ")
        new_record = employee_name + "," + employee_salary
        salary.write(new_record)
        salary.close()


def option2():
    list1 = []
    with open("Salaries.csv", 'r') as salary:
        reader = csv.reader(salary)
        for sal in reader:
            list1.append(sal)
        for entry in list1:
            print(entry)
        salary.close()


with open("Salaries.csv", 'w') as s:
    new_entry = "Alex" + "," + "28000"
    s.write(new_entry)
    s.close()


def show_menu(): 
    menu = "1) Add to file\n" \
       "2) View all records\n" \
       "3) Quit Program"
        print(menu)
        return menu

condition1 = True
while condition1 is True:
    user_option = int(input("\nPlease select an option from the list: "))

    if user_option == 1:
        option1()
        print("\nOption 1 selected")

    elif user_option == 2:
        option2()
        print("\nOption 2 selected")

    elif user_option == 3:
        condition1 = False
        print("Program successfully terminated")"""

# 6
"""def option1():
    with open("Salaries.csv", 'a') as salary:
        employee_name = input("Please enter name: ")
        employee_name = "\n" + employee_name
        employee_salary = input("Please enter salary: ")
        new_record = employee_name + "," + employee_salary
        salary.write(new_record)
        salary.close()


def option2():
    list1 = []
    with open("Salaries.csv", 'r') as salary:
        reader = csv.reader(salary)
        for sal in reader:
            list1.append(sal)
        for entry in list1:
            print(entry)
        salary.close()

# 1 read contents to list
# 2 close file
# 3 ask user to delete an entry from the list
# 4 write the new list to file2


def option3():
    file = open("Salaries.csv", 'r')
    temp = []
    x = 0
    for item in file:
        temp.append(item)
    file.close()
    for row in temp:
        print("{}: {}".format(x, row))
        x += 1
    val_del = int(input("Please select a row to delete: "))
    del temp[val_del]
    new_file = open("Salaries.csv", 'w')
    for new_row in temp:
        new_file.write(new_row)


def show_menu():
    menu = "1) Add to file\n" \
       "2) View all records\n" \
       "3) Delete Record \n" \
           "4) Quit Program"
    print(menu)
    return menu


with open("Salaries.csv", 'w') as s:
    new_entry = "Alex" + "," + "28000"
    s.write(new_entry)
    s.close()

show_menu()

condition1 = True
while condition1 is True:
    user_option = int(input("\nPlease select an option from the list: "))

    if user_option == 1:
        option1()
        print("\nOption 1 selected")
        show_menu()

    elif user_option == 2:
        option2()
        print("\nOption 2 selected")
        show_menu()
        
    elif user_option == 3:
        option3()
        print("\nOption 3 selected")
        show_menu()

    elif user_option == 4:
        condition1 = False
        print("Program successfully terminated")"""

