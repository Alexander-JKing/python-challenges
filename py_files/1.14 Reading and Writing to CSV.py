import csv
import random as r

Books = {0: {'Book': 'To Kill a Mockingbird', 'Author': 'Harper Lee', 'Year Released': 1960},
         1: {'Book': 'A Brief History of Time', 'Author': 'Stephen Hawking', 'Year Released': 1988},
         2: {'Book': 'The Great Gatsby', 'Author': 'F.Scott Fitzgerald', 'Year Released': 1922},
         3: {'Book': 'The Man Who Mistook His Wife for a Hat', 'Author': 'Oliver Sacks', 'Year Released': 1985},
         4: {'Book': 'Pride and Prejudice', 'Author': 'Jane Austen', 'Year Released': 1813}}

# 1
"""with open("Books.csv", 'w') as books:
    new_record = "To Kill a Mockingbird, Harper Lee, 1960\n"
    books.write(new_record)
    new_record = "A Brief History of Time, Stephen Hawking, 1988\n"
    books.write(new_record)
    new_record = "The Great Gatsby, F.Scott Fitzgerald, 1922\n"
    books.write(new_record)
    new_record = "The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n"
    books.write(new_record)
    new_record = "Pride and Prejudice, Jane Austen, 1813\n"
    books.write(new_record)
    books.close()"""

# 2
""""with open("Books.csv", 'a') as books:
    new_book = input("Please enter the book: ")
    new_author = input("Please enter the author: ")
    year = input("Please enter the year: ")
    new_record = "\n" + new_book + ", " + new_author + ", " + year
    books.write(new_record)
    books.close()

with open("Books.csv", 'r') as books:
    for row in books:
        print(row)"""

# 3
"""new_records = int(input("How many records would you like to add to the CSV: "))
with open("Books.csv", 'a') as books:
    for i in range(0, new_records):
        new_book = input("Please enter the new book: ")
        new_author = input("Please enter the new author: ")
        year = input("Please enter the year published: ")
        new_record = "\n" + new_book + ", " + new_author + ", " + year
        books.write(new_record)
    books.close()

author = input("Please select an author to search for: ")

with open("Books.csv", 'r') as books:
    for row in books:
        if author in row:
            print(row)
    books.close()"""

# 4
"""start_year = int(input("Please enter a start year: "))
end_year = int(input("Please enter an end year: "))

books = list(csv.reader(open("Books.csv")))
temp = []

for row in books:
    temp.append(row)

for i in temp:
    year = int(i[2])
    if year >= start_year and year <= end_year:
        print(i)"""

# 5
"""""with open("Books.csv", 'r') as books:
    temp = []
    count = 0
    for row in books:
        temp.append(row)
    for i in temp:
        row_object = i
        count += 1
        print("Index:", "   ", "Information:")
        print(count, "        ", row_object)"""

# 6
"""new_list = []
with open("Books.csv", 'r') as books:
    temp = []
    for row in books:
        temp.append(row)
    for entry in temp:
        print(entry)

    row_select = int(input("\nPlease select which row number you would like to delete: "))
    temp.remove(temp[row_select])
    for item in temp:
        new_list.append(item)
        print("\n", item)
        books.close()

print("========================================================")
print("========================================================")
for item in new_list:
    print(item)

with open("Books2.csv", 'w') as books:
    for item in new_list:
        books.write(item)
        print("\n", item)
    books.close()"""

# 7
"""score = 0
name = input("Please enter your name: ")
number1 = r.randint(0, 100)
number2 = r.randint(101, 199)
question1 = int(input("What is {} * {}: ".format(number1, number2)))
real_answer1 = number1 * number2
if question1 == real_answer1:
    score += 1

number3 = r.randint(0, 200)
number4 = r.randint(0, 50)
question2 = int(input("What is {} / {}".format(number3, number4)))
real_answer2 = number3 / number4
if question2 == real_answer2:
    score += 1

user_name = name + ", "
user_answers = str(question1) + ", " + str(question2) + ", "
real_answers = str(real_answer1) + ", " + str(real_answer2) + ", "
user_score = str(score)

new_record_string = ("Name: {}/ User Answers: {} / Real Answers: {} / Score: {}".format(user_name, user_answers, real_answers, user_score))
new_record = user_name + user_answers + real_answers + user_score

print(new_record)
print(new_record_string)

file = open("Maths.csv", 'w')
file.write(new_record)
file.close()

with open("Maths.csv", 'r') as test:
    for row in test:
        print(row)"""













# 6 (Alternate)
"""file = list(csv.reader(open("Books.csv")))
Booklist = []
for row in file:
    Booklist.append(row)


x = 0
for row in Booklist:
    display = x, Booklist[0]
    print(display)
    x += 1
getrid = int(input("Please enter a row number to delete: "))
Booklist.remove(getrid)

x = 0
for row in Booklist:
    display = x, Booklist[x]
    print(display)
    x += 1
alter = int(input("Please enter a row number to alter: "))

x = 0
for row in Booklist[alter]:
    display = x, Booklist[alter][x]
    print(display)
    x += 1
part = int(input("Which part do you want to change?: "))
newdata = input("Enter new data: ")
Booklist[alter][part] = newdata
print(Booklist[alter])

file.close()"""




