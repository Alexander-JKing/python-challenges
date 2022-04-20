import sqlite3

#########################################################
# 1
"""Create a SQL Database called PhoneBook 
that contains a table called Names with the following data:"""

# a) connect/create to the database:
# with sqlite3.connect("PhoneBook.db") as db:
#    cursor = db.cursor()

#  b) create table with Keys (Primary/Secondary Keys - only one Primary)
# cursor.execute("""CREATE TABLE IF NOT EXISTS Names(
# id integer PRIMARY KEY,
# First_Name text ,
# Surname text,
# Phone_Number text);""")

# c) create variables to store the relevant information in for easy insert into table
# cursor.execute("""INSERT INTO Names(id, First_Name, Surname, Phone_Number)
# VALUES("1", "Simon", "Howels", "01223 349752")""")
# db.commit()

# newID = input("Enter ID Number: ")
# newName = input("Please enter the first name: ")
# newSurname = input("Please enter the last name: ")
# newNumber = input("Please enter your phone number: ")


# c) add/insert the data to the table:
# cursor.execute("""INSERT INTO Names(id, First_Name, Surname, Phone_Number)
# VALUES(?,?,?,?)""", (newID, newName, newSurname, newNumber))
# db.commit()

# d) display all the data in the table
# cursor.execute("SELECT * FROM Names")
# for i in cursor.fetchall():
#    print(i)

# db.close()

#########################################################
# 2
"""Using the PhoneBook Database from program 139, 
write a program that will display the following menu"""


"""def display_menu():
    print("\t1) View Phonebook:")
    print("\t2) Add to Phonebook:")
    print("\t3) Search for Surname:")
    print("\t4) Delete Person from Phonebook:")
    print("\t5) Quit:")


# 1
def view_phonebook():
    cursor.execute("SELECT * FROM Names")
    for i in cursor.fetchall():
        print(i)"""


# 2
# def add_to_phonebook():
    # new_id = input("Please enter the employee ID: ")
    # new_first_name = input("Please enter the first name: ")
    # new_surname = input("Please enter the surname: ")
    # new_phone_number = input("Please enter the phone number: ")
    # cursor.execute("""INSERT INTO Names(id, First_Name, Surname, Phone_Number)
    # VALUES(?,?,?,?)""", (new_id, new_first_name, new_surname, new_phone_number))
    # db.commit()


# 3
"""def search_surname():
    look_surname = input("Please enter the surname you are looking for: ")
    cursor.execute("SELECT * FROM Names WHERE Surname=?", [look_surname])
    for i in cursor.fetchall():
        print(i)


# 4
def delete_entry():
    id_delete = input("Please enter the ID of the employee you would like to delete from the Database: ")
    cursor.execute("DELETE FROM Names WHERE id=?", [id_delete])
    db.commit()


# 5
def exit_database():
    db.close()


def main():
    not_exit = True
    while not_exit is True:
        print()
        display_menu()
        print()
        user_option = int(input("Please select an option from the menu: "))
        print("\n", user_option)
        if user_option == 1:
            view_phonebook()
        elif user_option == 2:
            add_to_phonebook()
        elif user_option == 3:
            search_surname()
        elif user_option == 4:
            delete_entry()
        elif user_option == 5:
            exit_database()
            not_exit = False
        else:
            print("Please select an appropriate option from the menu\n")


with sqlite3.connect("PhoneBook.db") as db:
    cursor = db.cursor()

main()
db.close()"""

#########################################################
# 3
#########################################################

"""Create a new SQL Database called BookInfo,
 that will store a list fo authors and the books they wrote
 It will have two tables, Authors, Books"""

# i) Create Database
with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

# ii) Create Tables
cursor.execute("""CREATE TABLE IF NOT EXISTS Authors(
name text PRIMARY KEY,
place_of_birth text);""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Books(
id integer PRIMARY KEY,
title text,
author text,
year_published integer);""")


# iii) Add entries


def add_to_Authors_table():
    entries = int(input("Please enter the number of records you wish to add: "))
    if entries > 0:
        for x in range(0, entries):
            author_name = input("Please enter their name: ")
            place_of_birth = input("Please enter their place of birth: ")
            cursor.execute("""INSERT INTO Authors(Name, Place_of_Birth)
            VALUES(?,?)""", (author_name, place_of_birth))
            db.commit()
    else:
        print("No records to add")


# add_to_Authors_table()


def display_Authors_table():
    cursor.execute("SELECT * FROM Authors")
    for i in cursor.fetchall():
        print(i)
        print()


def add_to_Books_table():
    entries = int(input("Please enter the number of records you wish to add: "))
    if entries > 0:
        for x in range(0, entries):
            new_id = input("Please enter the id: ")
            title = input("Please enter the book title: ")
            author = input("Please enter the Author's Name: ")
            year_published = input("Please enter the year published: ")
            cursor.execute("""INSERT INTO Books(id, Title, Author, Year_published)
                VALUES(?,?,?,?)""", (new_id, title, author, year_published))
            db.commit()
    else:
        print("No records to add")


# add_to_Books_table()


def display_Books_table():
    cursor.execute("SELECT * FROM Books")
    for i in cursor.fetchall():
        print(i)
        print()


cursor.execute("UPDATE Books SET Author='Cecelia Ahern' WHERE id=7")
db.commit()

cursor.execute("UPDATE Books SET title='The Marble Collector' WHERE id=7")
db.commit()


# cursor.execute("UPDATE Authors SET Name='Cecilia Ahern' WHERE Place_of_Birth='Boston'")
# db.commit()

#########################################################
# 4
#########################################################
"Ask the user to enter something to search the table with (In this case, year published)"


# display_Authors_table()
print("----------------------")
# display_Books_table()


# place_of_birth = input("Please enter the place of birth for the author you are looking for: ")
# Author = cursor.execute("SELECT Books.Title, Books.Author, Books.Year_published FROM Books, Authors WHERE "
#                        "Authors.Name=Books.Author AND Authors.Place_of_Birth=?", [place_of_birth])
# for x in cursor.fetchall():
    # print(x)
    # print()


#########################################################
# 5
#########################################################
"""Ask the user to enter a year and display all the books published after that year, " \
"sorted by the year that they were published"""

# the_year_published = int(input("Please enter the year the book was published: "))


def display_books_by_year(year):
    cursor.execute("""SELECT Books.title, Books.year_published FROM Books 
                WHERE year_published>? ORDER BY year_published""", [year])
    for x in cursor.fetchall():
        print(x)
        print()


# display_books_by_year(the_year_published)

#########################################################
# 6
#########################################################
""" Ask the user for the author's name and then save all the books by that author to a txt file,
with each field separated by dashes."""

# works_list = []

# display_Books_table()


# author_request = input("Please enter the name of the author you are looking for: ")


# books = cursor.execute("SELECT * FROM Books WHERE Books.Author=?", [author_request])
# for x in cursor.fetchall():
    # new_record = str(x[0]) + "- " + str(x[1]) + "- " + str(x[2]) + "- " + str(x[3]) + "-\n"
    # works_list.append(new_record)

# print("--------------------")
# for i in works_list:
    # print(i)

# print("--------------------")
# print("--------------------")


# with open("author_works.txt", 'w') as file:
    # for x in works_list:
        # file.write(x)
    # file.close()

# db.close()

