from turtle import *

Ryan = Turtle()

Ryan.color("blue")
Ryan.pensize(12)
Ryan.speed(2)
Ryan.shape("turtle")

def square():
Ryan.forward(100)
Ryan.left(90)
Ryan.forward(100)
Ryan.left(90)
Ryan.forward(100)
Ryan.left(90)
Ryan.forward(100)
Ryan.left(90)

def triangle():
Ryan.forward(45)
Ryan.left(120)
Ryan.forward(45)
Ryan.left(120)
Ryan.forward(45)
Ryan.left(120)

triangle()

mainloop()