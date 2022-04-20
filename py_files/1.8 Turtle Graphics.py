import turtle as turtle
import random

# 1
"""turtle.shape("turtle")
turtle.bgcolor("black")
turtle.color("yellow", "black")
for i in range(0, 4):
    turtle.forward(100)
    turtle.right(90)
turtle.exitonclick()"""

# 2
"""turtle.shape("turtle")
turtle.bgcolor("black")
turtle.color("yellow", "black")
for i in range(0, 3):
    turtle.forward(200)
    turtle.left(120)
turtle.exitonclick()"""

# 3
"""turtle.shape("turtle")
turtle.bgcolor("black")
turtle.color("yellow", "black")
radius = 50
turtle.circle(100)
turtle.exitonclick()"""

# OR
"""turtle.shape("turtle")
turtle.bgcolor("black")
turtle.color("yellow", "black")
for i in range(0, 360):
    turtle.forward(1)
    turtle.right(1)"""


# 4
"""turtle.shape("turtle")
turtle.bgcolor("black")
turtle.color("yellow", "black")
turtle.begin_fill()
for i in range(0, 3):
    turtle.hideturtle()
    turtle.penup()
    turtle.forward(60)
    for j in range(0, 4):
        turtle.showturtle()
        turtle.pendown()
        turtle.forward(50)
        turtle.right(90)
turtle.end_fill()
turtle.exitonclick()"""

# 5
"""turtle.shape("turtle")
turtle.bgcolor("black")
turtle.color("yellow", "black")
for i in range(0, 5):
    turtle.forward(100)
    turtle.right(144)
turtle.exitonclick()"""

# 6
"""turtle.shape("turtle")
turtle.bgcolor("black")
turtle.color("yellow", "black")

# (Number:1)
turtle.left(90)
turtle.forward(100)
turtle.penup()
turtle.right(90)
turtle.forward(30)
turtle.pendown()

# (Number:2)
for i in range(0, 3):
    turtle.forward(50)
    turtle.right(90)

turtle.left(180)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)

turtle.penup()
turtle.forward(30)
turtle.pendown()

# (Number:3)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(35)
turtle.right(180)
turtle.forward(35)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)

turtle.exitonclick()"""

# 7
"""turtle.shape("turtle")
turtle.bgcolor("black")
turtle.color("yellow", "black")
colors = ["yellow", "green", "blue", "orange", "white", "pink", "purple",]

for i in range(0, 8):
    turtle.forward(100)
    turtle.left(45)
    turtle.color(random.choice(colors))

turtle.exitonclick()"""

# 8
"""turtle.shape("turtle")
turtle.bgcolor("black")
turtle.color("yellow", "black")

for i in range(0, 10):
    turtle.right(36)
    for j in range(0, 8):
        turtle.forward(50)
        turtle.right(45)

turtle.exitonclick()"""

# 9
"""turtle.shape("turtle")
turtle.bgcolor("black")
turtle.color("yellow", "black")

rand_lines = random.randint(0, 25)
rand_angles = random.randint(0, 100)
rand_length = random.randint(0, 100)

print("Random number of lines is: {}".format(rand_lines))
print("Random angle is: {}".format(rand_angles))
print("Random length is: {}".format(rand_length))
for i in range(0, rand_lines):
    turtle.forward(rand_length)
    turtle.right(rand_angles)

turtle.exitonclick()"""


