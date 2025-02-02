
from turtle import *

# We want to paint a house

# Step 1: Draw the base of the house
shape("turtle")
width(7)
color("orange")  
begin_fill()
for _ in range(4):
    forward(100)
    left(90)
end_fill()

# Drawing the door
penup()
goto(35, 0)
pendown()
color("brown")
begin_fill()
left(90)
forward(50)  # Height of the door
right(90)
forward(30)
right(90)
forward(50)
right(90)
forward(30)
end_fill()

# Drawing the roof
penup()
goto(0, 100)
pendown()
color("darkred")  
begin_fill()
goto(50, 150)  
goto(100, 100)
goto(0, 100)
end_fill()

# Drawing the left window
penup()
goto(25, 70)  
pendown()
color("lightblue")  
begin_fill()
for _ in range(4):
    forward(20)
    right(90)
end_fill()

# Drawing the right window
penup()
goto(85, 70) 
pendown()
begin_fill()
for _ in range(4):
    forward(20)
    right(90)
end_fill()

hideturtle()
exitonclick()

