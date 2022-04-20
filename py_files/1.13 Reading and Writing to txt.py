# 1
"""file = open("Numbers.txt", 'w')
file.write("1, 2, 3, 4, 5!")
file.close()"""

# 2
"""file = open("Names.txt", 'w')
file.write("Alex,\nJohn,\nColm,\nCathal,\nCooney")
file.close()"""

# 3
"""names_file = open("Names.txt", 'a')
new_name = input("Please enter a name you would like to add to the file: ")
names_file.write("\n")
names_file.write(new_name)
names_file.close()"""

# 4
"""user_menu = "1) Create a new file\n" \
            "2) Display the file\n" \
            "3) Add a new item to the file\n" \
            "4) Make a selection of 1, 2 or 3: "
number_selection = int(input("Please select either 1, 2 or 3: "))
if number_selection == 1:
    subject = input("Please enter a school subject: ")
    file = open("Subject.txt", "w")
    file.write("\n")
    file.write(subject)
    file.close()
elif number_selection == 2:
    file = open("Subject.txt", 'r')
    print(file.read())
elif number_selection == 3:
    new_subject = input("Please enter another subject: ")
    file = open("Subject.txt", 'a')
    file.write("\n")
    file.write(new_subject)
    file.close()
else:
    print("Please enter a suitable option!")

file = open("Subject.txt", 'r')
print(file.read())"""

# 5
"""""
with open("Names.txt", 'r') as file:
    print(file.read())
    file.close()

with open("Names.txt", 'r') as file:
    selected_name = input("Please enter one of the names in the file: ")
    selected_name = selected_name + "\n"
    for row in file:
        if row != selected_name:
            file = open("Names3.txt", 'a')
            new_record = row
            file.write(new_record)
            file.close()
file.close()"""""

