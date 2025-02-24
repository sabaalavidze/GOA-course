from turtle import *

# We want to paint a house

# Step 1: Draw a square
shape("turtle")
width(7)
color("blue")
for _ in range(4):
    forward(100)
    left(90)

# Drawing a door
forward(35)
color("brown")
left(90)
forward(50)  # Height of the door
right(90)
forward(30)
right(90)
forward(50)
left(90)
backward(35)

# Drawing the roof
penup()
goto(0, 100)
pendown()
color("red")
begin_fill()
left(45)
forward(70)
right(90)
forward(70)
end_fill()

# Drawing the left window
penup()
goto(10, 60)
pendown()
color("white")
for _ in range(4):
    forward(20)
    right(90)

# Drawing the right window
penup()
goto(70, 60)
pendown()
for _ in range(4):
    forward(20)
    right(90)

hideturtle()
exitonclick()


