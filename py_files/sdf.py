import csv


def option3():
    temp = []
    x = 0
    file = open("Salaries.csv", 'r')
    reader = list(csv.reader(file))
    for item in reader:
        temp.append(item)
    for item2 in temp:
        print("{}: {}".format(x, item2))
    val_del = int(input("Please select a row to delete: "))
    del temp[val_del]
    file.close()

    file2 = open("Salaries.csv", 'w')
    for i in temp:
        file.write(i)


option3()

with open("Salaries.csv", 'r') as file3:
    for row in file3:
        print(row)