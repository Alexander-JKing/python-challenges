from tkinter import *
import random
import csv

# Focus could return the cursor to the entry box: Check this

# 1
# Labels : Label(text="")
# Entry Boxes : Entry(text=0)
# Message Boxes : Message(text=0)
# Buttons : Button(text="", command=click)
# Listbox = Listbox()

"""window = Tk()
window.title("Main Window")
window.geometry("500x400")


def click():
    name = entry_box.get()
    message = str("Hello " + name)
    message_box["bg"] = "black"
    message_box["fg"] = "yellow"
    message_box["text"] = message


label = Label(text="Please enter name here:")
label.place(x=-70, y=10, width=300, height=25)

entry_box = Entry("")
entry_box.place(x=150, y=10, width=200, height=25)
entry_box.focus()

message_box = Message("")
message_box["bg"] = "white"
message_box.place(x=150, y=40, width=200, height=65)

button = Button(text="Click Here", command=click)
button.place(x=150, y=120, width=200, height=25)

window.mainloop()"""

# 2
"""window = Tk()
window.title("Main Window")
window.geometry("500x400")


def rand_roll():
    number = random.randint(1, 6)
    message_box["bg"] = "black"
    message_box["fg"] = "yellow"
    message_box["text"] = number


label = Label(text="Click the button to roll the die")
label.place(x=-70, y=10, width=300, height=25)

message_box = Message(text=0)
message_box.place(x=150, y=40, width=200, height=65)

button = Button(text="Click Here to roll!", command=rand_roll)
button.place(x=150, y=120, width=200, height=25)

window.mainloop()"""

# 3
"""window = Tk()
window.title("Main Window")
window.geometry("500x400")


def add_num():
    number = entry_box.get()
    answer = message_box["text"]
    total = int(number) + int(answer)
    message_box["text"] = total
    entry_box.delete(0, END)


def reset():
    message_box["text"] = 0


label = Label(text="Enter number:")
label.place(x=-70, y=10, width=300, height=25)

entry_box = Entry(text=0)
entry_box.place(x=150, y=10, width=200, height=25)

message_box = Message(text=0)
message_box.place(x=150, y=40, width=200, height=65)

button = Button(text="Click Here", command=add_num)
button.place(x=150, y=120, width=200, height=25)

button2 = Button(text="Reset", command=reset)
button2.place(x=150, y=150, width=200, height=25)

window.mainloop()"""

# 4
"""window = Tk()
window.title("Main Window")
window.geometry("500x400")


def click():
    name = entry_box.get()
    name_list.insert(END, name)
    entry_box.delete(0, END)
    entry_box.focus()
    # Orients the cursor back to the entry box (saves you dragging your mouse)


def clear_list():
    name_list.delete(0, END)


label = Label(text="Enter name:")
label.place(x=-70, y=10, width=300, height=25)

entry_box = Entry(text="")
entry_box.place(x=150, y=10, width=200, height=25)

name_list = Listbox()
name_list.place(x=150, y=40, width=200, height=65)

button = Button(text="Click Here", command=click)
button.place(x=150, y=120, width=200, height=25)

button2 = Button(text="Delete", command=clear_list)
button2.place(x=150, y=150, width=200, height=25)

window.mainloop()"""

# 5
# 1 kilometre = 0.6214 miles
# 1  mile = 1.6093 kilometres.

"""one_km = 1.6093
one_mile = 0.6214

window = Tk()
window.title("Main Window")
window.geometry("500x400")


def km_to_m():
    kilometers = entry_box.get()
    km_float = float(kilometers)
    miles_converter = km_float * one_mile
    miles_rounded = round(miles_converter, 4)
    miles = str(miles_rounded)
    message_box["bg"] = "black"
    message_box["fg"] = "yellow"
    message_box["text"] = miles
    entry_box.delete(0, END)
    entry_box.focus()


def m_to_km():
    miles = entry_box.get()
    miles_float = float(miles)
    kilometers_converter = miles_float * one_km
    km_rounded = round(kilometers_converter, 4)
    kilometers = str(km_rounded)
    message_box["bg"] = "black"
    message_box["fg"] = "yellow"
    message_box["text"] = kilometers
    entry_box.delete(0, END)
    entry_box.focus()


def reset():
    message_box["bg"] = "white"
    message_box["text"] = ""


label = Label(text="Please enter distance here: :")
label.place(x=-70, y=10, width=300, height=25)

entry_box = Entry(text="")
entry_box.place(x=150, y=10, width=200, height=25)

message_box = Message(text="")
message_box["bg"] = "white"
message_box.place(x=150, y=40, width=200, height=25)

button1 = Button(text="Convert to Km", command=m_to_km)
button1.place(x=150, y=80, width=200, height=25)

button2 = Button(text="Convert to miles", command=km_to_m)
button2.place(x=150, y=110, width=200, height=25)

button3 = Button(text="Reset", command=reset)
button3.place(x=150, y=140, width=200, height=25)

window.mainloop()"""

# 6
"""window = Tk()
window.title("Main Window")
window.geometry("500x400")


def click():
    number = entry_box.get()
    if number.isdigit():
        int_num = int(number)
        numbers.insert(END, int_num)
        message_box["bg"] = "white"
        message_box["text"] = ""
        entry_box.delete(0, END)
        entry_box.focus()
    else:
        message_box["bg"] = "black"
        message_box["fg"] = "white"
        message_box["text"] = "Not a valid digit"
        entry_box.delete(0, END)


label = Label(text="Enter number here")
label.place(x=-70, y=10, width=300, height=25)

entry_box = Entry(text="")
entry_box.place(x=150, y=10, width=200, height=25)

numbers = Listbox()
numbers.place(x=150, y=40, width=200, height=25)

message_box = Message(text="")
message_box["bg"] = "white"
message_box.place(x=150, y=70, width=200, height=25)

button = Button(text="Click here", command=click)
button.place(x=150, y=100, width=200, height=25)

window.mainloop()"""

# 7
"""window = Tk()
window.title("Main Window")
window.geometry("500x400")


def click():
    number = entry_box.get()
    if number.isdigit():
        int_num = int(number)
        numbers.insert(END, int_num)
        message_box["bg"] = "white"
        message_box["text"] = ""
        entry_box.delete(0, END)
        entry_box.focus()
    else:
        message_box["bg"] = "black"
        message_box["fg"] = "white"
        message_box["text"] = "Not a valid digit"
        entry_box.delete(0, END)


def save_to_file():
    with open("numbers_listbox.csv", "w") as n:
        temp_list = numbers.get(0, END)
        for i in temp_list:
            value = str(i) + "\n "
            n.write(value)
        n.close()


def close_window():
    window.destroy()


label = Label(text="Enter number here")
label.place(x=-70, y=10, width=300, height=25)

entry_box = Entry(text="")
entry_box.place(x=150, y=10, width=200, height=25)

numbers = Listbox()
numbers.place(x=150, y=40, width=200, height=25)

message_box = Message(text="")
message_box["bg"] = "white"
message_box.place(x=150, y=70, width=200, height=25)

button = Button(text="Click here", command=click)
button.place(x=150, y=100, width=200, height=25)

button2 = Button(text="Save", command=save_to_file)
button2.place(x=150, y=130, width=200, height=25)

button3 = Button(text="Close", command=close_window)
button3.place(x=150, y=160, width=200, height=25)

window.mainloop()"""

# 8
"""window = Tk()
window.title("Main Window")
window.geometry("500x400")


def create_new():
    file = open("ages.csv", "w")
    file.close()


def save_list():
    file = open("ages.csv", "a")
    name = name_box.get()
    age = age_box.get()
    newrecord = name + ", " + age + "\n"
    file.write(str(newrecord))
    file.close()
    name_box.delete(0, END)
    age_box.delete(0, END)
    name_box.focus()


def close_window():
    window.destroy()


label1 = Label(text="Enter name here")
label1.place(x=-70, y=10, width=300, height=25)

name_box = Entry(text="")
name_box.place(x=150, y=10, width=200, height=25)

label2 = Label(text="Enter number here")
label2.place(x=-50, y=40, width=200, height=25)

age_box = Entry(text="Enter age here")
age_box.place(x=150, y=40, width=200, height=25)

button = Button(text="Create New", command=create_new)
button.place(x=150, y=70, width=200, height=25)

button2 = Button(text="Save List", command=save_list)
button2.place(x=150, y=100, width=200, height=25)

button3 = Button(text="Close", command=close_window)
button3.place(x=150, y=130, width=200, height=25)

window.mainloop()"""
