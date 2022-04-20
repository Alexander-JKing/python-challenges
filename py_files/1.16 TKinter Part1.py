from tkinter import *
import random

# 1
# Create a window that will ask the user to enter their name.
# When they click on a button it should display the message "Hello"
# and their name and change the background colour and font colour of the
# message box.

# 1) define function that changes the specified outputs
# 2) Create label asking question
# 3) Create entry box that will retrieve the user name
# 4) Create button that will call function when clicked
# 5) Create Message Box that will return the results.

"""window = Tk()
window.title("Main Window")
window.geometry("450x300")


def click():
    name = entry_box.get()
    message = str("Hello " + name)
    message_box["bg"] = "black"
    message_box["fg"] = "yellow"
    message_box["text"] = message


label = Label(text="Enter Name: ")
label.place(x=50, y=20, width=100, height=25)

entry_box = Entry(text="")
entry_box.place(x=150, y=20, width=100, height=25)
entry_box["justify"] = "left"
entry_box.focus()

message_box = Message(text="")
message_box.place(x=150, y=50, width=100, height=50)
message_box["bg"] = "red"
message_box["fg"] = "red"

button = Button(text="Click Here", command=click)
button.place(x=250, y=20, width=100, height=25)

window.mainloop()"""


# 2
"""def rand_num():
    rand_int = random.randint(0, 6)
    message_box["text"] = rand_int
    return rand_int


window = Tk()
window.title("Main Window")
window.geometry("450x300")

label = Label(text="Click button for random integer 1-6")
label.place(x=0, y=20, width=500, height=25)

message_box = Message(text="")
message_box.place(x=250, y=80, width=100, height=25)
message_box["bg"] = "black"
message_box["fg"] = "yellow"

button = Button(text="Click Here", command=rand_num)
button.place(x=250, y=50, width=100, height=25)

window.mainloop()"""

# 3
# 1) Ask the user to enter a number into a box
# 2) add that number to a total when button clicked.
# 3) total gets displayed in another box
# 4) Another button that resets the total back to 0 and empties the original text box, ready for them to start again.


# What you do here is, to retrieve the value in the message box, convert it to an int and add it to the value of the
# entry_box then reassign the value in the message_box again in the same function.

"""def add():
    number = entry_box.get()
    number = int(number)
    answer = message_box["text"]
    answer = int(answer)
    add_on = number + answer
    message_box["text"] = add_on


def reset():
    entry_box.delete(0, END)
    message_box["text"] = 0


total = 0
number = 0

window = Tk()
window.title("Main Window")
window.geometry("450x300")

label = Label(text="Counting Numbers")
label.place(x=0, y=20, width=500, height=25)

entry_box = Entry(text=0)
entry_box.place(x=100, y=20, width=500, height=25)

message_box = Message(text=0)
message_box.place(x=0, y=45, width=500, height=25)

button1 = Button(text="Add Numbers", command=add)
button1.place(x=0, y=70, width=500, height=25)

button2 = Button(text="Reset", command=reset)
button2.place(x=0, y=95, width=500, height=25)

window.mainloop()"""
